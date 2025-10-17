def logger(func):
    def wrapper(a, b=None):
        print(f'Вызов функции {func.__name__} с'
              f' аргументами {a} и {b}')
        try:
            if b is None:
                result = func(a)
            else:
                result = func(a, b)
            return f'Функция {func.__name__} вернула результат: {result}'
        except Exception as e:
            return f'Произошла ошибка {Exception} - {e}'
    return wrapper


@logger
def add(a, b):
    return a + b


@logger
def divide(a, b):
    return a / b


@logger
def greet(name):
    return f'Привет, {name}!'


print(add(2, 3))
print(divide(6, 0))
print(greet('Alex'))


def require_role(allowed_roles):
    def func_decorator(func):
        def wrapper(name):
            if name not in allowed_roles:
                return f'Доступ запрещен пользователю {name}'
            else:
                return func(name)
        return wrapper

    return func_decorator


@require_role(["admin"])
def delete_database(user):
    return f'База данных удалена пользователем {user}'


print(delete_database('admin'))
