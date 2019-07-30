# 비동기를 사용하는 방법 중 하나는 이벤트 루프를 사용하는 것이다. 
# 이벤트 루프란? 이벤트/잡 을 관리하는 큐가 있을때 큐에서 잡을 꺼내서 실행시켜주는 것을 의미한다. 
# 이때, 이 잡들을 코루틴이라고 부른다. 
# 코루틴이란, 비동기식 프로그래밍을 하기 위해서는 한번 주면 발을 때까지 기다리기만 하는 함수를 발전시켜 멀티태스킹이 가능하게 만들어진 함수다.


# python 3.6.5
# 참고>
# https://tech.ssut.me/python-3-play-with-asyncio/
# https://wikidocs.net/21046

import requests
import asyncio
from bs4 import BeautifulSoup
import time
s = time.time()
results = []

#----------------------------------------------
async def getpage(url):
    req = await loop.run_in_executor(None, requests.get, url)
    html = req.text
    soup = await loop.run_in_executor(None, BeautifulSoup, html, 'lxml')
    return soup

#---------------------------------------------- 
async def main():
    urls = ["https://wp.me/p9x2W1-x",
            "https://wp.me/p9x2W1-w",
            "https://wp.me/p9x2W1-t",
            "https://wp.me/p9x2W1-q",
            "https://wp.me/p9x2W1-p",
            "https://wp.me/p9x2W1-j",
            "https://wp.me/p9x2W1-h"]

    fts = [asyncio.ensure_future(getpage(u)) for u in urls]
    r = await asyncio.gather(*fts)
    global results
    results = r

#----------------------------------------------
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close
e = time.time()

print("{0:.2f}초 걸렸습니다".format(e - s))

#결과
#0.88초 걸렸습니다


# python 3.7.3
import asyncio
import datetime

async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

asyncio.run(display_date())