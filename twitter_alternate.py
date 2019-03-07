# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 02:37:41 2019

@author: TheSiddy
"""

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
import json

consumer_key="Nv0UJjhuhJXAnDNuUl3Rr0fwA"
consumer_secret="m4vHuXoh3YQ3rFJt51bKg3N4DncByrKxFVt3nwMyijRrfkQQZF"
access_token="877892050124976128-E8Fws8Yxn1g4cwQWX7efJAcdv3iYWoJ"
access_secret="CQWKjZZXsIXMQ9pU4tgafNJUAb5ILxMBC0Jk4nUn3SMAi"
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status
 
# Status() is the data model for a tweet
tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse
class MyListener(tweepy.StreamListener):
 
    def on_data(self, data):
        try:
            with open('FILENAME.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
#Set the hashtag to be searched
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['dog'])