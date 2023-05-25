import requests
from datetime import datetime
import time
import json


def download_from_url(file_name: str, url_base: str, sub_reddit: str, start_time: datetime, end_time: datetime) -> None:
    """
    API URL downloader
    :param file_name: The name of the file where the query results will be saved
    :param url_base: Base url address
    :param sub_reddit: A sub forum of the reddit site
    :param start_time: Search start time
    :param end_time: Search end time
    :return: None
    """
    print(f'Saving to "{file_name}".')

    start_epoch = str(int(start_time.timestamp()))
    end_epoch = str(int(end_time.timestamp()))

    url = url_base.format(sub_reddit, start_epoch, end_epoch)
    print(f'{url=}')

    try:
        response = requests.get(url, headers={'User-Agent': "Url downloader by Serhii_Miroshnychenko"})  # Робимо запит
    except requests.exceptions.SSLError as e:
        print(e.__class__, e)
    else:
        print(f"Status code: {response.status_code}")  # Атрибут status_code повідомляє нам, чи був запит успішним
        # Зберегти відповідь API у змінну
        response_dict = response.json()

        with open(file_name, 'w') as f:
            json.dump(response_dict, f, indent=4)


if __name__ == "__main__":

    start = datetime.strptime("29_01_2023", "%d_%m_%Y")
    print(type(start))
    end = datetime.strptime("31_01_2023", "%d_%m_%Y")
    s_time = str(start).split(' ')[0]
    e_time = str(end).split(' ')[0]
    filename = f'comments_from_{s_time}_to_{e_time}.json'
    subreddit = 'r/ideavim'
    urlbase = 'https://api.pushshift.io/reddit/comment/search?limit=1000&order=desc&subreddit={}&after={}&before={}'

    download_from_url(file_name=filename, url_base=urlbase, sub_reddit=subreddit, start_time=start, end_time=end)
