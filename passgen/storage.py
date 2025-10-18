import hashlib


def hashing_saving(password, type):
    if type == "sha256":
        hashed = hashlib.sha256(password.encode()).hexdigest()
    if type == "md5":
        hashed = hashlib.md5(password.encode()).hexdigest()
    if type == "blake2b":
        hashed = hashlib.blake2b(password.encode()).hexdigest()
    file = open('password.txt', 'w', encoding='UTF-8')
    file.write(f'Хэшированный пароль: {hashed}')
    return f'Хэшированный пароль {hashed} был сохранен в файл "password.text"'