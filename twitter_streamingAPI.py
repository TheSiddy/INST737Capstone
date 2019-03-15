# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 22:07:34 2019

@author: TheSiddy
"""

import sys
import tweepy

consumer_key="Nv0UJjhuhJXAnDNuUl3Rr0fwA"
consumer_secret="m4vHuXoh3YQ3rFJt51bKg3N4DncByrKxFVt3nwMyijRrfkQQZF"
access_key="877892050124976128-E8Fws8Yxn1g4cwQWX7efJAcdv3iYWoJ"
access_secret="CQWKjZZXsIXMQ9pU4tgafNJUAb5ILxMBC0Jk4nUn3SMAi"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print( status.text)

    def on_error(self, status_code):
        print( sys.stderr, 'Encountered error with status code:', status_code)
        return True # Don't kill the stream

    def on_timeout(self):
        print(sys.stderr, 'Timeout...')
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())    
sapi.filter(locations=[-6.38,49.87,1.77,55.81])
