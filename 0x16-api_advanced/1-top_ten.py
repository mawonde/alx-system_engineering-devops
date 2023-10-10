#!/usr/bin/python3
""" A function that queries the Reddit API 
and prints the titles of the first 10 hot posts"""

import requests


def top_ten(subreddit):

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {"User-Agent": "Mozilla/5.0"}

    try:

        res = requests.get(url, headers=headers, allow_redirects=False)

        if res.status_code == 200:

            data = res.json()

            if "data" in data:

                posts = data["data"]["children"]

                for post in posts:
                    title = post["data"]["title"]
                    print(title)
            else:
                print("No data found for this subreddit.")
        else:

            print(None)
    except Exception as e:

        print(None)
