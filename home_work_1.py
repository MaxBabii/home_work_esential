while True:
    select = input("""
1) BMW
2) Mercedes
3) VW
Enter a car:
""")

    class salon:
        def __init__(self, model, color, price):
            self.model = model
            self.color = color
            self.price = price

    def print_info(self):
        print(self.model, self.color, self.price)


    car1 = salon("BMW", "Black", 60000)

    car2 = salon("Mercedes", "White", 50000)

    car3 = salon("VW", "Blue", 30000)


    if select == "1":
        print_info(car1)

    elif select == "2":
        print_info(car2)

    elif select == "3":
        print_info(car3)


