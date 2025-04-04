class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def dataprint(self):
        print(f"Name: {self.name}, Roll Number: {self.roll_number}")

student1 = Student("Anjali", 101)
student2 = Student("Rahul", 102)

student1.dataprint()
student2.dataprint()
