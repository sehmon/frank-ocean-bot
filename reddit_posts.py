import praw
import tweepy
import random
from config import *

# Twitter doesn't like duplicate statuses so I had to create this dict lol
# Taken from: http://blog.oxforddictionaries.com/2015/10/ways-to-say-no/

ways_to_say_no = [
        "uh-uh",
        "nix",
        "nixie",
        "nixy",
        "nope",
        "nah",
        "nay",
        'no way',
        'no way Jose',
        'negative',
        'veto',
        'no siree',
        'not on your Nelly',
        'not for all the tea in China',
        'magic 8 ball says no',
        'thumbs down',
        'pigs may fly',
        'fat chance',
        'go fish',
        "are pigs green?"
        ]

ways_to_say_no.extend(['no']*30)

#----------- Reddit stuff --------------

r = praw.Reddit(user_agent = user_agent)

hiphopheads = r.get_subreddit('hiphopheads')
hot_posts = hiphopheads.get_hot()
tweet_string = random.choice(ways_to_say_no)

for post in hot_posts:
    if '[fresh] frank ocean' in post.title.lower():
        tweet_string = "YES! {}: {}".format(post.title, post.short_link)

print tweet_string

#----------- Twitter stuff --------------

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(tweet_string)
