import tweepy
import time

# authenticate API
consumer_key = "your code here"
consumer_secret = "your code here"
access_token = "your code here"
access_token_secret = "your code here"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# follow users who follow you
for follower in tweepy.Cursor(api.followers).items():
	if not follower.following:
		follower.follow()