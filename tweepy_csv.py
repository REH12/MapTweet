import tweepy
import csv

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Open/Create a file to append data
csvFile = open('tweets.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#alcoholguidelines").items():
	if tweet.coordinates != None:
		print(tweet.created_at, tweet.text, tweet.coordinates)
		csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'), tweet.coordinates])
