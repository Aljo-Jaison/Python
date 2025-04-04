from breezypythongui import EasyFrame
import math

class SqrtCalculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Square Root Calc")
        self.addLabel(text="Enter the Num:", row=0, column=0)
        self.numberField = self.addFloatField(value=0.0, row=0, column=1, width=15)
        self.addLabel(text="Sqrt :", row=1, column=0)
        self.sqrtField = self.addFloatField(value=0.0, row=1, column=1, width=15, precision=2)
        self.sqrtField["state"] = "readonly"
        self.addButton(text="Compute sqrt", row=2, column=0, columnspan=2, command=self.computeSqrt)

    def computeSqrt(self):
        try:
            num = self.numberField.getNumber()
            if num < 0:
                raise ValueError()
            self.sqrtField.setNumber(math.sqrt(num))
        except:
            self.messageBox("Invalid Input", "Please enter a valid non -ve number.")

if __name__ == "__main__":
    SqrtCalculator().mainloop()
