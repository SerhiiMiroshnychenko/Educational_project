from concurrent.futures import ThreadPoolExecutor
import threading
import requests
import json
import os

my_semaphore = threading.BoundedSemaphore(1)

def download_from_url(sub_reddit: str) -> None:
    """
    API URL downloader
    :param sub_reddit: A sub forum of the reddit site
    :return: None
    """

    file_name = 'comments.json'

    print(f'Saving to "{file_name}".')
    urlbase = f'https://api.pushshift.io/reddit/comment/search' \
              f'?limit=3&order=desc&subreddit={sub_reddit}&after=05_02_2023'

    print(f'{urlbase=}')

    try:
        response = requests.get(urlbase, headers={'User-Agent': "Url downloader by Serhii_Miroshnychenko"})
    except requests.exceptions.SSLError as e:
        print(e.__class__, e)
    else:
        print(f"Status code: {response.status_code}")
        response_dict = response.json()
        print(response_dict)
        filename = os.path.basename(file_name)
        with my_semaphore:
            with open(filename, 'a+') as file:
                # First we load existing data into a dict.
                try:
                    file_data = json.load(file)
                # Join new_data with file_data inside emp_details
                    for one_dict in response_dict['data']:
                        file_data['data'].append(one_dict)
                # Sets file's current position at offset.
                    file.seek(0)
                # convert back to json.
                    json.dump(file_data, file, indent=4)
                except json.decoder.JSONDecodeError as e:
                    print(e.__class__, e)
                    json.dump(response_dict, file, indent=4)



downloader_1 = threading.Thread(target=download_from_url, args=('r/ideavim',))
downloader_2 = threading.Thread(target=download_from_url, args=('r/python',))
downloader_3 = threading.Thread(target=download_from_url, args=('r/pycharm',))

downloader_1.start()
downloader_2.start()
downloader_3.start()

downloader_1.join()
downloader_2.join()
downloader_3.join()
