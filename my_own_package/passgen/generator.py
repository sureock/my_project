"""Модуль генерации пароля
"""
import random


def get_generated_password(length: int, s: bool, d: bool, u: bool, hash: str):
    """Генерирует пароль, используя кодировку юникод,
       сохраняя метод хэширования

    Args:
        length (int): длина генерируемого пароля
        s (bool): флаг, использования спец. символов
        d (bool): флаг, использования цифр
        u (bool): флаг, использования заглавных букв
        hash (str): метод хэширования
    Returns:
        tuple: сгенерированный пароль, метод хэширования
    """
    if hash is None:
        hash = "sha256"
    all_symbols = []
    result = []
    for i in range(97, 123):
        all_symbols.append(chr(i))
    if s:
        symbols = ['!', '@', '#', '$', '%', '^', '&',
                   '*', '(', ')', '—', '_', '+', '=',
                   ';', ':', ',', './', '?', '\\', '|',
                   '`', '~', '[', ']', '{', '}']
        for i in symbols:
            all_symbols.append(i)
    if d:
        for i in range(48, 58):
            all_symbols.append(str(chr(i)))
    if u:
        for i in range(65, 91):
            all_symbols.append(chr(i))
    for i in range(length):
        result.append(random.choice(all_symbols))
    finall_result = ''.join(result)
    return (finall_result, hash)
