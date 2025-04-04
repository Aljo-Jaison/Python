class Car:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def cost(self):
        print(f"The price of {self.model} ({self.year}) is ₹{self.price}")

car1 = Car("Toyota Fortuner", 2022, 4200000)
car2 = Car("Hyundai i20", 2023, 950000)

car1.cost()
car2.cost()
