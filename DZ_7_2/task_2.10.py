def gen_count_days():
    count = 1
    while True:
        yield f'День {count}'
        count += 1