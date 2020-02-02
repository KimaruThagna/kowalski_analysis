import tweepy, logging, time
from config.config import create_api

def retrieve_tweets(keyword):
    for tweet in api.search(q=keyword, lang="en", rpp=10):
        print(f"{tweet.user.name}:{tweet.text}")