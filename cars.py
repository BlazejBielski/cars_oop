class Car:
    def __init__(self, brand, tank_capacity, tanked_fuel, engine_type):
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

    def fill_tank(self, liters=None):

        if self._engine_type == 'Diesel':
            raise EnvironmentError(f'ON fuel not available,because of environmental restrictions. '
                                   f'Change engine as soon, as possible')

        else:

            if not liters:
                liters = self.tank_capacity
                print(f'Tanked {liters}')
            elif liters > self.tank_capacity:
                raise ValueError(f'You can not fill on {liters} because tank have {self.tank_capacity} liter capacity')
            else:
                print(f'Tanked {liters}')

    def __str__(self):
        return f'New car of brand {self.brand}, with tank full in ' \
               f'{(self.tanked_fuel / self.tank_capacity).__round__(3)*100}%'


auto = Car(brand="Fiat", tank_capacity=60, tanked_fuel=50, engine_type="Gasoline")
auto.fill_tank()
print(auto)
