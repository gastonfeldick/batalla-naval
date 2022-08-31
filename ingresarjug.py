from cProfile import label
from cgitb import text
import string
from tkinter import *
from unicodedata import name

def insertarjugadores():
    ventananueva=Toplevel()
    ventananueva.geometry("300x300")
    etiquetajug1=Label(ventananueva,text="Jugador N°1:")
    entradajug1=Entry(ventananueva,textvariable=jug1)

    etiquetajug2=Label(ventananueva,text="Jugador N°2:")
    entradajug2=Entry(ventananueva,textvariable=jug2)
    etiquetajug1.place(x=60,y=100)
    entradajug1.place(x=140,y=100)

    etiquetajug2.place(x=60,y=150)
    entradajug2.place(x=140,y=150)

    



ventana=Tk()
jug1=StringVar(value="Jugador1")
jug2=StringVar(value="Jugador2")

Namejug1=Label(ventana,textvariable=jug1)
Namejug2=Label(ventana,textvariable=jug2)

Namejug1.place(x=120,y=50)
Namejug2.place(x=120,y=80)

Cargarjug=Button(ventana,text="Cargar jugadores",command=insertarjugadores)
Cargarjug.place(x=100,y=100)


ventana.geometry("500x500")






ventana.mainloop()