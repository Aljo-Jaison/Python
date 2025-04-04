from breezypythongui import EasyFrame
from tkinter import DISABLED, NORMAL

class ReverseGuessGame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Guess the Number")
        
        self.lbl_g = self.addLabel(text="Think of a number 1–100.", row=0, column=0, columnspan=2)
        self.btn_sm = self.addButton(text="Too Small", row=1, column=0, command=self.small)
        self.btn_lg = self.addButton(text="Too Large", row=1, column=1, command=self.large)
        self.btn_corr = self.addButton(text="Correct!", row=2, column=0, columnspan=2, command=self.correct)
        self.addButton(text="New Game", row=3, column=0, columnspan=2, command=self.new_game)

        self.l, self.h, self.a = 1, 100, 0
        self.g = 0
        self.guess_game()

    def guess_game(self):
        if self.l <= self.h:
            self.g = (self.l + self.h) // 2
            self.lbl_g["text"] = f"Is it {self.g}?"
        else:
            self.lbl_g["text"] = "Restart game."

    def small(self):
        self.l = self.g + 1
        self.a += 1
        self.guess_game()

    def large(self):
        self.h = self.g - 1
        self.a += 1
        self.guess_game()

    def correct(self):
        self.messageBox("Done!", f"Guessed in {self.a} attempts!")
        self.disable_btns()

    def disable_btns(self):
        self.btn_sm["state"] = DISABLED
        self.btn_lg["state"] = DISABLED
        self.btn_corr["state"] = DISABLED

    def enable_btns(self):
        self.btn_sm["state"] = NORMAL
        self.btn_lg["state"] = NORMAL
        self.btn_corr["state"] = NORMAL

    def new_game(self):
        self.l, self.h, self.a = 1, 100, 0
        self.enable_btns()
        self.guess_game()

if __name__ == "__main__":
    ReverseGuessGame().mainloop()
