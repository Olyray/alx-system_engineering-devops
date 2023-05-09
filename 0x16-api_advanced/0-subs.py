#!/usr/bin/python3
"""Function to request the number of subscribers in a subreddit"""

import requests


def number_of_subscribers(subreddit):
    # Create the required header/headers
    headers = {"User-Agent": "my-bot/0.0.1"}
    # Request the subreddit, using the header
    response = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),  headers=headers)
    # If the response from the request is valid
    if response.status_code == 200:
        # Parse through it and return the total number of subscribers
        subscriber_amount = response.json()
        return subscriber_amount["data"]["subscribers"]
    # Else return 0
    else:
        return 0
