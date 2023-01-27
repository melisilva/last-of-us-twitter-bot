import tweepy
import random
import time

# Consumer keys and access tokens, used for OAuth
api_key = ''
api_key_secret = ''
bearer_token = ''
access_token = ''
access_token_secret = ''

tweepy_auth = tweepy.OAuthHandler(api_key, api_key_secret)
tweepy_auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(tweepy_auth)
f = open("joel_quotes.txt", "r")
lines = f.readlines()
api.update_status(random.choice(lines))