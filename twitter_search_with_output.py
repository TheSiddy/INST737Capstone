# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 21:50:19 2019

@author: TheSiddy
"""

#!/usr/bin/env python

#-----------------------------------------------------------------------
# twitter-search-geo
#  - performs a search for tweets close to New Cross, London,
#    and outputs them to a CSV file.
#-----------------------------------------------------------------------

from twitter import *

import sys
import csv
latitude = 48.8566
longitude = 2.3522
#latitude = 51.474144    # geographical centre of search
#longitude = -0.035401    # geographical centre of search
max_range = 10             # search range in kilometres
num_results = 100        # minimum results to obtain
outfile = "output.csv"

#-----------------------------------------------------------------------
# load our API credentials
#-----------------------------------------------------------------------
sys.path.append(".")
import config

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))

#-----------------------------------------------------------------------
# open a file to write (mode "w"), and create a CSV writer object
#-----------------------------------------------------------------------
csvfile = open(outfile, "w")
csvwriter = csv.writer(csvfile)

#-----------------------------------------------------------------------
# add headings to our CSV file
#-----------------------------------------------------------------------
row = [ "user", "text", "latitude", "longitude", "location", "language" ]
csvwriter.writerow(row)

#-----------------------------------------------------------------------
# the twitter API only allows us to query up to 100 tweets at a time.
# to search for more, we will break our search up into 10 "pages", each
# of which will include 100 matching tweets.
#-----------------------------------------------------------------------
result_count = 0
last_id = None
while result_count <  num_results:
    #-----------------------------------------------------------------------
    # perform a search based on latitude and longitude
    # twitter API docs: https://dev.twitter.com/rest/reference/get/search/tweets
    #-----------------------------------------------------------------------
    query = twitter.search.tweets(q = "", geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), lang = "fr", count = 100, max_id = last_id)
    print(query, '\n\t')

    for result in query["statuses"]:
        #-----------------------------------------------------------------------
        # only process a result if it has a geolocation
        #-----------------------------------------------------------------------
        if result["lang"]=='en':
            user = result["user"]["screen_name"]
            text = result["text"]
            text = text.encode('ascii', 'replace')
#            latitude = result["geo"]["coordinates"][0]
#            longitude = result["geo"]["coordinates"][1]
            location = result["user"]["location"]
            language = result["lang"]

            #-----------------------------------------------------------------------
            # now write this row to our CSV file
            #-----------------------------------------------------------------------
            row = [ user, text, latitude, longitude, location, language ]
            csvwriter.writerow(row)
            result_count += 1
        last_id = result["id"]

    #-----------------------------------------------------------------------
    # let the user know where we're up to
    #-----------------------------------------------------------------------
    print("got %d results" % result_count)

#-----------------------------------------------------------------------
# we're all finished, clean up and go home.
#-----------------------------------------------------------------------
csvfile.close()

print("written to %s" % outfile)
