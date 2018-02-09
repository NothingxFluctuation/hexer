#this is a program to get hex values of different colors
from tkinter import colorchooser
from tkinter.messagebox import *
from tkinter import Tk
root=Tk()
root.withdraw()
aa=colorchooser.askcolor()
a,b=aa
showinfo("Hex Value","The Hex Value of Color is "+str(b)+'.')
