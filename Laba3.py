import decimal
import fractions
import datetime

task = input("Введите номер задания или 'окончить выполнение': ")
while task != "окончить выполнение":
    if task == '1':
        a = [x**2 for x in range(1, 11)]
        print(a)
    if task == '2':
        b = [x for x in range(1, 20) if x % 2 == 0]
        print(b)
    if task == '3':
        words = ['python', 'Java', 'c++', 'Rust', 'go']
        c = [x.upper() for x in words if len(x) > 3]
        print(c)

    if task == '4':
        class Countdown:
            def __init__(self, max_value):
                self.value = max_value+1

            def __iter__(self):
                return self

            def __next__(self):
                if self.value == 1:
                    raise StopIteration
                self.value -= 1
                return self.value

        for i in Countdown(5):
            print(i)

    if task == '5':
        class Fibonacci:
            def __init__(self, number):
                self.value = 0
                self.fibonacci = [0] * number
                self.fibonacci[1] = 1
                for i in range(2, number):
                    self.fibonacci[i] = self.fibonacci[i-1]+self.fibonacci[i-2]

            def __iter__(self):
                return self

            def __next__(self):
                if self.value == len(self.fibonacci):
                    raise StopIteration
                self.value += 1
                return self.fibonacci[self.value-1]

        for i in Fibonacci(5):
            print(i)

    if task == '6':
        decimal.getcontext().prec = 3

        class IncomeCalc:
            def __init__(self, start, perc, time):
                self.deposit = decimal.Decimal(start)
                self.percent = decimal.Decimal(perc)
                self.term = decimal.Decimal(time)
                # self.deposit = int(start)
                # self.percent = int(perc)
                # self.term = int(time)

            def calc(self):
                return self.deposit * ((1+(self.percent/(12*100)))**(12*self.term))

        a = input("Введите начальный вклад, процент (в виде дроби) и срок через пробел: ").split(' ')
        a[1] = a[1].replace("%", "")
        n = f'{IncomeCalc(a[0], a[1], a[2]).calc():f}'
        print(f' Итоговая сумма вклада: {n}\n Общая прибыль: {int(n)-int(a[0])}')

    if task == '7':
        first = fractions.Fraction('3/4')
        second = fractions.Fraction('5/6')
        print(f'Сложение: {first+second}, вычитание: {first-second}, умножение: {first*second}, деление: {first/second}')
    
    if task == '8':
        all_now = datetime.datetime.now()
        print(f'Текущее дата и время {datetime.datetime.strftime(all_now, "%Y-%m-%d %H:%M:%S")}, текущая дата {datetime.datetime.strftime(all_now, "%Y-%m-%d")}, текущее время {datetime.datetime.strftime(all_now, "%H:%M:%S")}')

    if task == '9':
        my_date = datetime.date(2005, 12, 25)
        now_date = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")
        print(now_date, my_date)
        delta = datetime.timedelta(now_date-my_date)
        print(f'Разница в днях {delta.days}')

    task = input("Введите номер задания или 'окончить выполнение': ")
