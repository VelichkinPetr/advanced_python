from typing import Generator

#1.1
def gen_reverse_in_diapason(start: int, end: int) -> Generator:
    while start >= end:
        yield start
        start -= 1

#1.2
def gen_fibonacci_multiples_5() -> Generator:
    first = 0
    second = 1
    while True:
        if first % 5 == 0 and first != 0:
            yield first
        first, second = second, first+second

#1.3
def gen_factorial() -> Generator:
    start = 1
    step = 2
    while True:
        yield start
        start *= step
        step += 1
#1.4
def gen_alphabet() -> Generator:
    start = 65
    while start <= 90:
        yield chr(start)
        if start == 90:
            start = 65
        start += 1
#1.5
def gen_unic_word(string: str) -> Generator:

    set_string = list(string.split(' '))
    unic_elements = []
    index = 0
    while len(set_string) - index != 0:
        if set_string[index] not in unic_elements:
            yield set_string[index]
            unic_elements.append(set_string[index])
        index +=1
#1.6
def gen_word_on_len(string: str, length: int) -> Generator:

    sort_list = sorted(string.split(' '), key = lambda x: len(x), reverse= True)
    for word in sort_list:
        if len(word) > length:
            yield word
#1.7
def gen_unic_symbols(string: str, n: int) -> Generator:

    from itertools import permutations
    for i in range(1,n+1):
        for p in permutations(string, i):
            elem = ''.join(p)
            yield elem

#1.8
def gen_vowels_symbols(string: str) -> Generator:

    key = ['a', 'e', 'i', 'o', 'u']
    unic = []
    for symbol in string:
        if symbol.lower() in key and symbol.lower() not in unic:
            unic.append(symbol.lower())
            yield symbol
