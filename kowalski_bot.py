import tweepy, logging, time
from config.config import create_api
from sentiments import sentiment_analyzer_scores
from retrieve_tweets import retrieve_tweets
from word_cloud import generate_wordcloud
from random import random
import preprocessor as p
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def listen(api, since_id):
    logger.info("Retrieving mentions")
    me = api.me()
    new_since_id = since_id
    screen_name = f'@{me.screen_name}'
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None: # check if the current tweet is a reply to another tweet.
            continue # only interested in main tweets and not replies
        logger.info(f"Answering to {tweet.user.name}")

        if tweet.user.id != me.id and not tweet.user.following: # follow the user who summoned the bot and not self
            tweet.user.follow()
        # remove username part
        keyword = str( p.clean(tweet.text)).replace(f'{screen_name}', "")
        print(f'{keyword}')

        if keyword == "": # query is empty
            api.update_status(
                status= f'{random()} Im gonna need a topic for query and analysis',
                in_reply_to_status_id=tweet.id,
            )
        else:

            generate_wordcloud(retrieve_tweets(keyword), f'For you {tweet.user}', f'wordcloud/{tweet.user.id}.png')
            img_file = open(f'wordcloud/{tweet.user.id}.png','rb')
            wordcloud_img = api.media_upload(filename=f'wordcloud/{tweet.user.id}.png', file=img_file)

            api.update_status(
                status=sentiment_analyzer_scores(retrieve_tweets(keyword)), # results of the analysis
                in_reply_to_status_id=tweet.id,
                media_ids=[wordcloud_img.media_id_string]
            )
    return new_since_id

api = create_api()

since_id = 1
while True:
    since_id = listen(api, since_id)
    logger.info("Ready on my mark...")
    time.sleep(60)