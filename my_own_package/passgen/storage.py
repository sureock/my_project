"""Модуль хэширования и сохранения пароля
"""
import unittest
import hashlib


def save_hash_in_file(password: str, type: str,
                      path: str):
    """Хэширует текст (и сохраняет его в файле)

    Args:
        password (str): пароль
        type (str): тип хэширования
        path (str): путь сохранения пароля
    Returns:
        str: Строка с информированием о хэшировании (и сохранении)
    """
    if type == "md5":
        hashed = hashlib.md5(password.encode()).hexdigest()
    if type == "blake2b":
        hashed = hashlib.blake2b(password.encode()).hexdigest()
    else:
        hashed = hashlib.sha256(password.encode()).hexdigest()
    if path is None:
        return f'Хэшированный пароль {hashed}'
    file = open(path, 'w', encoding='UTF-8')
    file.write(f'Хэшированный пароль: {hashed}')
    return f'Хэшированный пароль {hashed} был сохранен в файл {path}'
