class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.cost = 0.0

    def get_details(self):
        self.title = input("Enter Book Title: ")
        self.author = input("Enter Author Name: ")
        self.cost = float(input("Enter Book Cost: "))

    def print_details(self):
        print(f"\nBook Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Cost: ₹{self.cost}")

book1 = Book()
book1.get_details()
book1.print_details()
