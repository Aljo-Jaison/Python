from breezypythongui import EasyFrame

class BouncyBallCalculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Bouncy Ball Distance Calculator")

        
        self.addLabel(text="Initial Height:", row=0, column=0)
        self.heightField = self.addFloatField(value=0.0, row=0, column=1, width=10)

        self.addLabel(text="Bounciness Index:", row=1, column=0)
        self.bounceField = self.addFloatField(value=0.0, row=1, column=1, width=10)

        self.addLabel(text="Number of Bounces:", row=2, column=0)
        self.bouncesField = self.addIntegerField(value=0, row=2, column=1, width=10)

        self.addLabel(text="Total Distance:", row=3, column=0)
        self.resultField = self.addFloatField(value=0.0, row=3, column=1, width=10, precision=2)
        self.resultField["state"] = "readonly"

        
        self.addButton(text="Compute Distance", row=4, column=0, columnspan=2, command=self.computeDistance)

    def computeDistance(self):
        try:
            h = self.heightField.getNumber()
            b = self.bounceField.getNumber()
            n = self.bouncesField.getNumber()

            if h < 0 or b < 0 or b >= 1 or n < 0:
                self.messageBox("Error", "Please enter valid positive values. Bounciness should be between 0 and 1.")
                return

            d = h
            for _ in range(n):
                h *= b
                d += 2 * h

            self.resultField.setNumber(d)
        except:
            self.messageBox("Error", "Please enter valid numeric inputs.")


if __name__ == "__main__":
    BouncyBallCalculator().mainloop()
