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
        with open(filename, 'a') as f:
            print('Start')
            json.dump(response_dict, f, indent=4)
            print('Ok')


subreddits = ('r/ideavim', 'r/python', 'r/pycharm')

with ThreadPoolExecutor() as executor:
    executor.map(download_from_url, subreddits)



