import random
import time
from threading import Thread

'''

 **Задача №2**

Создайте класс `MyThread`, который наследуется от `threading.Thread`. 
В методе `run` этот класс должен выводить "Поток [имя потока] работает" 
и засыпать на случайное время (можно передать через конструктор). 
Запустите от 5 до 10 потоков.

'''
class MyThread(Thread):

    def __init__(self, id: int or str):
        super().__init__()
        self.id = id
        self.time_sleep = random.randint(1, 3)

    def run(self):
        print(f'Привет {self.name} работает')
        time.sleep(self.time_sleep)
        print(f'Поток {self.name} умер')

def main():

    for i in range(5):
        MyThread(i).start()

if __name__ == '__main__':
    main()