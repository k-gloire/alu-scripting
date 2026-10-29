#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """DEBUG version: prints status info."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting/1.0"}
    try:
        res = requests.get(url, headers=headers, params={"limit": 10},
                           allow_redirects=False)
    except Exception as e:
        print(type(e).__name__, str(e)[:150])
        return
    print(res.status_code, res.headers.get("Location"))
    print(res.text[:150])
