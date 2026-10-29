#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Prints first 10 hot post titles, or OK if the request fails."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting/1.0"}
    try:
        res = requests.get(url, headers=headers, params={"limit": 10},
                           allow_redirects=False)
        if res.status_code != 200:
            print("OK", end="")
            return
        posts = res.json().get("data", {}).get("children", [])
    except (requests.RequestException, ValueError):
        print("OK", end="")
        return
    for post in posts:
        print(post.get("data", {}).get("title"))
