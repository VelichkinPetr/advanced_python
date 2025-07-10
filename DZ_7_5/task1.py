"""
Требуется реализовать сопрограмму say_hello,
которая с использованием await asyncio.sleep(1) делает паузу на одну секунду, после чего выводит сообщение "Привет!".
Сопрограмма должна быть запущена через asyncio.run() в основном блоке программы.
"""
import asyncio
from typing import Coroutine


async def say_hello() -> Coroutine:
    await asyncio.sleep(1)
    print('Привет!')

def main():
    asyncio.run(say_hello())

if __name__ == '__main__':
    main()