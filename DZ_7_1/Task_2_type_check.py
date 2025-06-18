def type_check(*types):

    def decorator(func):

        def wrapper(*args, **kwargs):

            for i in range(len(args)):
                if not isinstance(args[i],types[i]):
                    raise TypeError(f'Неверный тип аргумента \'{func.__code__.co_varnames[i]}\'. Ожидался <class \'int\'>, получен <class \'str\'>')

            return func(*args, **kwargs)

        return wrapper

    return decorator

@type_check(int, int)
def add(a, b):
    return a + b

print(add(2, 3))     # 5
print(add(44, 3))     # 47
print(add(2, '3'))   # TypeError: Неверный тип аргумента  'b'. Ожидался <class 'int'>, получен <class 'str'>