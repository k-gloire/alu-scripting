#!/usr/bin/python3
"""Queries the Reddit API for the subscriber count of a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Returns total subscribers of a subreddit, or 0 if invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting/1.0"}
    try:
        res = requests.get(url, headers=headers, allow_redirects=False)
        if res.status_code != 200:
            return 0
        return res.json().get("data", {}).get("subscribers", 0)
    except (requests.RequestException, ValueError):
        return 0
