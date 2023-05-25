# Task 3

# Requests using multiprocessing
# Download all comments from a subreddit of your choice using
# URL: https://api.pushshift.io/reddit/comment/search/ .
# As a result, store all comments in chronological order in JSON
# and dump it to a file. For this task use Threads for making requests
# to reddit API.

"""
DOWNLOAD IN DIFFERENT FILES
"""

from concurrent.futures import ThreadPoolExecutor
import requests
import json
import os


def download_from_url(sub_reddit: str) -> None:
    """
    API URL downloader
    :param sub_reddit: A sub forum of the reddit site
    :return: None
    """

    file_name = f'{sub_reddit}_comments.json'

    print(f'Saving to "{file_name}".')
    urlbase = f'https://api.pushshift.io/reddit/comment/search' \
              f'?limit=10&order=desc&subreddit={sub_reddit}&after=05_02_2023'

    print(f'{urlbase=}')

    try:
        response = requests.get(urlbase, headers={'User-Agent': "Url downloader by Serhii_Miroshnychenko"})
    except requests.exceptions.SSLError as e:
        print(e.__class__, e)
    else:
        print(f"Status code: {response.status_code}")
        response_dict = response.json()
        filename = os.path.basename(file_name)
        with open(filename, 'w') as f:
            json.dump(response_dict, f, indent=4)


def main():
    subreddits = ('r/ideavim', 'r/python', 'r/pycharm')

    with ThreadPoolExecutor() as executor:
        executor.map(download_from_url, subreddits)


if __name__ == "__main__":
    main()
