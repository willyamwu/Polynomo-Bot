import math
import tweepy
import re

# Twitter KEYS
TWITTER_API_KEY = '4daamXNzmbHiznUVMUo8KHGyQ'
TWITTER_API_SECRET = 'wktU7MoTKHDgnAirbCTwAf21IH5xV3aQo94mHs98ZFJaViQzQU'
TWITTER_ACCESS_KEY = '1668811790505967617-J5DV8Y1cGQM4mNI1CklbYMvMBIAXpS'
TWITTER_ACCESS_SECRET = 'ycbpNcS1fKfGuKJU33D6utKWROhnv121WWcuR8PsYINjK'
TWITTER_BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAM2soAEAAAAAbxxTvuGcskUhL6nymq9uoBAWGrQ%3DYLC7nxoj09CkgmaQy6FYBvQrp5OXKUz3Pjforf40Yh9Wz1oNnD'

# Propublica KEYS + URLs
PROPUBLICA_API_KEY = "Zcj8pKTOxuFf8i44KbBIfU8o6cmFmLQ7nEXOb3EA"
UPCOMING_URL = "https://api.propublica.org/congress/v1/bills/upcoming/house.json"
UPDATED_URL = "https://api.propublica.org/congress/v1/118/both/bills/updated.json?offset="
SPECIFIC_URL = "https://api.propublica.org/congress/v1/118/bills/"
# MEMBER_URL = "https://api.propublica.org/congress/v1/members/.json"

# Twitter Authentication
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)
twitter = tweepy.API(auth)

twitter.update_status("Joe Mama")

# def divide_post(message):
#     if len(message) > 280:
#         parts = math.ceil(len(message) / 280)
#         message = re.split(r'(\s+|\n)', message)

#         print(message)

#         messagelength = math.ceil(len(message) / parts)
#         chunks = [
#             message[i : i + messagelength]
#             for i in range(0, len(message), messagelength)
#         ]
#         message_chunks = []
#         for i, j in enumerate(chunks):
#             message_chunks.append(f"({i+1}/{len(chunks)}) " + "".join(j).strip())
#         return message_chunks
#     else:
#         return [message]

# # def divide_post(message):
# #     if len(message) > 280:
# #         parts = math.ceil(len(message) / 280)
# #         message = message.split()

# #         messagelength = math.ceil(len(message) / parts)
# #         chunks = [
# #             message[i : i + messagelength]
# #             for i in range(0, len(message), messagelength)
# #         ]
# #         message_chunks = []
# #         for i, j in enumerate(chunks):
# #             message_chunks.append(f"({i+1}/{len(chunks)}) " + " ".join(j).strip())
# #         return message_chunks
# #     else:
# #         return [message]
    
# print(divide_post("To amend the Federal Water Pollution Control Act and direct the Secretary of the Interior to conduct a study with respect to stormwater runoff from oil and gas operations, and for other purposes. (hr4778-118) \n Sponsor: @RepCartwright \n Update: Referred to the Subcommittee on Water Resources and Environment"))

# # text = "To amend the Federal Water Pollution Control Act and direct the Secretary of the Interior to conduct a study with respect to stormwater runoff from oil and gas operations, and for other purposes. (hr4778-118) \n Sponsor: @RepCartwright \n Update: Referred to the Subcommittee on Water Resources and Environment"
# # print(text.split())


# Gathers and posts data about the most recent updated bills.
import math
import CONSTANTS
import json
import re
import requests
from datetime import datetime, timedelta

all_post_text = []
post_list_array = []
post_list_dict = {}
offset = 0

def get_current_date():
    # Get the current date
    current_date = datetime.now()

    # Calculate yesterday's date
    yesterday_date = current_date - timedelta(days=1)

    # Format yesterday's date as a string
    formatted_yesterday_date = yesterday_date.strftime('%Y-%m-%d')

    return formatted_yesterday_date

# Gathers the data for the most recent updated tweets
def get_data(url):
    response = requests.get(url=url, headers=CONSTANTS.header)
    data = response.json()['results'][0]['bills']
    json_string = json.dumps(data, sort_keys=True, indent=4)
    # print (json_string)

    for bill in data:
        if bill['latest_major_action_date'] == get_current_date():
            print(bill['latest_major_action_date'])
            print(get_current_date())
            # An array of all the updated bill names
            post_list_array.append(bill["bill_slug"])

            # All the data of the updated bills
            post_list_dict[bill["bill_slug"]] = bill
    
    if len(post_list_array) % 20 == 0 and len(post_list_array) != 0:
        # print(len(post_list_array))
        # number = len(post_list_array)
        text = str(len(post_list_array))
        print(text)
        url = UPDATED_URL + text
        print(url)
        get_data(url=url)


get_data(UPDATED_URL)
print(post_list_array)