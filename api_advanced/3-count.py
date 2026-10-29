#!/usr/bin/python3
"""Recursively counts keywords in the hot post titles of a subreddit."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Prints a sorted count of keywords found in hot post titles."""
    words = [w.lower() for w in word_list]
    if counts is None:
        counts = {}
        for w in words:
            counts[w] = 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting/1.0"}
    try:
        res = requests.get(url, headers=headers,
                           params={"after": after, "limit": 100},
                           allow_redirects=False)
        if res.status_code == 200:
            data = res.json().get("data", {})
            for child in data.get("children", []):
                title = child.get("data", {}).get("title", "")
                for token in title.lower().split():
                    if token in counts:
                        counts[token] += 1
            after = data.get("after")
            if after is not None:
                return count_words(subreddit, word_list, after, counts)
    except (requests.RequestException, ValueError):
        pass

    results = [(w, c * words.count(w)) for w, c in counts.items() if c > 0]
    for word, total in sorted(results, key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(word, total))
