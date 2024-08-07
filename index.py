# This code is for research mental health using python
# Author : Fauzi Fadhlurrohman

import tweepy
import re
from transformers import pipeline
import pandas as pd

# Step 1 Collecting Data

## Setup Twitter API authentication
auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')
api = tweepy.API(auth)

## Collect tweets
query = "depresi OR kecemasan OR stres OR bantuan"
tweets = tweepy.Cursor(api.search_tweets, q=query, lang="id").items(1000)

tweet_data = []
for tweet in tweets:
    tweet_data.append(tweet.text)

# Step 2 Process Data

def clean_tweet(tweet):
    tweet = re.sub(r"http\S+", "", tweet)  # Remove URLs
    tweet = re.sub(r"@\S+", "", tweet)  # Remove mentions
    tweet = re.sub(r"#\S+", "", tweet)  # Remove hashtags
    tweet = re.sub(r"[^\w\s]", "", tweet)  # Remove punctuation
    tweet = tweet.lower()  # Convert to lowercase
    return tweet

clean_tweets = [clean_tweet(tweet) for tweet in tweet_data]

# Step 3 Analysis

sentiment_pipeline = pipeline('sentiment-analysis', model='indobenchmark/indobert-base-p1')
sentiments = [sentiment_pipeline(tweet) for tweet in clean_tweets]

# Step 4 Classification

df = pd.DataFrame(sentiments)
df['tweet'] = clean_tweets
df.to_csv('sentiment_analysis_results.csv')

