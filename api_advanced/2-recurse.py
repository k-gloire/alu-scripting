#!/usr/bin/python3
"""Recursively collects the titles of all hot posts of a subreddit."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Returns a list of all hot post titles, or None if invalid."""
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting/1.0"}
    try:
        res = requests.get(url, headers=headers,
                           params={"after": after, "limit": 100},
                           allow_redirects=False)
        if res.status_code != 200:
            return None
        data = res.json().get("data", {})
    except (requests.RequestException, ValueError):
        return None

    for child in data.get("children", []):
        hot_list.append(child.get("data", {}).get("title"))

    after = data.get("after")
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
