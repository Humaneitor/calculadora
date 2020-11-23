from tkinter import *
from tkinter import ttk
import calculator

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("272x300")
        self.title("Calculadora")

        self.display =calculator.Display(self)        
        self.display.pack(side=TOP)

        self.teclado = ttk.Frame(self, width=calculator.WIDTH*4, height=calculator.HEIGHT*5)
        self.teclado.grid_propagate(0)
        self.teclado.pack(side=TOP, fill=BOTH, expand=TRUE)

        botonC = calculator.CalcButton(self.teclado, 'C')
        botonC.grid(row=0, column=0)

        botonC = calculator.CalcButton(self.teclado, '+/-')
        botonC.grid(row=0, column=1)

'''
        self.calcButtonC = ttk.Frame(self, width=136, height=50)
        btn = ttk.Button(self.calcButtonC, text='C')
        self.calcButtonC.pack_propagate(False)
        btn.pack(side=TOP, fill=BOTH, expand=True)
        self.calcButtonC.grid(column=0, row=1, columnspan=2)

        self.calcButtonCS = ttk.Frame(self, width=68, height=50)
        btn = ttk.Button(self.calcButtonCS, text='+\-')
        self.calcButtonCS.pack_propagate(False)
        btn.pack(side=TOP, fill=BOTH, expand=True)
        self.calcButtonCS.grid(column=2, row=1, columnspan=2)        

        self.calcButtonDiv = ttk.Frame(self, width=68, height=50)
        btn = ttk.Button(self.calcButtonDiv, text='/')
        self.calcButtonDiv.pack_propagate(False)
        btn.pack(side=TOP, fill=BOTH, expand=True)
        self.calcButtonDiv.grid(column=4, row=1) 
'''

if __name__ == '__main__':
    app = MainApp()
    app.mainloop()