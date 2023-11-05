# A file with constants and the creation up variables that are used repeatedly
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
import requests
import tweepy

# Twitter KEYS
TWITTER_API_KEY = os.environ['TWITTER_API_KEY']
TWITTER_API_SECRET = os.environ['TWITTER_API_SECRET']
TWITTER_ACCESS_KEY = os.environ['TWITTER_ACCESS_KEY']
TWITTER_ACCESS_SECRET = os.environ['TWITTER_ACCESS_SECRET']
TWITTER_BEARER_TOKEN = os.environ['TWITTER_BEARER_TOKEN']

# Propublica KEYS + URLs
PROPUBLICA_API_KEY = os.environ['PROPUBLICA_API_KEY']
UPCOMING_URL = "https://api.propublica.org/congress/v1/bills/upcoming/house.json"
UPDATED_URL = "https://api.propublica.org/congress/v1/118/both/bills/updated.json?offset="
SPECIFIC_URL = "https://api.propublica.org/congress/v1/118/bills/"
NOMINATION_URL = "https://api.propublica.org/congress/v1/118/nominations.json"
FLOOR_ACTION_URL = "https://api.propublica.org/congress/v1/{chamber}/floor_updates/2023/07/25.json"
RECENT_VOTES_URL = "https://api.propublica.org/congress/v1/both/votes/recent.json"
ENACTED_URL = "https://api.propublica.org/congress/v1/118/both/bills/enacted.json"

# Get the current date and time
current_date = datetime.now()

# Format the current date as a string
current_date_string = current_date.strftime('%Y-%m-%d')

# current_date_string = "2023-11-02"

# Calculate yesterday's date
yesterday_date = current_date - timedelta(days=1)

# Format yesterday's date as a string
yesterday_date_string = yesterday_date.strftime('%Y-%m-%d')

# Calculate yesteryesterday's date
yesteryesterday_date = current_date - timedelta(days=2)

# Format yesteryesterday's date as a string
yesteryesterday_date_string = yesteryesterday_date.strftime('%Y-%m-%d')

# Twitter Authentication
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)
twitter = tweepy.API(auth)

client = tweepy.Client(
    consumer_key=TWITTER_API_KEY,
    consumer_secret=TWITTER_API_SECRET,
    access_token=TWITTER_ACCESS_KEY,
    access_token_secret=TWITTER_ACCESS_SECRET
)

header = {
    'X-API-KEY': PROPUBLICA_API_KEY
}


def get_member_info(url):
    response = requests.get(url=url, headers=header)
    twitter_account = response.json()['results'][0]['twitter_account']
    if twitter_account == None:
        twitter_account = response.json(
        )['results'][0]['first_name'] + " " + response.json()['results'][0]['last_name']
    else:
        twitter_account = "@" + twitter_account
    return twitter_account


start_up_prompt = '''Command Options:
(1) Daily Script (Nominations + Enacted)
(2) Print
'''

# API_KEY = getenv("API_KEY")
# API_SECRET = getenv("API_SECRET")
# ACCESS_KEY = getenv("ACCESS_KEY")
# ACCESS_SECRET = getenv("ACCESS_SECRET")
