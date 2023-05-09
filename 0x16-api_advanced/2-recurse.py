#!/usr/bin/python3
"""Return a list with all hot posts"""


import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    headers = {'User-Agent': 'my-bot/0.0.1'}
    params = {'limit': 100, 'after': after}
    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit), headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        after = data['data']['after']
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
