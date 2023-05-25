from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen
import threading
import requests
import json



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
        # print(response_dict)
        with open(file_name, 'w') as f:
            json.dump(response_dict, f, indent=4)
            print('Ok')

# subreddits = ('r/ideavim', 'r/python', 'r/pycharm')
#
#
# with ThreadPoolExecutor() as executor:
#     executor.map(download_from_url, subreddits)


downloader_1 = threading.Thread(target=download_from_url, args=('r/ideavim',))
downloader_2 = threading.Thread(target=download_from_url, args=('r/python',))
downloader_3 = threading.Thread(target=download_from_url, args=('r/pycharm',))

downloader_1.start()
downloader_2.start()
downloader_3.start()

downloader_1.join()
downloader_2.join()
downloader_3.join()




