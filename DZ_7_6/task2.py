'''
Написать сопрограмму fetch_text(url), выполняющую GET-запрос и асинхронно читающую тело ответа строкой через await resp.text().
Создать список из пяти разных страниц (новостных или документации) и запустить их параллельно через asyncio.gather.
В конце вывести длину текста каждой страницы.
'''

import asyncio, aiohttp
from typing import Coroutine

async def fetch_text(url) -> Coroutine:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    list_url = ['https://mltimes.ai/hitachi-sozdala-metavselennuyu-dlya-atomnyh-elektrostanczij/',
                'https://mltimes.ai/amazon-web-services-zapuskaet-marketplejs-ii-agentov-s-uchastiem-anthropic/',
                'https://mltimes.ai/ilon-mask-anonsiroval-integracziyu-grok-v-avtomobili-tesla-na-sleduyushhej-nedele/']
    page = await asyncio.gather(*[fetch_text(url) for url in list_url])
    len_page = [len(elem) for elem in page]
    for i,url in enumerate(list_url):
        print(f'URL >> {url}, LEN PAGE >> {len_page[i]}')


if __name__ == '__main__':
    asyncio.run(main())