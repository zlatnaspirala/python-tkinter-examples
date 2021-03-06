#!/usr/bin/env python3

'''
The Grid container provides for multiple widgets to be inserted into a program
based on defined rows and columns.
'''

import tkinter

class Grid(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Grid")

        grid = tkinter.Grid()

        label = tkinter.Label(text="Label 1")
        label.grid(row=0)
        label = tkinter.Label(text="Label 2")
        label.grid(row=0, column=1)
        label = tkinter.Label(text="Label 3")
        label.grid(row=1, column=2)
        label = tkinter.Label(text="Label 4")
        label.grid(row=4, column=3)
        label = tkinter.Label(text="Label 5")
        label.grid(row=2, column=0)

if __name__ == "__main__":
    application = Grid()
    application.mainloop()
