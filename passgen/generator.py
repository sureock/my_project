import random


def generate():
    all_symbols = []
    for i in range(97, 123):
        all_symbols.append(chr(i))
    return all_symbols


print(generate())
