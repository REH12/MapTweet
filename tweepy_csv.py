import tweepy
import csv

consumer_key = 'hxJALVpXO0DHOB8rqfGQrqo5d'
consumer_secret = 'zN4XToW9NHuhEQlC13X7mjMIpdf74UDRdxySolCKqlwZyrL4Kj'
access_token = '2925200369-Ih0UU53AuEALRXMBQhtqOjJmNJeF23e63qHRLVI'
access_secret = '3rIgo5eZ9NhLUVTL7UZG36B1LAdc5TUcrchVAVAFd8feF'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Open/Create a file to append data
csvFile = open('friendtweets.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#LoseAFriendIn3Words").items():
	if tweet.coordinates != None:
		print(tweet.created_at, tweet.text, tweet.coordinates)
		csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'), tweet.coordinates])
