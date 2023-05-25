"""
Task 2

Requests using concurrent and multiprocessing libraries

Download all comments from a subreddit of your choice using
URL: https://api.pushshift.io/reddit/comment/search/ .

As a result, store all comments in chronological order in JSON
and dump it to a file. For this task use concurrent and
multiprocessing libraries for making requests to Reddit API.
"""

import multiprocessing
from multiprocessing import Queue
import requests
from datetime import datetime
import json




def download_from_url(sub_reddit: str, q: Queue) -> None:
    """
    API URL downloader

    :param sub_reddit: A sub forum of the reddit site
    :param q: A multiprocessing queue
    :return: None
    """

    urlbase = f'https://api.pushshift.io/reddit/comment/search' \
              f'?limit=2&order=desc&subreddit={sub_reddit}&after=05_02_2023'

    print(f'Download from {urlbase=}')

    try:
        response = requests.get(urlbase, headers={'User-Agent': "Url downloader by Serhii_Miroshnychenko"})
    except requests.exceptions.SSLError as e:
        print(e.__class__, e)
    else:
        print(f"Status code: {response.status_code}")
        response_dict = response.json()
        q.put(response_dict)


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
    queue_ = Queue()
    downloaders = []

    for subreddit in ('r/ideavim', 'r/python', 'r/ukraine'):
        downloader = multiprocessing.Process(target=download_from_url, args=(subreddit, queue_,))
        downloaders.append(downloader)

    for process_ in downloaders:
        process_.start()
        process_.join()

    dicts = []
    for elem in iter(queue_.get, None):
        dicts.append(elem)
        if queue_.empty():
            break

    for ds in dicts[1]['data']:
        dicts[0]['data'].append(ds)
    for ds in dicts[2]['data']:
        dicts[0]['data'].append(ds)

    res = dicts[0]['data']

    list_of_dicts_sort(res)

    with open('comments.json', 'w') as f:
        json.dump(res, f, indent=4)
    print('Written to file "comments.json" successfully.')


if __name__ == "__main__":
    main()
