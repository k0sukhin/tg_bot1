class Car:
    def __init__(self,
                 mark=None,
                 model=None,
                 year_of_manufacture=None,
                 mileage=None):

        self.mark = mark
        self.model = model
        self.year_of_manufacture = year_of_manufacture
        self.mileage = mileage

    def mileage_update(self, new_mileage):
        if new_mileage <= self.mileage:
            return print('Указанный пробег меньше либо равен предыдущему.')
        else:
            self.mileage = new_mileage


class Details(Car):
    def __init__(self, name, lifetime=None, mileage_replacement=None):
        self.name = name
        self.lifetime = lifetime
        self.mileage_replacement = mileage_replacement

    def mileage_replacement_create(self, car):
        self.mileage_replacement = car.mileage + self.lifetime

    def check_lifetime(self, car):
        if car.mileage > self.mileage_replacement:
            return f'Комлектующее необходимо было заменить {car.mileage - self.mileage_replacement} км назад!'
        else:
            return f'Ожидает замены через {self.mileage_replacement - car.mileage} км'

    def __str__(self):
        return f'Комплектующее: {self.name}. Необходима замена на {self.mileage_replacement} км'


auto = Car(mark='VW', model='polo', mileage=250_000)

engine_oil = Details('Моторное масло', lifetime=10000)
engine_oil.mileage_replacement_create(auto)

print(engine_oil.lifetime)
print(engine_oil)

print(auto.mileage)
print(engine_oil.check_lifetime(auto))

auto.mileage_update(258999)
print(auto.mileage)

print(engine_oil.check_lifetime(auto))
