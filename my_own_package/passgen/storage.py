import hashlib


def save_hash_in_file(password: str, type: str = 'sha256',
                      path: str = 'password.txt'):
    if type == "sha256":
        hashed = hashlib.sha256(password.encode()).hexdigest()
    if type == "md5":
        hashed = hashlib.md5(password.encode()).hexdigest()
    if type == "blake2b":
        hashed = hashlib.blake2b(password.encode()).hexdigest()
    if path is None:
        path = "password.txt"
    file = open(path, 'w', encoding='UTF-8')
    file.write(f'Хэшированный пароль: {hashed}')
    return f'Хэшированный пароль {hashed} был сохранен в файл {path}'
