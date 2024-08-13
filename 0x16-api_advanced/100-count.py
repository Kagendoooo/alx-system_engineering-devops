#!/usr/bin/python3
"""Count words in all hot posts titles from a subreddit recursively"""
import requests


def count_words(subreddit, word_list, after="", count={}):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "0x16.api.advanced/v1.0.0"
    }
    params = {
        "after": after,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return
    posts = response.json().get("data", {}).get("children", [])
    after = response.json().get("data", {}).get("after", None)
    if not count:
        count = {word.lower(): 0 for word in word_list}
    for post in posts:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in title:
            if word in count:
                count[word] += 1
    if after is not None:
        return count_words(subreddit, word_list, after, count)
    sorted_count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_count:
        if count > 0:
            print(f"{word}: {count}")
    return count
