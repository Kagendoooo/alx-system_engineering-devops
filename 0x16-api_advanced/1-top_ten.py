#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed for a subreddit
"""

import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16.api.advanced/v1.0.0"
    }
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    post = response.json().get("data")
    [print(c.get("data").get("title")) for c in post.get("children")]
