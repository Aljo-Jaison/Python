class Mobile:
    def __init__(self):
        self.company = ""
        self.model = ""
        self.price = 0.0

    def set_details(self):
        self.company = input("Enter Mobile Company: ")
        self.model = input("Enter Mobile Model: ")
        self.price = float(input("Enter Mobile Price: "))

    def display_details(self):
        print(f"Company: {self.company}")
        print(f"Model: {self.model}")
        print(f"Price: ₹{self.price}")

mobile1 = Mobile()
mobile1.set_details()
print("\nMobile Details:")
mobile1.display_details()
