import twitter

twitter_api = twitter.Twitter(domain = "api.twitter.com", api_version = '1')
WORLD_WOE_ID = 1
world_trends = twitter_api.trends._(WORLD_WOE_ID)
trends = world_trends()
print [trend['name'] for trend in trends[0]['trends']]
