#!/usr/bin/python3
"""
queries the Reddit API,returns the number of subscribers for a subreddit
"""

import requests


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'custom-script/0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    else:
        return 0
