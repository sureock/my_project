import re


# # 1
def validate_login(login):
    login = input('Введите логин: ')
    pattern = r'^[a-zA-Z0-9_]{4,19}[a-zA-Z0-9]$'
    if re.match(pattern, login) is not None:
        print('Допускается')
    else:
        print('Не допускается')


# 2
def search_date():
    date = input('Введите строку на поиск даты: ')
    symbols = '/.-'
    patterns = [
        r'([0-3][0-9]|[0-3]?[0-9])\.(1[0-2]|0?[1-9])\.[0-2]?[0-9]?[0-9]?[0-9]?',
        r'([0-3][0-9]|[0-3]?[0-9])\-(1[0-2]|0?[1-9])\-[0-2]?[0-9]?[0-9]?[0-9]?',
        r'([0-3][0-9]|[0-3]?[0-9])\/(1[0-2]|0?[1-9])\/[0-2]?[0-9]?[0-9]?[0-9]?',
    ]
    symbols
    for i in patterns:
        search = re.search(i, date)
        # result = search.group()
        if search is not None:
            for j in symbols:
                if j in search.group():
                    result = search.group().split(j)
                    break
            if int(result[0]) > 28:
                if (result[0] == '29' and int(result[1]) == 2) and int(result[2]) % 4 != 0:
                    break
                if int(result[0]) > 29 and int(result[1]) == 2:
                    break
                if int(result[0]) == 31 and str(int(result[1])) not in ['1', '3', '5', '7', '8', '10', '12']:
                    break
                if int(result[0]) > 31:
                    break
            print(search.group())
    print('Нет даты.')


# 3
def logs_parse():
    logs = input('Введите логи для парсинга: ')
    pattern = r'(\d+-\d+-\d+) (\d+:\d+:\d+) INFO user=(.+) action=(.+) ip=(\d+.\d+.\d+.\d)'
    search = re.search(pattern, logs)
    if search is not None:
        print("{\n\t'date': '"+search.group(1)+"'\n\t'time': '"+search.group(2)+"'\n\t'user': '"+search.group(3)+"'\n\t'action': '"+search.group(4)+"'\n\t'ip': '"+search.group(5)+"'\n}")


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
        r'gmail.com',
        r'yandex.ru',
        r'edu.ru',
        ]
    for i in patterns:
        search = re.search(i, email)
        if search is not None:
            return print(True)
    return print(False)


# 6
def number_check():
    number = input('Введите номер телефона для парсинга: ')
    pattern = r'\+?[0-9]{1}[ -\(\)]*\d{3}[ -\(\)]*\d{3}[ -\(\)]*\d{2}[ -\(\)]*\d{2}'
    symbols = ' -()'
    search = re.search(pattern, number)
    if search is not None:
        result = search.group()
        for i in symbols:
            result = result.replace(i, '')
        return print(result)
    return print('Не номер')


validate_login()
search_date()
logs_parse()
password_check()
email_check()
number_check()
