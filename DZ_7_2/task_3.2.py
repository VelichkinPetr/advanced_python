def gen_string_with_len(string: str, length: int):
    unic_str = set()
    while len(string) > 0:
        for i in range(1, length+1):
            if string[0:i] not in unic_str:
                unic_str.add(string[0:i])
                yield string[0:i]
        string = string[1:len(string)]