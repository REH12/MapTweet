import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'ZNFGmPbvdIYgphOShBqnDNz88'
consumer_secret = 'GxVdMqRDmnL9BpAmHdtxI9O1LF08x4Vx8juQ62XTqbCiYqs0Vi'
access_token = '2801629397-XX7B1tHKTaJ0JDBkybCF9c6x9Nh4F7kjIswyHED'
access_secret = 'ZzVBDbHq3P958dffh36bj17Frjhch9HfyTT3VyPzZQRfI'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text) 
