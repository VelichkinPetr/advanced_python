import threading
from functools import reduce
'''

Задача №6.

Создать программу, которая делит массив чисел на несколько частей,
передает эти части в разные потоки для вычисления частичных сумм,
а затем объединяет результаты, чтобы получить общую сумму.

'''

massiv = [i for i in range(1, 101)]
partial_sums = []

def calculate_sum(start, end, index):
    partial_sums.insert(index, reduce(lambda x,y: x+y, massiv[start:end]))

def main():
    step = len(massiv) // 5

    for i in range(5):
        thread = threading.Thread(target=calculate_sum, args=(i*step, (i+1)*step,i))
        thread.start()
        thread.join()

    return partial_sums

if __name__ == '__main__':
    print(temp:=main(), ' = ', sum(temp) )
