#!/usr/bin/python3
""" A function that queries the Reddit API and 
returns the number of subscribers """

import requests


def number_of_subscribers(subreddit):

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {"User-Agent": "Mozilla/5.0"}

    try:

        res = requests.get(url, headers=headers, allow_redirects=False)

        if res.status_code == 200:

            data = res.json()

            subscribers = data["data"]["subscribers"]

            return subscribers
        else:

            return 0
    except Exception as e:

        print(f"An error occurred: {e}")
        return 0
