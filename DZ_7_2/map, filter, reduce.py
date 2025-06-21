from functools import reduce
import math

#1
input = ["1", "20", "300"]
output = list(map(lambda elem: int(elem), input))
print('№1', input,' => ', output)

#2
input = [1, 2, 3, 4, 5, 6]
output = list(filter(lambda elem: elem % 2 == 0, input))
print('№2', input,' => ', output)

#3
input = [1, 2, 3, 4]
output = list(map(lambda elem: elem ** 2, input))
print('№3', input,' => ', output)

#4
input = ["cat", "elephant", "dog", "tiger"]
output = list(filter(lambda elem: len(elem) > 3, input))
print('№4', input,' => ', output)

#5
input = [1, 2, 3, 4]
output = reduce(lambda cache, s_elem : cache * s_elem, input)
print('№5', input,' => ', output)

#6
input = ["hello", "world", "Python"]
output = list(map(lambda elem: len(elem), input))
print('№6', input,' => ', output)

#7
input = ["apple", "banana", "pear", "strawberry"]
output = max(map(lambda elem: len(elem), input))
print('№7', input,' => ', output)

#8
input = ["hello", "world"]
output = list(map(lambda elem: elem.upper(), input))
print('№8', input,' => ', output)

#9
input = ["1", "2", "3", "4"]
output = list(map(lambda elem: int(elem) ** 2,
                  filter( lambda elem: int(elem) % 2 ==0, input)))
print('№9', input,' => ', output)

#10
input = [-2, 3, -4, 5, 6]
output = reduce(lambda f_elem, s_elem: f_elem * s_elem,
                filter(lambda elem: elem > 0 , input))
print('№10', input,' => ', output)

#11
input = ["apple", "banana", "orange", "grape"]
vowels = "aeiou"
output = list(map(lambda elem: len(elem),
                  filter(lambda elem: elem[0].lower() in vowels , input)))
print('№11', input,' => ', output)

#12
input = ["racecar", "hello", "level", "world"]
output = list(filter(lambda elem: elem == elem[::-1], input))
print('№12', input,' => ', output)

#13
input = [2, 3, 4, 5, 6]
output = reduce(lambda f_elem, s_elem: f_elem * s_elem,
                map(lambda elem: math.factorial(elem),
                         filter(lambda elem: elem % 2 == 0 , input) ))
print('№13', input,' => ', output)

#14
input = ["hello", "world", "Python", "is", "great"]
output = reduce(lambda f_elem, elem: f_elem.upper() + " " + elem.upper(),
                filter(lambda elem: len(elem) % 2 == 0 , input))
print('№14', input,' => ', output)

