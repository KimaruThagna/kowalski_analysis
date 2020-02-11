from config.config import create_api
import preprocessor as p
api = create_api()

def retrieve_tweets(keyword, number=100):
    tweet_block = ''
    for tweet in api.search(q=keyword, lang="en", rpp=number):  # most recent 100 public tweets that contain the query word
        tweet_block = f'{tweet_block} {p.clean(tweet.text)}'  # accumulate all tweets into one major string

    return tweet_block  # derive a general sentiment from all the tweets
