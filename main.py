from tkinter import *
from tkinter import ttk

import calculator

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("272x300")
        self.title("Calculadora")
        s = ttk.Style()
        s.theme_use('alt')
        ## s.configure('my.TLabel', font='Helvetica 36', background='black', foreground='white')

        self.display = ttk.Label(self, text="0", anchor=E, font='Helvetica 36', background='black', foreground='white', padding=5)
        self.display.pack(side=TOP, fill=BOTH)    


if __name__ == '__main__':
    app = MainApp()
    app.mainloop()