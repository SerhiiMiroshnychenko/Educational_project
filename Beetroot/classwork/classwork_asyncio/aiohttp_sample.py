import aiohttp


session = aiohttp.ClientSession()


async def future_example(session):
    resp = await session.get('https://www.google.com/')
    data = await resp.text()
    return resp


data = await future_example(session)

data
