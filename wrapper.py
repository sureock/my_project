def logger(func):
    def wrapper(a, b=None, *args, **kwargs):
        print(f'Вызов функции {func.__name__} с'
              f' аргументами {a} и {b}')
        try:
            if b is None:
                result = func(a, *args, **kwargs)
            else:
                result = func(a, b, *args, **kwargs)
            return f'Функция {func.__name__} вернула результат: {result}'
        except Exception as e:
            print(f'Произошла ошибка {Exception} - {e}')
    return wrapper


@logger
def add(a, b):
    return a + b


@logger
def divide(a, b):
    return a / b


@logger
def greet(name):
    return f'Привет {name}!'


print(add(2, 3))
print(divide(6, 5))
print(greet('Alex'))
