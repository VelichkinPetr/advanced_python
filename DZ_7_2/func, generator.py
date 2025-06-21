from random import randint

#1.1
def gen_number_multiples_5():
    num = 5
    while True:
        yield num
        num += 5

#1.2
def gen_square_numbers():
    num = 1
    while True:
        yield num ** 2
        num += 1

#1.3
def gen_numbers_not_multiples_3(N: int):
    num = 1
    while num <= N:
        if num % 3 != 0:
            yield num
        num += 1

#1.4
def gen_string_with_len(string: str, length: int):
    while len(string) >= length:
        yield string[:length:]
        string = string[1:len(string)]

#1.5
def gen_number_in_diapason_with_step(diapason: list[int], step: int):
    while diapason[0] <= diapason[1] :
        yield diapason[0]
        diapason[0] += step

#1.6
def gen_random_numbers_in_diapason(diapason: list[int]):
    while True:
        yield randint(*diapason)

#1.7
def gen_fibonacci(number: int):
    first = 0
    sec = 1
    while first < number:
        yield first
        first, sec = sec, first + sec