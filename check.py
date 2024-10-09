class Car:
    def __init__(self, mark):
        self.mark = mark


class Detail(Car):
    def __init__(self, lifetime):
        self.lifetime = lifetime
        super().__init__(mark)


polo = Car('VW')
oil = Detail(10)
print(oil.mark)

