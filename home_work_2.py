class car_dealshiper:
    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price


class Car1(car_dealshiper):
    print("BMW", "black", 60000)
print()

class Car2(car_dealshiper):
    print("Mercedes", "red", 50000)
print()

class Car3(car_dealshiper):
    print("VW", "white", 30000)
print()

