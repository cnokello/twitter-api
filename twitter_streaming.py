import tweepy
import random
import string
import json
import logging

from config import Config
from daemon import Daemon

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth1.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth1)
api.update_status(''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(140)))

class StreamListener(tweepy.StreamListener):
    """
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)
    """

    def on_status(self, status):
        # Do things with the post received. Post is the status object
        logging.debug(status.text)
        message = {
            'author_name': status.author.screen_name,
            'author_id': status.author.id,
            'id': status.id,
            'text': status.text,
            'retweeted': status.retweeted,
            'coordinates': status.coordinates,
            'time': int(time.time())}

        logging.debug(message)
        self.callback(json.dumps(messahe), 'posts')

    def on_error(self, status_code):
        # When there's an error on the stream
        logging.debug('error: %s', status_code)

    def on_timeout(self, track):
        # If no post is received for too long
        logging.debug("Timeout occurred: %s", track)

    def on_limit(self, track):
        # If too many posts match our filter and only a subset is sent to us
        logging.debug("Limit has been reached: %s", track)
        return

    def on_delete(self, status_id, user_id):
        # When a delete notice arrives for a post
        logging.debug("A post delete notice has been received: %s - %s", status_id, user_id)
        return

    def set_tweets(self, t):
        # Set tweets class object
        self.tweets = t

    def on_data(self, data):
        logging.debug(json.dumps(data))
        #print "Process received data here"

    def set_callback(self, callback):
        # Pass callback to call when a new post arrives
        self.callback = callback

class Tweets:
    # Tweets main class
    def __init__(self, pid_file):
        # Constructor
        logging.basicConfig(level=logging.DEBUG)
        #Daemon.__init__(self, pid_file)

    def setup(self):
        # Setup DB connection, Message Queue and Twitter Listerner
        self.setup_stream_listener()

    def setup_stream_listener(self):
        # Setup twitter API streaming listener
        listener = StreamListener()
        listener.set_tweets(self)
        self.stream = tweepy.Stream(auth = auth1, 
                                    listener = listener,
                                    timeout=3600)

    def stream_filter(self):
        # Start listening, based on your chosen criteria
        person_filter = ["Obama", "Odinga", "Oliech", "Ocampo"]
        logging.debug("Persons tracked: %s", person_filter)
        while True:
            try:
                self.stream.filter(track = person_filter)
            except Exception:
                logging.exception("Stream filter exception")
                time.sleep(10)

    def run(self):
        self.setup()
        self.stream_filter()    

if __name__ == "__main__":
    daemon = Tweets("/tmp.tweets.pid")
    daemon.run()    

    """
    sl = StreamListener()
    streamer = tweepy.Stream(auth = auth1, listener = sl)
    setTerms = ['twitter']
    streamer.filter(track = setTerms)
    """
