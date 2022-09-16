import tweepy
import time

consumer_key='JjPzJS1Crcife12gQemaMAAEg'
consumer_secret = 'fybjrtlNPD2geScm3JjTZhWuGj6BvGHWYbeuHw0chJnrsKcgDL'
key='1559268671058366464-Hsd3wTLKhrRZPVCoqDUru7A02ZlVb2'
secret='HqsvDC3e91MgpcCn7DwtLxKiDpkrZWCZR3H0nBvpOMPhH'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)
# api.update_status('Hello from twitter bot-second tweeet')

# print("Status Updated!")


FILE_NAME = 'last_seen.txt'



def read_last_seen(FILE_NAME):
    file_read=open(FILE_NAME, 'r')
    last_seen_id=int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write=open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return 

def reply():
    tweets =api.mentions_timeline(since_id=read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#gregiscoding' in tweet.full_text.lower():
            print("New Tweet Found!")
            print("Replied to ID - "+str(tweet.id))
            api.update_status(status="@"+tweet.user.screen_name + " Hello", in_reply_to_status_id=tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id) 

while True:
    reply()
    time.sleep(15)
