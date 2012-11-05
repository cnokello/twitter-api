import urllib
import simplejson
import json

def searchTweets(query):
    search = urllib.urlopen("http://search.twitter.com/search.json?q=" + query)
    dict = simplejson.loads(search.read())
    
    tweets = []
    for result in dict['results']:
        tweets.append(result)
        print "Tweet: %s\n" % result

searchTweets("#ChelseaFC&rpp=50")
