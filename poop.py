# import json
# import requests

# TWITTER_API_KEY = '4daamXNzmbHiznUVMUo8KHGyQ'
# TWITTER_API_SECRET = 'wktU7MoTKHDgnAirbCTwAf21IH5xV3aQo94mHs98ZFJaViQzQU'
# TWITTER_ACCESS_KEY = '1668811790505967617-J5DV8Y1cGQM4mNI1CklbYMvMBIAXpS'
# TWITTER_ACCESS_SECRET = 'ycbpNcS1fKfGuKJU33D6utKWROhnv121WWcuR8PsYINjK'
# TWITTER_BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAM2soAEAAAAAbxxTvuGcskUhL6nymq9uoBAWGrQ%3DYLC7nxoj09CkgmaQy6FYBvQrp5OXKUz3Pjforf40Yh9Wz1oNnD'

# # Propublica KEYS + URLs
# PROPUBLICA_API_KEY = "Zcj8pKTOxuFf8i44KbBIfU8o6cmFmLQ7nEXOb3EA"
# UPCOMING_URL = "https://api.propublica.org/congress/v1/bills/upcoming/house.json"
# UPDATED_URL = "https://api.propublica.org/congress/v1/118/both/bills/updated.json"
# SPECIFIC_URL = "https://api.propublica.org/congress/v1/118/bills/hr4778.json"
# # MEMBER_URL = "https://api.propublica.org/congress/v1/members/.json"


# header = {
#     'X-API-KEY': PROPUBLICA_API_KEY
# }

# response = requests.get(url=SPECIFIC_URL, headers=header)
# data = response.json()['results'][0]['bill']
# json_string = json.dumps(data, sort_keys=True, indent=4)
# print (json_string)

# text = "h.r.233"
# print(text.upper())

# print(text)

import tweepy
    
TWITTER_API_KEY = '221usDMCFgLVrpH8GWcYRmSRN'
TWITTER_API_SECRET = 'tgZyg3Vz5warXZ7L5qxl4SZkTeA0tfMB6fZujrYziHVksnYyVR'
TWITTER_ACCESS_KEY = '1668811790505967617-eTq2PmxkKWhirpAE0sL5yyWZMKzPeC'
TWITTER_ACCESS_SECRET = 'DX9IcM96cHNXfXw1Gu1MmDzT9htsWRprqFp5Vj895XDtq'

client = tweepy.Client(
    consumer_key=TWITTER_API_KEY,
    consumer_secret=TWITTER_API_SECRET,
    access_token=TWITTER_ACCESS_KEY,
    access_token_secret=TWITTER_ACCESS_SECRET
)

client.create_tweet(text='Test.')