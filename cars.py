import numpy as np


class Car:
    def __init__(self, brand, tank_capacity, tanked_fuel, engine_type):
        self.brand = brand
        self.tank_capacity = tank_capacity
        self.tanked_fuel = tanked_fuel
        self._engine_type = engine_type
        engine_types = ['Diesel', 'Gasoline']
        if engine_type not in engine_types:
            raise ValueError(f'Invalid engine type. Expected one of types: {engine_types[0]} or {engine_types[1]}')

        print(f'New car of brand {self.brand}, with tank full in '
              f'{(self.tanked_fuel / self.tank_capacity).__round__(3) * 100}%')

    def fill_tank(self, liters=None):

        if self._engine_type == 'Diesel':
            raise EnvironmentError(f'ON fuel not available,because of environmental restrictions. '
                                   f'Change engine as soon, as possible')

        else:

            if not liters:
                liters = self.tank_capacity
                print(f'Tanked {liters}')
                self.tanked_fuel = liters
            elif liters < self.tank_capacity < liters + self.tanked_fuel:
                raise ValueError(f'You cannot refuel more than tank capacity: {self.tank_capacity}')
            else:
                self.tanked_fuel = liters + self.tanked_fuel
                print(f'Tanked {liters}')

    def empty_tank(self, limit=None):
        if limit in np.arange(0, 1.1, 0.1):
            self.tanked_fuel = self.tank_capacity * limit
            print(f'Empty {self.tanked_fuel} liters')
            self.tanked_fuel = self.tank_capacity - self.tanked_fuel
        else:
            raise ValueError(f'You must enter a value in the range 0-1 in steps of 0.1')

    def __str__(self):
        return f'Car of brand {self.brand}, with tank full in ' \
               f'{(self.tanked_fuel / self.tank_capacity).__round__(3)*100}%'


auto = Car(brand="Fiat", tank_capacity=60, tanked_fuel=30, engine_type="Gasoline")
auto.fill_tank(10)
auto.fill_tank(19)
print(auto)
auto.empty_tank_prototype()
print(auto)
auto.fill_tank()
print(auto)
auto.empty_tank_prototype(50)
print(auto)
auto.fill_tank()
auto.empty_tank(1)
print(auto)

