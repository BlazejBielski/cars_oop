class Car:
    def __init__(self, brand, tank_capacity, tanked_fuel, engine_type):
        self.liter = 0
        self.brand = brand
        self.tank_capacity = tank_capacity
        self.tanked_fuel = tanked_fuel
        self._engine_type = engine_type
        print(f'New car of brand {self.brand}, with tank full in '
              f'{(self.tanked_fuel / self.tank_capacity).__round__(3) * 100}%')

    # @property
    # def engine_type(self):
    #     return self._engine_type
    #
    # @engine_type.setter
    # def engine_type(self, engine):
    #     pass

    def fill_tank(self, liter=0):
        self.liter = liter
        if not self.liter:
            self.liter = self.tank_capacity
            print(f'Tanked {self.liter}')
        elif self.liter > self.tank_capacity:
            raise ValueError(f'You can not fill on {self.liter} because tank have {self.tank_capacity} liter capacity')
        else:
            print(f'Tanked {self.liter}')

    def __str__(self):
        return f'New car of brand {self.brand}, with tank full in ' \
               f'{(self.tanked_fuel / self.tank_capacity).__round__(3)*100}%'


auto = Car(brand="Fiat", tank_capacity=60, tanked_fuel=50, engine_type="Diesel")
# print(auto)
auto.fill_tank(6)
print(auto)
