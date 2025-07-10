"""
Задача заключается в создании списка из трёх сопрограмм,
каждая из которых делает задержку от 1 до 3 секунд и выводит номер своей задачи.
Все сопрограммы должны быть запущены одновременно с помощью await asyncio.gather(...).
Проследите, что выполнение начинается одновременно, а завершается по мере завершения отдельных задач.
"""
import asyncio
from typing import Coroutine


async def my_coroutine(name_task: str, delay: int) -> Coroutine:
    await asyncio.sleep(delay if isinstance(delay, int) else 0)
    print(name_task)

async def main():
    await asyncio.gather(my_coroutine('Kara1',3),
                         my_coroutine('Kara2', 1),
                         my_coroutine('Kara3', 2))

if __name__ == '__main__':
    asyncio.run(main())