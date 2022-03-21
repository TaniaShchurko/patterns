class MotorCycle:
    def __init__(self):
        self.name = "MotorCycle"

    def TwoWheeler(self):
        return "TwoWheeler"

class Truck:
    def __init__(self):
        self.name = "Truck"

    def EightWheeler(self):
        return "EightWheeler"

class Car:
    def __init__(self):
        self.name = "Car"

    def FourWheeler(self):
        return "FourWheeler"

class Adapter:
    def __init__(self, obj, **adapted_methods):
        self.name = obj.name
        self.wheels = adapted_methods['wheels']


objects = []
motorCycle = MotorCycle()
truck = Truck()
car = Car()
objects.append(Adapter(motorCycle, wheels = motorCycle.TwoWheeler))
objects.append(Adapter(truck, wheels = truck.EightWheeler))
objects.append(Adapter(car, wheels = car.FourWheeler))
for item in objects:
    print(f"A {item.name} is a {item.wheels()} vehicle")