# A file for printing the JSON file regarding enacted bill data.
import CONSTANTS
import requests
from datetime import datetime

all_post_text = []


def get_data(datum, context):
    response = requests.get(url=CONSTANTS.ENACTED_URL,
                            headers=CONSTANTS.header)
    data = response.json()['results'][0]['bills']

    for bill in data:
        if bill["enacted"] == CONSTANTS.yesterday_date_string or bill["enacted"] == CONSTANTS.current_date_string or bill["enacted"] == CONSTANTS.yesteryesterday_date_string:
            build_text(bill)

        else:
            break

    format_tweet(all_post_text)


def build_text(bill):
    text = str.upper(bill["bill_slug"]) + ": " + bill["short_title"] + "\n"
    text = text + "\U0001F464: " + \
        CONSTANTS.get_member_info(bill['sponsor_uri']) + "\n"
    text = text + "\U0001F4DD: " + "Made law on " + bill['enacted'] + "\n"
    text = text + "|" + "\u2139: " + bill['title']
    all_post_text.append(text)


def format_tweet(all_post_text):
    for message in all_post_text:
        message_list = message.split("|")
        previous_message = CONSTANTS.client.create_tweet(text=message_list[0])
        CONSTANTS.client.create_tweet(
            text=message_list[1], in_reply_to_tweet_id=previous_message.data['id'])


get_data()
