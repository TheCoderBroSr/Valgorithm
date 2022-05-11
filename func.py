import random

def rand_list(length, range):
    data = []
    start, end = range

    while len(data) != length:
        data.append(random.randint(start, end))

    return data