import urllib
import simplejson
import json
import nltk
import re
import networkx as nx

def get_rt_sources(tweet):
    rt_patterns = re.compile(r"(RT|via)((?:\b\W*@\w+)+)", re.IGNORECASE)
    return [source.strip()
                for tuple in rt_patterns.findall(tweet)
                    for source in tuple 
                         if source not in ("RT", "via")]

def searchTweets(query):
    search = urllib.urlopen("http://search.twitter.com/search.json?q=" + query)
    dict = simplejson.loads(search.read())
    
    tweets_dtl = []
    for result in dict['results']:
        tweets_dtl.append(result)
        # print "Tweet Details: %s\n" % result

    print json.dumps(tweets_dtl, sort_keys = True, indent = 1)
    tweets = [r['text'] for r in tweets_dtl]
    
    words = []
    for t in tweets:
        print "Tweet: %s\n" % t
        # Extract all words in tweets
        words += [w for w in t.split()]

    # Length of all words
    len_all_words = len(words)
    print "All words is %s\n" % len_all_words
    # Length of unique words
    len_unique_words = len(set(words))
    print "Unique words is %s\n" % len_unique_words

    # Lexical Diversity
    ld = 1.0 * len_unique_words / len_all_words
    print "Lexical Diversity is %s\n" % ld

    # Average words per tweet
    awpt = 1.0 * len_all_words / len(tweets)
    print "Average words per tweet is %s\n" % awpt

    # Frequency distribution
    freq_dist = nltk.FreqDist(words)
    print "Frequency Distribution: %s" % freq_dist
    print "50 most frequet terms: %s\n" % freq_dist.keys()[:50]
    print "50 least frequent terms: %s\n" % freq_dist.keys()[-50:]

    # Find retweets
    rt_patterns = re.compile(r"(RT|via)((?:\b\W*@\w+)+)", re.IGNORECASE)
    print "Retweets: \n"
    for t in tweets:
        retweet = rt_patterns.findall(t)
        if retweet:
            print retweet

    # Tweets graph
    g = nx.DiGraph()
    for tweet in tweets_dtl:
        rt_sources  = get_rt_sources(tweet["text"])
        if not rt_sources: continue
        for rt_source in rt_sources:
            g.add_edge(rt_source, tweet["from_user"], {"tweet_id" : tweet["id"]})

    # No. of nodes in the graph
    print "\nNo.of nodes in graph is %s\n" % g.number_of_nodes()
    # No. of edges in the graph
    print "No. of edges in the graph is %s\n" % g.number_of_edges()

    # The first edge in the graph
    #print "The first edge in the graph is %s\n" % (g.edges(data=True)[0])

    # Length of the undirected version of the graph
    print "Length of an undirected version of the graph is %s\n" % len(nx.connected_components(g.to_undirected()))

    # Degree of the graph
    print "Degree of the graph is %s\n" % nx.degree(g)

searchTweets("#ChelseaFC&rpp=500")
