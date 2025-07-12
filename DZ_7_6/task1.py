'''
Написать сопрограмму fetch_status(url), которая с помощью aiohttp.ClientSession
отправляет GET-запрос по переданному URL и возвращает HTTP-код ответа.
В отдельном корутин-скрипте сформировать список из трёх URL (например, , , ) и последовательно вывести коды ответов.
'''
import asyncio, aiohttp
from typing import Coroutine


async def fetch_status(url) -> Coroutine:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response.status

async def main():
    list_url = ['https://example.com/',
                'https://httpbin.org/status/404',
                'https://httpbin.org/status/500']

    status = await asyncio.gather(*[fetch_status(url) for url in list_url])

    for i,url in enumerate(list_url):
        print(f'URL >> {url}, STATUS >> {status[i]}')

    return status

if __name__ == '__main__':
    asyncio.run(main())