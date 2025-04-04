class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def display(self):
        if self.imag >= 0:
            print(f"{self.real} + {self.imag}i")
        else:
            print(f"{self.real} - {abs(self.imag)}i")

c1 = Complex(3, 4)
c2 = Complex(1, -2)

c3 = c1 + c2

print("First Complex Number: ", end="")
c1.display()

print("Second Complex Number: ", end="")
c2.display()

print("Sum: ", end="")
c3.display()
