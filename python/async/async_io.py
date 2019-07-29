# 참고>
# https://tech.ssut.me/python-3-play-with-asyncio/
# https://wikidocs.net/21046

# import asyncio
# import datetime
# import random


# @asyncio.coroutine
# def display_date(num, loop):
#     end_time = loop.time() + 50.0
#     while True:
#         print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
#         if (loop.time() + 1.0) >= end_time:
#             break
#         yield from asyncio.sleep(random.randint(0, 5))


# loop = asyncio.get_event_loop()

# asyncio.ensure_future(display_date(1, loop))
# asyncio.ensure_future(display_date(2, loop))

# loop.run_forever()

#####################################################

import aiohttp
import asyncio
import timeit

@asyncio.coroutine
def fetch(url):
    print('Start', url)
    req = yield from aiohttp.request('GET', url)
    print('Done', url)

@asyncio.coroutine
def fetch_all(urls):
    fetches = [asyncio.Task(fetch(url)) for url in urls]
    yield from asyncio.gather(*fetches)

urls = ['http://b.ssut.me', 'https://google.com', 'https://apple.com', 'https://ubit.info', 'https://github.com/ssut']

start = timeit.default_timer()
asyncio.get_event_loop().run_until_complete(fetch_all(urls))
duration = timeit.default_timer() - start