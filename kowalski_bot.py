import tweepy, logging, time
from config.config import create_api
from sentiments import sentiment_analyzer_scores
from retrieve_tweets import retrieve_tweets

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def listen(api, since_id):
    logger.info("Retrieving mentions")
    me = api.me()
    new_since_id = since_id
    screen_name = f'@{me.screen_name}'
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        print(f'>>>>{me.screen_name}>>>>>>>>{tweet.text}')
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None: # check if the current tweet is a reply to another tweet.
            continue # only interested in main tweets and not replies
        logger.info(f"Answering to {tweet.user.name}")
        if not tweet.user.following and tweet.user is not me: # follow the user who summoned the bot and not self
            tweet.user.follow()
        # remove username part
        split_tweet = tweet.text.split(" ")
        keyword = split_tweet[1:]
        keyword = " ".join(keyword)
        if keyword == "": # query is empty
            api.update_status(
                status= f'{new_since_id} Im gonna need a topic for query and analysis',
                in_reply_to_status_id=tweet.id,
            )
        else:
            api.update_status(
                status= sentiment_analyzer_scores(retrieve_tweets(keyword)), # results of the analysis
                in_reply_to_status_id=tweet.id,
            )
    return new_since_id

api = create_api()

since_id = 1
while True:
    since_id = listen(api, since_id)
    logger.info("Ready on my mark...")
    time.sleep(60)