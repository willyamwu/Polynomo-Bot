import requests
import CONSTANTS


def get_data():
    response = requests.get(url=CONSTANTS.NOMINATION_URL,
                            headers=CONSTANTS.header)
    data = response.json()['results'][0]['votes']

    count = 0

    for bill in data:
        if bill['date'] == CONSTANTS.yesterday_date_string:
            build_text(bill=bill)
            count += 1

        else:
            break
    
    if count == 0:
        print("No new nominations for ", CONSTANTS.yesterday_date_string)
        

def build_text(bill):
    description_list = bill['description'].split(',')
    description_text = description_list[0] + description_list[2]
    text = "\U0001F464: " + description_text + "\n"

    if bill['result'] == "Nomination Confirmed":
        result = "CONFIRMED"
    elif bill['result'] == "Nomination Denied":
        result = "DENIED"
    else:
        result = bill['result'].upper()

    text = text + "\U0001F6A8: " + result + "\n"
    text = text + "\U0001F5D3: " + bill['date'] + "\n\n"

    # Total counts
    total_yes = str(bill["total"]['yes']) + "(Y)"
    total_no = str(bill["total"]['no']) + "(N)"
    total_no_vote = str(bill["total"]['not_voting']) + "(NV)"

    # Democratic counts
    dem_yes = str(bill["democratic"]['yes']) + "(Y)"
    dem_no = str(bill["democratic"]['no']) + "(N)"
    dem_no_vote = str(bill["democratic"]['not_voting']) + "(NV)"

    # Republican counts
    rep_yes = str(bill["republican"]['yes']) + "(Y)"
    rep_no = str(bill["republican"]['no']) + "(N)"
    rep_no_vote = str(bill["republican"]['not_voting']) + "(NV)"

    # Independent counts
    ind_yes = str(bill["independent"]['yes']) + "(Y)"
    ind_no = str(bill["independent"]['no']) + "(N)"
    ind_no_vote = str(bill["independent"]['not_voting']) + "(NV)"

    text = text + "TOTAL: " + total_yes + "-" + \
        total_no + "-" + total_no_vote + "\n"
    text = text + "D: " + dem_yes + "-" + dem_no + "-" + dem_no_vote + "\n"
    text = text + "I: " + ind_yes + "-" + ind_no + "-" + ind_no_vote + "\n"
    text = text + "R: " + rep_yes + "-" + rep_no + "-" + rep_no_vote + "\n"

    print(text)

    post_tweet(text)


def post_tweet(text):
    CONSTANTS.client.create_tweet(text=text)


def run():
    get_data()


run()