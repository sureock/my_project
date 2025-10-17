class Transport:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def __str__(self):
        return f' Transport: {self.brand}, Speed: {self.speed}\n'

    def move(self):
        return f'Transport is moving at {self.speed} km/h'


car = Transport('mustang', '70')
print(car, car.move())
