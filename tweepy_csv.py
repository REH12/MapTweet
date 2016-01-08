# Finds all the tweets within a radius of 500km of the center of the UK (roughly) and
# stores the time, tweet text, and geo location data (lat/lon) in a CSV file
# using the tweepy package

import tweepy
import csv

# Enter users consumer key, consumer secret, access token and access secret below:

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Open/Create a file to append data
csvFile = open('friendtweets.csv', 'a')

#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search, geocode="54.02,-2.04,500km").items():
	if tweet.coordinates != None:
		print(tweet.created_at, tweet.text, tweet.coordinates)
		csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'), tweet.coordinates])