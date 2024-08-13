#!/usr/bin/python3
"""
returns a list containing the titles of all hot articles for a subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "0x16.api.advanced/1.0"}
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return None
        post = response.json().get("data")
        children = post.get("children", [])
        if not children:
            return hot_list if hot_list else None
        for child in children:
            hot_list.append(child.get("data").get("title"))
        after = post.get("after")
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    except requests.RequestException:
        return None
