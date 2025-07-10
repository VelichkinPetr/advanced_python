'''
Требуется реализовать функцию parallel_sum, принимающую список чисел.
Для каждого элемента списка необходимо вызвать сопрограмму delayed_square(x),
возвращающую квадрат числа с задержкой. Все задачи должны быть запущены одновременно,
а после их выполнения — рассчитана сумма результатов.
Для параллельного выполнения следует использовать asyncio.gather.
'''
import asyncio
from typing import Coroutine


async def parallel_sum(list_int: list[int]) -> int:
    return sum(await (asyncio.gather(*[delayed_square(x) for x in list_int])))

async def delayed_square(x:int) -> Coroutine:
    await asyncio.sleep(1)
    return x**2

if __name__ == '__main__':
    total_sum = asyncio.run(parallel_sum(list_int=[1,2,3,4]))
    print(total_sum)