# Task 3

# Requests using multiprocessing
# Download all comments from a subreddit of your choice using
# URL: https://api.pushshift.io/reddit/comment/search/ .
# As a result, store all comments in chronological order in JSON
# and dump it to a file. For this task use Threads for making requests
# to reddit API.

"""
DOWNLOAD IN ONE FILE
"""

import threading
import requests
from datetime import datetime
import json


locker = threading.Lock()
result = 0

def download_from_url(sub_reddit: str) -> None:
    """
    API URL downloader
    :param sub_reddit: A sub forum of the reddit site
    :return: None
    """

    global result
    file_name = 'comments.json'

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
        result = response_dict


def list_of_dicts_sort(array) -> None:
    """
    The function for sorting list of dictionaries by date in dictionary
    :param array: unordered list of dictionaries
    :return: None
    """

    for pass_num in range(len(array) - 1, 0, -1):
        for i in range(pass_num):
            i_date = datetime.strptime(array[i]["utc_datetime_str"], "%Y-%m-%d %H:%M:%S")
            ip_date = datetime.strptime(array[i+1]["utc_datetime_str"], "%Y-%m-%d %H:%M:%S")
            if i_date > ip_date:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp


def main():
    global locker
    global result
    global dicts

    for subreddit in ('r/ideavim', 'r/python', 'r/ukraine'):
        with locker:
            downloader = threading.Thread(target=download_from_url, args=(subreddit,))
            downloader.start()
            downloader.join()
            dicts.append(result)

    for ds in dicts[1]['data']:
        dicts[0]['data'].append(ds)
    for ds in dicts[2]['data']:
        dicts[0]['data'].append(ds)

    res = dicts[0]['data']

    list_of_dicts_sort(res)

    with open('comments.json', 'w') as f:
        json.dump(res, f, indent=4)


if __name__ == "__main__":
    locker = threading.Lock()
    result = 0
    dicts = []
    main()
