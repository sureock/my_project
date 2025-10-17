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
        return super().__str__()+f' Seats: {self.seats}'

    def honk():
        return 'Beep-Beep!'


car = Transport('mustang', '70').Car(6)
print(car, car.move())
