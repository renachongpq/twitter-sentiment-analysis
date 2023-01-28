import sys
sys.path.insert(0, r'C:\Users\renac\Downloads\Computing\Github')

from twitter_authentication import consumer_key, consumer_secret, access_token, access_token_secret, bearer_token
# from twitter_authentication import bearer_token
import tweepy
import csv

# print(consumer_key)


# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)

# print(api.verify_credentials().screen_name) # print if authentication is successful


client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, 
                    access_token=access_token, access_token_secret=access_token_secret,
                    bearer_token=bearer_token)
# client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

csvFile = open('test_tweet', 'a')
csvWriter = csv.writer(csvFile)

search_words = '(grammys or grammy) lang:en -is:retweet -is:reply -is:quote'
tweets = client.search_recent_tweets(query=search_words, max_results=10, tweet_fields=['id', 'text', 'author_id', 'created_at', ])
# tweets = api.search_tweets(q=search_words, lang='en',result_type='mixed', count='3', tweet_mode="extended")
print(tweets.data)
for tweet in tweets.data:
    print(tweet)
    # print(tweet.text)
    print("==============")
