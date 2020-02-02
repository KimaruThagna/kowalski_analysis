import tweepy
import logging
from config.config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def listen(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None: # check if the current tweet is a reply to another tweet.

            logger.info(f"Answering to {tweet.user.name}")
            if not tweet.user.following: # follow the user who summoned the bot
                tweet.user.follow()

            api.update_status(
                status="Please reach us via DM", # results of the analysis
                in_reply_to_status_id=tweet.id,
            )
    return new_since_id