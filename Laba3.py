import decimal


a = [x**2 for x in range(1, 11)]
print(a)

b = [x for x in range(1, 20) if x % 2 == 0]
print(b)

words = ['python', 'Java', 'c++', 'Rust', 'go']
c = [x.upper() for x in words if len(x) > 3]
print(c)


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

getcontext().prec = 10

class IncomeCalc:
    def __init__(self, start, perc, time):
        self.deposit = decimal.Decimal(start)
        self.percent = decimal.Decimal(perc)
        self.term = decimal.Decimal(time)

    def calc(self):
        return decimal.Decimal(self.deposit *
                               ((1+(self.percent/12*100))**(12*self.term)))


a = input("Введите начальный вклад, процент (в виде дроби) и срок через пробел: ").split(' ')
a[1] = a[1].replace("%", "")
print(IncomeCalc(a[0], f'0.{a[1]}', a[2]).calc)
