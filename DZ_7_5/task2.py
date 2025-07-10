"""
Необходимо написать функцию delayed_print(text, delay), которая будет ожидать заданное количество секунд,
а затем выводить переданный текст.
Для проверки рекомендуется вызвать эту функцию с разными значениями задержки, например 2 и 4 секунды.
Ожидание должно быть реализовано через await asyncio.sleep(delay).
"""
import asyncio
from typing import Coroutine


async def delayed_print(text: str, delay: int) -> Coroutine:
    await asyncio.sleep(delay if isinstance(delay, int) else 0)
    print(text)

async def main():
    await asyncio.gather(delayed_print('Кара!', 4), delayed_print('No Kara!', 2))

if __name__ == '__main__':
    asyncio.run(main())