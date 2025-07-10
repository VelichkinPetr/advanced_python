"""
Задача заключается в написании сопрограммы fetch_data(index),
которая делает паузу на случайное количество секунд от 1 до 5 и возвращает сообщение "Данные {index} получены".
С помощью asyncio.gather необходимо запустить 5 таких задач одновременно.
Для генерации случайных задержек требуется использовать модуль random.
"""
import asyncio
import random
from typing import Coroutine

async def fetch_data(index) -> Coroutine:
    await asyncio.sleep(random.randint(1,5))
    print(f'Данные {index} получены')

async def main():
    await asyncio.gather(*[fetch_data(i) for i in range(5)])

if __name__ == '__main__':
    asyncio.run(main())