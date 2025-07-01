import random
import threading
import time

'''

**Задача №1**

Напишите программу, которая создает несколько потоков (5-8). 
Каждый поток должен выполнять функцию, которая выводит сообщение "Привет из потока [имя потока]!" 
и засыпает на случайное время (от 1 до 3 секунд).

'''

def output():
    print(f'Привет из потока {threading.current_thread().name}')
    time.sleep(random.randint(1,3))
    print(f'Поток {threading.current_thread().name} умер')

def main():

    for i in range(5):
        threading.Thread(target= output).start()

if __name__ == '__main__':
    main()