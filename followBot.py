import tweepy
import time

# authenticate API
consumer_key = "api key"
consumer_secret = "secret api key"
access_token = "access token"
access_token_secret = "secret access token"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# follow another user's followers
screen_name = "screen name here"
for follower in api.followers(screen_name):
	follower.follow()