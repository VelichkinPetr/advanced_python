import threading
import time

from DZ_7_2.sort import times

'''

Задача №5

Создайте программу, где несколько потоков добавляют элементы в общий список.
Используйте мьютекс для защиты доступа к списку. Каждый поток должен добавлять 5 случайных чисел.
Запустите не менее 3 потоков, реализуйте механизм запуска любым из двух основных способов: передача функции или ООП формат.

'''
mutex = threading.Lock()
list_for_all = []

def append_in_list(elem):

    print(f' Поток {threading.current_thread().name} захват потока')
    mutex.acquire()

    print(f' добавил элемент в список ')
    list_for_all.append(elem)

    print(f' Поток {threading.current_thread().name} освободил поток')
    mutex.release()


def main():

    for i in range(3):
        threading.Thread(target= append_in_list, args=(i,)).start()

if __name__ == '__main__':
    main()