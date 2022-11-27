# Cars

    def empty_tank(self, limit=None):
        if not limit:
            limit = 0
            self.tanked_fuel = 0
        return self.tanked_fuel