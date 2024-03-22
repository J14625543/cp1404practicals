class Car:

    def __init__(self, fuel=0):
        self.fuel = fuel
        self._odometer = 0

    def add_fuel(self, amount):
        self.fuel += amount

    def drive(self, distance):
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance