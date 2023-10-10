#!/usr/bin/python3
"""
a recursive function that queries the Reddit API, parses the
title of all hot articles, and prints a sorted count of given keywords
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):

    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"

    headers = {"User-Agent": "MyBot/1.0 (by YourUsername)"}

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
                    title = post["data"]["title"].lower()

                    words = title.split()

                    for word in word_list:
                        word = word.lower()

                        if word in words:
                            counts[word] = counts.get(word, 0) + words.count(word)

                if after:
                    return count_words(subreddit, word_list, after, counts)
                else:

                    sorted_c = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

                    for word, count in sorted_c:
                        print(f"{word}: {count}")
                    return counts
            else:

                return None
        else:

            return None
    except Exception as e:

        return None
