#!/usr/bin/python3
"""Function to get the top ten hottest posts in a subreddit"""

import requests


def top_ten(subreddit):
    # Create the required header/headers
    headers = {"User-Agent": "my-bot/0.0.1"}
    # Request the subreddit, using the header
    response = requests.get("https://www.reddit.com/r/{}/hot.json?\
                            limit=10".format(subreddit), headers=headers)
    # If the response from the request is valid
    if response.status_code == 200:
        # Parse through it and return the top ten hottest posts
        top_ten = response.json()
        for post in top_ten["data"]["children"]:
            print(post["data"]["title"])
    # Else return 0
    else:
        print(None)
