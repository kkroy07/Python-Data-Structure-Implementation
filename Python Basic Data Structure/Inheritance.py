class Vehicle():
    def general_usage(self):
        print("General usage:transportation")

class car(Vehicle):
    def __init__(self):
        print("I am a car")
        self.wheels=4
        self.has_roof=False
    def specific_usage(self):
        self.general_usage()
        print("To enjoy vacation with family")

class motor_cycle(Vehicle):
    def __init__(self):
        print("I am a motor cycle")
        self.wheels=2
        self.has_roof=True
    def specific_usage(self):
        self.general_usage()
        print("To enjoy riding on a trip alone or with two person")

c=car()
c.specific_usage()
print(c.wheels)
print(c.has_roof)
m=motor_cycle()
m.specific_usage()
print(m.wheels)
print(m.has_roof)
