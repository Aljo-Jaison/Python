from breezypythongui import EasyFrame
import random

class GuessTheNumber(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Guess the num game")
        self.addLabel(text="Guess a num (1-100):", row=0, column=0)
        self.inputField = self.addIntegerField(value=0, row=0, column=1, width=10)
        self.addButton(text="Submit your Guess", row=1, column=0, columnspan=2, command=self.Guess_game)
        self.resultLabel = self.addLabel(text="", row=2, column=0, columnspan=2)
        self.addButton(text="Reset the Game", row=3, column=0, columnspan=2, command=self.game_reseter)
        self.target_number = random.randint(1, 100)
        self.guess_count = 0

    def Guess_game(self):
        try:
            user_guess = self.inputField.getNumber()
            self.guess_count += 1
            if user_guess < self.target_number:
                self.resultLabel["text"] = "Too small, try again."
            elif user_guess > self.target_number:
                self.resultLabel["text"] = "Too large, try again."
            else:
                self.messageBox("Congratulations!", f"You guessed it right in {self.guess_count} attempts!")
                self.game_reseter()
        except:
            self.messageBox("Invalid i/p", "Please enter a valid int.")

    def game_reseter(self):
        self.target_number = random.randint(1, 100)
        self.guess_count = 0
        self.resultLabel["text"] = ""
        self.inputField.setNumber(0)

if __name__ == "__main__":
    GuessTheNumber().mainloop()
