import tweepy
import time

consumer_key='JjPzJS1Crcife12gQemaMAAEg'
consumer_secret = 'fybjrtlNPD2geScm3JjTZhWuGj6BvGHWYbeuHw0chJnrsKcgDL'
key='1559268671058366464-Hsd3wTLKhrRZPVCoqDUru7A02ZlVb2'
secret='HqsvDC3e91MgpcCn7DwtLxKiDpkrZWCZR3H0nBvpOMPhH'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

hashtag="Messi"
tweetNumber =5

tweets= tweepy.Cursor(api.search_tweets, hashtag).items(tweetNumber)
def searchbot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Done!")
            time.sleep(2)
        except tweepy.TweepyException as e:
            print(e.reason)
            time.sleep(2)
searchbot()  