import requests
import tweepy
import time

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Meme API URL
meme_api_url = "https://api.example.com/memes"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Function to fetch a meme from the API
def fetch_meme():
    response = requests.get(meme_api_url)
    if response.status_code == 200:
        meme_data = response.json()
        meme_url = meme_data['url']
        return meme_url
    else:
        return None

# Function to post a meme on Twitter
def post_meme_on_twitter():
    meme_url = fetch_meme()
    if meme_url:
        api.update_status(status="Check out this meme!", media_ids=[api.media_upload(meme_url).media_id])

# Post memes three times a day with an hour gap
for _ in range(3):
    post_meme_on_twitter()
    time.sleep(3600)  # Sleep for 1 hour (3600 seconds)
