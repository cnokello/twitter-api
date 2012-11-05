import tweepy
import random
import string

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth1.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth1)
api.update_status(''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(140)))

class StreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        print "Ran on status"

    def on_error(self, status_code):
        print 'Error: ' + repr(status_code)
        return False

    def on_data(self, data):
        print data
        #print "Process received data here"

sl = StreamListener()
streamer = tweepy.Stream(auth = auth1, listener = sl)
setTerms = ['twitter']
streamer.filter(track = setTerms)
