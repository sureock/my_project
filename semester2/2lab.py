import re


# # 1
def validate_login():
    login = input('Введите логин: ')
    pattern = r'^[a-zA-Z][a-zA-Z0-9_]{3,18}[a-zA-Z0-9]$'
    if re.match(pattern, login) is not None:
        print('Допускается')
    else:
        print('Не допускается')


# 2
def search_date():
    date = input('Введите строку на поиск даты: ')
    symbols = '/.-'
    pattern = r'([0-3][0-9]|[0-3]?[0-9])[-./](1[0-2]|0?[1-9])[-./][0-9]?[0-9]?[0-9]?[0-9]?'
    search = re.search(pattern, date)
    if search is not None:
        for j in symbols:
            if j in search.group():
                result = search.group().split(j)
                break
        if int(result[0]) > 28:
            if (result[0] == '29' and int(result[1]) == 2) and int(result[2]) % 4 != 0:
                return print('Нет даты.')
            if int(result[0]) > 29 and int(result[1]) == 2:
                return print('Нет даты.')
            if int(result[0]) == 31 and str(int(result[1])) not in ['1', '3', '5', '7', '8', '10', '12']:
                return print('Нет даты.')
            if int(result[0]) > 31:
                return print('Нет даты.')
        return print(search.group())


# 3
def logs_parse():
    logs = input('Введите логи для парсинга: ')
    pattern = {
        'date': r'(\d+-\d+-\d+)',
        'time': r'(\d+:\d+:\d+)',
        'user': r'user=(.\S+)',
        'action': r'action=(.\S+)',
        'ip': r'(\d+\.\d+\.\d+\.\d)',
        }
    for key, item in pattern.items():
        pattern[key] = re.search(item, logs).group(1)
    return print(pattern)


# 4
def password_check():
    password = input('Введите пароль для проверки: ')
    patterns = [
        r'[a-zA-Z0-9!@#$%^&*]{8,}',
        r'[a-z]{1,}',
        r'[A-Z]{1,}',
        r'[0-9]{1,}',
        r'[!@#$%^&*]{1,}',
        ]
    for i in patterns:
        search = re.search(i, password)
        if search is None:
            return print(False)
    return print(True)


# 5
def email_check():
    email = input('Введите email для проверки: ')
    patterns = [
        r'[a-zA-Z][a-zA-Z0-9_-.%+-]{,319}@gmail.com',
        r'[a-zA-Z][a-zA-Z0-9_-.%+-]{,319}@yandex.ru',
        r'[a-zA-Z][a-zA-Z0-9_-.%+-]{,319}@edu.ru',
        ]
    for i in patterns:
        search = re.search(i, email)
        if search is not None:
            return print(True)
    return print(False)


# 6
def number_check():
    number = input('Введите номер телефона для парсинга: ')
    pattern = r'(\+?7|8)[\s\-\(\)]?(\d{3})[\s\-\(\)]?(\d{3})[\s\-\(\)]?(\d{2})[\s\-\(\)]?(\d{2})'
    search = re.search(pattern, number)
    if search is not None:
        return print('+7'+search.group(2)+search.group(3)+search.group(4)+search.group(5))
    return print('Не номер')


# validate_login()
# search_date()
# logs_parse()
# password_check()
# email_check()
number_check()
