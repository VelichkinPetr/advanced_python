"""
Следует реализовать сопрограмму countdown(n),
которая выводит числа от n до 1 с интервалом в одну секунду между каждым выводом.
Необходимо убедиться, что задержки реализованы корректно, и программа не блокирует выполнение.
"""
import asyncio
from typing import Coroutine

async def countdown(n: int) -> Coroutine:
    for i in range(n,0,-1):
        await asyncio.sleep(1)
        print(i)

def main():
    print('Проверка начала')
    asyncio.run(countdown(5))
    print('Проверка конца')

if __name__ == '__main__':
    main()