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
