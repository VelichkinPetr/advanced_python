import threading


'''

Задача №3

Напишите программу, где несколько потоков увеличивают общий счетчик на 1. 
Каждое увеличение должно быть выполнено в отдельном потоке, и результат счетчика должен выводиться после каждого инкремента. 
Запустите не менее 50 потоков.

'''
num = 0

def add_one():
    global num
    num += 1
    print(num)

def main():

    for i in range(50):
        threading.Thread(target= add_one).start()

if __name__ == '__main__':
    main()