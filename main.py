from tkinter import Tk

class Calc:
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculadora")
        self.window.resizable(0,0)

        self.window.mainloop()

Calc()