# A test file for printing recent bills. It is for troubleshooting.

import json
import pprint
import tweepy
import requests
from datetime import date
import pprint

# Propublica KEYS + URLs
PROPUBLICA_API_KEY = "Zcj8pKTOxuFf8i44KbBIfU8o6cmFmLQ7nEXOb3EA"
UPCOMING_URL = "https://api.propublica.org/congress/v1/bills/upcoming/house.json"
UPDATED_URL = "https://api.propublica.org/congress/v1/118/both/bills/updated.json"
ENACTED_URL = "https://api.propublica.org/congress/v1/118/both/bills/enacted.json"
SPECIFIC_URL = "https://api.propublica.org/congress/v1/118/bills/"
MEMBER_URL = "https://api.propublica.org/congress/v1/members/.json"

url = "https://api.propublica.org/congress/v1/118/both/bills/updated.json?offset={offset}"

# print(url)

page_number = "3" 

headers = {
    'X-API-KEY': PROPUBLICA_API_KEY
}
params = {
    'page': page_number
}

response = requests.get(url=ENACTED_URL, headers=headers)
data = response.json()['results'][0]['bills']
json_string = json.dumps(data, sort_keys=True, indent=4)
print (json_string)