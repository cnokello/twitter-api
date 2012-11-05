import tweepy
import random
import string

consumer_key = 'pmiDbakOGGSUY5gCVZhGkw'
consumer_secret = 'ASqsBnI71ThtZyyK6dx0p2Jf9KO4K2y3iufSU6Q'

access_token = '89438660-ftY2E7ME3A3dzjH3TpvPDQXqV4oMFraLn7pHshcs'
access_token_secret = 'qjMLXeoDHnAqho3R5B5KfArfcXgE2rOLF74c61Vcn7g'

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
