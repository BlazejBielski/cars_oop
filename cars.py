class Car:
    def __init__(self, brand, tank_capacity, tanked_fuel, engine_type):
        self.brand = brand
        self.tank_capacity = tank_capacity
        self.tanked_fuel = tanked_fuel
        self.engine_type = engine_type

    def __str__(self):
        return f'New car of brand {self.brand}, with tank full in ' \
               f'{(self.tanked_fuel / self.tank_capacity).__round__(3)*100}%'


auto = Car(brand="Fiat", tank_capacity=60, tanked_fuel=50, engine_type="Diesel")
print(auto)
