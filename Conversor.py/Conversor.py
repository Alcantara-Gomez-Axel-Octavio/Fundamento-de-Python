#App para convertir pies a metros usando Tkinter
#Alcantara Gomez Axel Octavio
#23 de febrero 2023

from tkinter import *
from tkinter import ttk


if __name__=="__main__":
    print("Solo se mostrara si es el principal")

class Conversor: 

    def __init__(self, raiz):
        self.pies=StringVar()
        self.metros=StringVar()
        raiz.title("Pies a metros")

