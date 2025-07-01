import time
from threading import Thread


'''

Задача №4

Напишите программу, которая создает несколько потоков, каждому из которых передаются параметры. 
Пусть каждый поток принимает имя и задержку, выводит "Поток [имя] начался", 
засыпает на заданное время, а затем выводит "Поток [имя] завершен". 
Реализуйте механизм потоков любым из двух основных способов: передача функции или ООП формат.

'''

class MyThread(Thread):

    def __init__(self, name: int or str, delay: int or float):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        print(f'Поток {self.name} начался')
        time.sleep(self.delay)
        print(f'Поток {self.name} завершен')

def main():
    for i in range(5):
        MyThread(i,1).start()

if __name__ == '__main__':
    main()