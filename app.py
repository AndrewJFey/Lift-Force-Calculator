# app.py

from tkinter import Tk
from logic import LiftCalculatorLogic
from ui import LiftCalculatorUI

class LiftCalculatorApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Force of Lift")
        self.root.geometry('550x350')

        self.logic = LiftCalculatorLogic()
        self.ui = LiftCalculatorUI(self.root, self.logic)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = LiftCalculatorApp()
    app.run()
