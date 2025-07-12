'''
Написать сопрограмму fetch_json(url), делающую GET-запрос и возвращающую распарсенный JSON через await resp.json().
Обработать возможные ошибки: если при запросе возникло исключение aiohttp.ClientError,
вернуть None и вывести в лог сообщение об ошибке.
'''

import asyncio, aiohttp
from typing import Coroutine
from aiohttp import ClientError


async def fetch_json(url) -> Coroutine:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.content_type == 'application/json':
                    return await response.json()
                else:
                    print(f"Ошибка: Ответ не содержит JSON. URL: {url}")
                    return None
    except ClientError as e:
        print(f"Ошибка при запросе: {e}")
        return None

async def main():
    list_url = ['https://httpbin.org/json',
                'https://api.github.com',
                'https://httpbin.org/status/500',
                'https://httspbin.org/status/500',
                'https://mltimes.ai/hitachi-sozdala-metavselennuyu-dlya-atomnyh-elektrostanczij/',
                'https://mltimes.ai/amazon-web-services-zapuskaet-marketplejs-ii-agentov-s-uchastiem-anthropic/',
                'https://mltimes.ai/ilon-mask-anonsiroval-integracziyu-grok-v-avtomobili-tesla-na-sleduyushhej-nedele/'
                ]

    pages = await asyncio.gather(*[fetch_json(url) for url in list_url], return_exceptions= True)
    for i,page in enumerate(pages):
        if page is not None:
            print(f"Данные из {list_url[i]}: {page}")
    return pages

if __name__ == '__main__':
    asyncio.run(main())