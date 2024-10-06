class Car:
    def init(self, mark=None, model=None, year_of_manufacture=None, mileage=None):

        self.mark = mark
        self.model = model
        self.year_of_manufacture = year_of_manufacture
        self.milage = mileage

    def milage_update(self, new_mileage):
        self.milage = new_mileage


class Details(Car):
    def init(self, milage=None, lifetime=None):
        self.lifetime = lifetime
        super().init(milage)

    def check_lifetime(self):
        pass


polo = Car(mark='VW', model='polo', mileage=250_000)

engine_oil = Details(lifetime=10000)

print(engine_oil.lifetime)
