def uppercase_result(func):

    def wrapper(*args, **kwargs):

        r = func(*args,**kwargs)
        if isinstance(r, str):
            r = r.upper()

        return r

    return wrapper



@uppercase_result
def get_greeting(name):
    return f"Привет, {name}"

print(get_greeting("Алексей"))  # Вывод: ПРИВЕТ, АЛЕКСЕЙ

@uppercase_result
def add_numbers(a, b):
    return a + b

print(add_numbers(2, 3))  # Вывод: 5