class Car():
    def __init__(self, id, color, make, gas, has_accident):
        self.id = id
        self.color = color
        self.make = make
        self.gas = gas
        self.has_accident = has_accident

    # Accessor function that returns how much gas is left
    def get_gas(self):
        return self.gas

    # uses one gallon of gas to drive the car
    def drive(self):
        if self.gas <= 0:
            print("out of gas")
        else:
            self.gas -= 1

    # Accident occurs so indicates that both cars had an accident
    def crash(self, other):
        self.has_accident = True
        other.has_accident = True

    # string representation of a car
    def __str__(self):
        return self.id + ' ' + self.color + ' ' + self.make + ' ' + str(self.gas)

def main():
    my_car = Car('abc123', 'blue', 'sedan', 6, False)

    print("Example of driving car: ")
    for i in range(0,7):
        my_car.drive()
        print(my_car.get_gas())
    print()

    print("Example of string representation of object:")
    print(my_car)
    print(my_car.__str__())
    print()

main()
