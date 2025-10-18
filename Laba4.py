class Transport:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def __str__(self):
        return f'Transport: {self.brand}, Speed: {self.speed}'

    def move(self):
        return f'\rTransport is moving at {self.speed} km/h'


class Car(Transport):
    def __init__(self, brand, speed, seats):
        super().__init__(brand, speed)
        self.seats = seats

    def __str__(self):
        return (f'Transport: {self.brand}, Speed: {self.speed},'
                f' Seats: {self.seats}')

    def __len__(self):
        return self.seats

    def __eq__(self, other):
        return self.speed == other.speed

    def __add__(self, other):
        return f'Суммарная скорость машин: {self.speed + other.speed}'

    def honk(self):
        return '\nBeep-Beep!'

    def move(self):
        return f'\nCar {self.brand} is driving at {self.speed} km/h'


class Bike(Transport):
    def __init__(self, brand, speed, type):
        super().__init__(brand, speed)
        self.type = type

    def __str__(self):
        return (f'\nTransport: {self.brand}, Speed: {self.speed},'
                f' Type: {self.type}')

    def move(self):
        return f'\nBike {self.brand} is cycling at {self.speed} km/h'


transport = Transport('ford', 60)
car1 = Car('mustang', 70, 6)
car2 = Car('f-1', 120, 1)
bike = Bike('T-34', 90, 'mountain')
print(car1 + bike)

for i in [transport, car1, car2, bike]:
    print(i.move())
