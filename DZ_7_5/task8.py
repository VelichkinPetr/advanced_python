'''
Необходимо создать асинхронный цикл, который каждые 1 секунду проверяет выполнение некоего условия —
например, делится ли текущее количество секунд на 5.
Если условие выполняется, программа должна выводить соответствующее сообщение.
Цикл не должен работать более 10 секунд.
Время можно отслеживать через asyncio.get_event_loop().time() или time.time().
'''

import asyncio

async def check_second_even_5():
    for i in range(10):
        second = round(asyncio.get_event_loop().time())
        if second % 5 == 0:
             print(f'Текущее количество {second} секунд делиться на 5')
        else:
            print(f'Текущее количество {second} секунд НЕ делиться на 5')
        await asyncio.sleep(1)

if __name__ == '__main__':
    asyncio.run(check_second_even_5())