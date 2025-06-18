def trace(func):

    def wrapper(*args, **kwargs):

        print(f'Вход в функцию \'{func.__name__}\' с аргументами {args},'+'{}')
        r = func(*args,**kwargs)
        print(f'Выход из функции \'{func.__name__}\' с результатом {r}')

        return r

    return wrapper

@trace
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factorial(3)
# Вывод:
# --> Вход в функцию 'factorial' с аргументами (3,), {}
#     --> Вход в функцию 'factorial' с аргументами (2,), {}
#         --> Вход в функцию 'factorial' с аргументами (1,), {}
#             --> Вход в функцию 'factorial' с аргументами (0,), {}
#             <-- Выход из функции 'factorial' с результатом 1
#         <-- Выход из функции 'factorial' с результатом 1
#     <-- Выход из функции 'factorial' с результатом 2
# <-- Выход из функции 'factorial' с результатом 6
