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
    print(json_string)
    for bill in data:
        if bill['latest_major_action_date'] == get_current_date():
            # An array of all the updated bill names
            post_list_array.append(bill["bill_slug"])

            # All the data of the updated bills
            post_list_dict[bill["bill_slug"]] = bill

    if len(post_list_array) % 20 == 0 and len(post_list_array) != 0:
        offset = str(len(post_list_array))
        url = CONSTANTS.UPDATED_URL + offset
        get_data(url=url)

    print(post_list_array)
    build_updated_bills_text(
        post_list_array=post_list_array, post_list_dict=post_list_dict)


# Building the text for the daily update
def build_daily_update_text(post_list_array):
    progress = ""
    update_updates = ""
    daily_update = "Good Evening! "
    size = len(post_list_array)

    if size == 0:
        print()
        progress = "Congress was chilling today. No activity from them yesterday. Have a good night! " + \
            '\U0001F971' + '\U0001F634'
        return daily_update + progress
    elif size == 1:
        update_updates = " update "
        progress = "Congress did something yesterday. "
    elif size < 10 and size > 0:
        update_updates = " updates "
        progress = "Congress was making moves yesterday. "
    elif size >= 10:
        progress = "Congress was really busy yesterday. "
        update_updates = " updates "
    else:
        progress = "I'm bugging. " + '\U0001F47E' + " Please help @PolynomoDev"

    daily_update = daily_update + progress + \
        str(size) + " new" + update_updates + "yesterday! Check the thread!"
    return daily_update


# Returns the member's twitter username
def get_member_info(url):
    response = requests.get(url=url, headers=CONSTANTS.header)
    twitter_account = response.json()['results'][0]['twitter_account']
    if twitter_account == None:
        twitter_account = response.json(
        )['results'][0]['first_name'] + " " + response.json()['results'][0]['last_name']
    else:
        twitter_account = "@" + twitter_account
    return twitter_account


# Builds the text format for a new updated bill
def build_updated_bills_text(post_list_array, post_list_dict):
    # count = 0

    for bill in post_list_array:
        # if count == 1:
        #     break
        updated_bill_tweet = "" + \
            post_list_dict[bill]['number'] + "\n" + \
            post_list_dict[bill]['short_title'] + "\n"
        updated_bill_tweet = updated_bill_tweet + "\U0001F464: " + \
            get_member_info(post_list_dict[bill]['sponsor_uri']) + "\n"
        updated_bill_tweet = updated_bill_tweet + "\U0001F6A8: " + \
            post_list_dict[bill]['latest_major_action'] + "\n"

        # party_emoji = ""
        # if post_list_dict[bill]['sponsor_party'] == "D":
        #     party_emoji = "\U0001F7E6"
        # elif post_list_dict[bill]['sponsor_party'] == "R":
        #     party_emoji = "\U0001F7E5" \U0001F464
        all_post_text.append(updated_bill_tweet)
        # count+=1


# Divides the post into 280 character long chunks.
def divide_post(message):
    if len(message) > 278:
        parts = math.ceil(len(message) / 278)
        message = re.split(r'(\s+|\n)', message)

        messagelength = math.ceil(len(message) / parts)
        chunks = [
            message[i: i + messagelength]
            for i in range(0, len(message), messagelength)
        ]
        message_chunks = []
        for i, j in enumerate(chunks):
            message_chunks.append(
                f"({i+1}/{len(chunks)}) " + "".join(j).strip())
        return message_chunks
    else:
        return [message]

# Posts the tweet in such a way that they are all threaded together
# def post_tweet(message, reply=None):
#     return CONSTANTS.twitter.update_status(status=message, in_reply_to_status_id=reply.id, auto_populate_reply_metadata=True)


get_data(CONSTANTS.UPDATED_URL)

text = build_daily_update_text(post_list_array)
print(text)
# previous_message = CONSTANTS.twitter.update_status(status=text, auto_populate_reply_metadata=True)
# for message in all_post_text:
#     for i in divide_post(message):
#         print(i)
#         previous_message = post_tweet(i, previous_message)

print("hello")
