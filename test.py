import math
import tweepy
import re


data = [
    ['P', 'Y', 'N', 'NV'],
    ['D', '30', '12', '12'],
    ['R', '25', '12', '12'],
    ['I', '35', '12', '12']
]

# Function to print a row
def print_row(row, widths):
    print("| " + " | ".join((val.ljust(width) for val, width in zip(row, widths))) + " |")

# Function to print a line
def print_line(widths):
    print("+-" + "-+-".join('-' * width for width in widths) + "-+")

# Calculate column widths
widths = [max(len(row[i]) for row in data) for i in range(len(data[0]))]

# Print the table
print_line(widths)
print_row(data[0], widths)
print_line(widths)
for row in data[1:]:
    print_row(row, widths)
print_line(widths)


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


# # Gathers and posts data about the most recent updated bills.
# import math
# import CONSTANTS
# import json
# import re
# import requests
# from datetime import datetime, timedelta

# all_post_text = []
# post_list_array = []
# post_list_dict = {}
# offset = 0

# def get_current_date():
#     # Get the current date
#     current_date = datetime.now()

#     # Calculate yesterday's date
#     yesterday_date = current_date - timedelta(days=1)

#     # Format yesterday's date as a string
#     formatted_yesterday_date = yesterday_date.strftime('%Y-%m-%d')

#     return formatted_yesterday_date

# # Gathers the data for the most recent updated tweets
# def get_data(url):
#     response = requests.get(url=url, headers=CONSTANTS.header)
#     data = response.json()['results'][0]['bills']
#     json_string = json.dumps(data, sort_keys=True, indent=4)
#     # print (json_string)

#     for bill in data:
#         if bill['latest_major_action_date'] == get_current_date():
#             print(bill['latest_major_action_date'])
#             print(get_current_date())
#             # An array of all the updated bill names
#             post_list_array.append(bill["bill_slug"])

#             # All the data of the updated bills
#             post_list_dict[bill["bill_slug"]] = bill
    
#     if len(post_list_array) % 20 == 0 and len(post_list_array) != 0:
#         # print(len(post_list_array))
#         # number = len(post_list_array)
#         text = str(len(post_list_array))
#         print(text)
#         url = UPDATED_URL + text
#         print(url)
#         get_data(url=url)


# get_data(UPDATED_URL)
# print(post_list_array)