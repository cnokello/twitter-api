import urllib
import simplejson
import json

def searchTweets(query):
    search = urllib.urlopen("http://search.twitter.com/search.json?q=" + query)
    dict = simplejson.loads(search.read())
    count = 1
    print json.dumps(dict["results"])
    """
    for result in dict["results"]:
        print "%s %s \n" % (count, result)
    """
searchTweets("#Nairobi&rpp=50")
