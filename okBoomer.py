def send_tweet(request):

    # Importing the libraries we'll use
    import tweepy
    import os
    import random
    from os import getenv
    

    # Getting the key and secret codes from my environment variables
    consumer_key = getenv("consumer_key")
    consumer_secret = getenv("consumer_secret")
    access_token = getenv("access_token")
    access_secret = getenv("access_secret")


    # Tweepy's process for setting up authorisation
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)


    # A list of words that sound like "boomer"
    oomer_list=["rumour", "bloomer", "humour", "puma", "fumer"]


    # For each work that sounds like "boomer"
    for oomer in oomer_list:
        
        # Search Twitter for tweets containing this word
        oomer_search = api.search(q=oomer)
        
        # Select a random tweet from the list
        random_oomer = random.choice(oomer_search)
        
        # Get the text of that tweet (we're only doing it so you can see it if you want to)
        random_oomer_text=random_oomer.text
        
        # Get the ID of the tweet (we need this to send a response to the tweet)
        random_oomer_id=random_oomer.id

        print (random_oomer_id, ">>>", random_oomer_text,"""

            """)
        
        # Creating the message you want to send
        message = "OK {}".format(oomer)

        
        # Sending the message using the status id to reply
        api.update_status(message,in_reply_to_status_id=random_oomer_id, auto_populate_reply_metadata=True)
