"""
Task 2

Requests using asyncio and aiohttp
Download all comments from a subreddit of your choice using
URL: https://api.pushshift.io/reddit/comment/search/ .

As a result, store all comments in chronological order
in JSON and dump them to a file. For this task use asyncio
and aiohttp libraries for making requests to Reddit API.
"""
import aiohttp
import asyncio
from datetime import datetime
import json


async def get_comment(session, url):
    async with session.get(url) as resp:
        return await resp.json()


async def list_of_dicts_sort(array) -> None:
    for pass_num in range(len(array) - 1, 0, -1):
        for i in range(pass_num):
            i_date = datetime.strptime(array[i]["utc_datetime_str"], "%Y-%m-%d %H:%M:%S")
            ip_date = datetime.strptime(array[i + 1]["utc_datetime_str"], "%Y-%m-%d %H:%M:%S")
            if i_date > ip_date:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp


async def write_file(content):
        with open('comments.json', 'w') as f:
            json.dump(content, f, indent=4)


async def main():

    async with aiohttp.ClientSession() as session:
        results = []
        for subreddit in ('r/ideavim', 'r/python', 'r/ukraine'):
            urlbase = f'https://api.pushshift.io/reddit/comment/search' \
                      f'?limit=10&order=desc&subreddit={subreddit}&after=05_02_2023'
            results.append(asyncio.ensure_future(get_comment(session, urlbase)))

        dicts = await asyncio.gather(*results)

        for ds in dicts[1]['data']:
            dicts[0]['data'].append(ds)
        for ds in dicts[2]['data']:
            dicts[0]['data'].append(ds)

        res = dicts[0]['data']
        print(res)

        await list_of_dicts_sort(res)
        await write_file(res)


asyncio.run(main())
