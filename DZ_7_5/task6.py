"""
Студенту предлагается использовать библиотеку aiohttp для реализации асинхронной функции get_status(url),
выполняющей GET-запрос к указанному адресу и возвращающей HTTP-статус ответа.
Следует создать список из нескольких URL-адресов (например, https://example.com, https://dv.rak.org и т.п.)
и выполнить параллельные запросы с использованием async with aiohttp.ClientSession() и await.
"""

import asyncio
import aiohttp

list_url = ['https://google.com','https://yandex.ru']

async def get_status(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()

def main():
    for url in list_url:
        print(asyncio.run(get_status(url)))


if __name__ == '__main__':
    main()