
import tweepy
import csv

# Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Search query for specific product or category
search_query = "mobile phone -filter:retweets"
tweets = tweepy.Cursor(api.search_tweets, q=search_query, lang="en", tweet_mode='extended').items(100)

# Save extracted data into CSV
with open("social_media_engagement.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Post Content", "Likes", "Retweets", "Hashtags"])
    
    for tweet in tweets:
        hashtags = [ht['text'] for ht in tweet.entities['hashtags']]
        writer.writerow([tweet.full_text, tweet.favorite_count, tweet.retweet_count, hashtags])

print("Social media engagement data saved to social_media_engagement.csv")

