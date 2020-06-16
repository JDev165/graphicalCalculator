from tkinter import *

class CalculatorGUI:

    def __init__(self):
        self.gui = Tk()

    def create(self):
        setTitle()
        setSize()

    # What's the naming convention for private functions?
    def setTitle(self, titleString):
        self.gui.title(titleString)

    def setSize(self, dimensionsString):
        self.gui.geometry(dimensionsString)
