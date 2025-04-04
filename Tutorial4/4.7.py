class Student:
    def __init__(self):
        self.rollno = 0
        self.mark1 = 0
        self.mark2 = 0
        self.total = 0

    def readData(self):
        self.rollno = int(input("Enter Roll Number: "))
        self.mark1 = float(input("Enter Mark 1: "))
        self.mark2 = float(input("Enter Mark 2: "))

    def computeTotal(self):
        self.total = self.mark1 + self.mark2

    def printDetails(self):
        print(f"Roll Number: {self.rollno}")
        print(f"Mark 1: {self.mark1}")
        print(f"Mark 2: {self.mark2}")
        print(f"Total Marks: {self.total}")

student1 = Student()
student1.readData()
student1.computeTotal()
print("\nStudent Details:")
student1.printDetails()
