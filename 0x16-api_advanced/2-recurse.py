#!/usr/bin/python3
"""
 a recursive function that queries the Reddit API and returns a list
 containing the titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=None, after=None):

    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"

    headers = {"User-Agent": "Mozilla/5.0"}

    if after:
        url += f"&after={after}"

    try:

        res = requests.get(url, headers=headers, allow_redirects=False)

        if res.status_code == 200:

            data = res.json()

            if "data" in data:

                posts = data["data"]["children"]

                after = data["data"]["after"]

                for post in posts:
                    title = post["data"]["title"]
                    hot_list.append(title)

                if after:
                    return recurse(subreddit, hot_list, after)
                else:
                    return hot_list
            else:

                return None
        else:

            return None
    except Exception as e:

        return None
