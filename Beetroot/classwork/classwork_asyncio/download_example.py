import asyncio
import time
import aiohttp
import os


async def download_image(url):
    async with aiohttp.ClientSession() as session:
        responce = await session.get(url)
        image_data = await responce.read()

        # if not image_data:
        #     raise Exception(f"Error: could not download the image from {url}")

        filename = os.path.basename(url)
        with open(filename, 'wb') as image_file:
            image_file.write(image_data)
            print(f'{filename} was downloaded...')


start = time.perf_counter()

urls = ['https://upload.wikimedia.org/wikipedia/commons/9/9d/Python_bivittatus_1701.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/4/48/Python_Regius.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/d/d3/Baby_carpet_python_caudal_luring.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/f/f0/Rock_python_pratik.JPG',
        'https://upload.wikimedia.org/wikipedia/commons/0/07/Dulip_Wilpattu_Python1.jpg']

loop = asyncio.get_event_loop()
print(loop)


async def create_tasks_func():
    tasks = []
    for i in urls:
        task = asyncio.create_task(download_image(i))
        tasks.append(task)
    await asyncio.wait(tasks)


loop.run_until_complete(create_tasks_func())
loop.close()

finish = time.perf_counter()
print(f'It took {finish - start} second(s) to finish.')
