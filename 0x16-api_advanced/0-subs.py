#!/usr/bin/python3

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers to the subreddit.

    Parameters:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers to the subreddit. Returns 0 if the subreddit is not found or an error occurs.
    """
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/about.json".format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)

    if sub_info.status_code >= 300:
        return 0

    subscribers_count = sub_info.json().get("data", {}).get("subscribers", 0)

    return subscribers_count
