from concurrent.futures import ThreadPoolExecutor
import threading
import requests
from datetime import datetime
import json
import os



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


dicts = []

for subreddit in ('r/ideavim', 'r/python', 'r/ukraine'):
    with locker:
        downloader = threading.Thread(target=download_from_url, args=(subreddit,))
        downloader.start()
        downloader.join()
        dicts.append(result)


# print(dicts)

for ds in dicts[1]['data']:
    dicts[0]['data'].append(ds)
for ds in dicts[2]['data']:
    dicts[0]['data'].append(ds)

# with open('comments.json', 'w') as f:
#     json.dump(dicts[0]['data'], f, indent=4)
res = dicts[0]['data']
# for elem in res:
#
#     print(type(elem), elem)

def bubble_sort(array):
    for pass_num in range(len(array) - 1, 0, -1):
        for i in range(pass_num):
            el_i = array[i]["utc_datetime_str"]
            el_ip = array[i+1]["utc_datetime_str"]
            # print(f'{el_i=}, {type(el_i)=} ')
            # print(f'{el_ip=}, {type(el_ip)=} ')
            i_date = datetime.strptime(array[i]["utc_datetime_str"], "%Y-%m-%d %H:%M:%S")
            ip_date = datetime.strptime(array[i+1]["utc_datetime_str"], "%Y-%m-%d %H:%M:%S")
            # print(f'{i_date=}, {type(i_date)=}')
            # print(f'{ip_date=}, {type(ip_date)=}')
            # print(f'{i_date} < {ip_date} : {i_date < ip_date}')
            if i_date > ip_date:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp

# 2023-02-05 22:08:25
# start = datetime.strptime("29_01_2023", "%d_%m_%Y")
# start_epoch = str(int(start_time.timestamp()))

# for elem in res:
#     print(elem["utc_datetime_str"], type(elem["utc_datetime_str"]))

bubble_sort(res)
# for elem in res:
#     print(elem["utc_datetime_str"], type(elem["utc_datetime_str"]))
with open('comments.json', 'w') as f:
    json.dump(res, f, indent=4)
