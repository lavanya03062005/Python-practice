"""
Create classes Vehicle → Car → ElectricCar.
Add attributes and methods at each level.
Show how ElectricCar can access methods from Vehicle.
"""

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        return f"{self.make} {self.model} engine started."
class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def open_doors(self):
        return f"{self.num_doors} doors opened."
class ElectricCar(Car):
    def __init__(self, make, model, num_doors, battery_capacity):
        super().__init__(make, model, num_doors)
        self.battery_capacity = battery_capacity

    def charge_battery(self):
        return f"Charging battery with capacity {self.battery_capacity} kWh."
electric_car = ElectricCar("Tesla", "Model S", 4, 100)
print(electric_car.start_engine())
print(electric_car.open_doors())
print(electric_car.charge_battery())
