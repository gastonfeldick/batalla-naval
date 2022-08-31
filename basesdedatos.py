from cgitb import text

import sqlite3
from tkinter.ttk import Treeview
from venv import create 
from tkinter import *
from tkinter import ttk
def insertar():
    conexion=sqlite3.connect("puntajes.db")
    try:
        conexion.execute("""CREATE TABLE jugadores(ID integer primary key AUTOINCREMENT, jugador1 text, jugador2 text, puntosJ1 integer,puntosJ2 integer)""")
        conexion.execute("insert into jugadores(jugador1,jugador2,puntosj1,puntosj2) values(?,?,?,?)",("Gaston","Nicolas",100,10))
        conexion.commit()
        conexion.close()
    except sqlite3.OperationalError:
        
        conexion.execute("insert into jugadores(jugador1,jugador2,puntosj1,puntosj2) values(?,?,?,?)",("Nicolas","Gaston",100,10))
        conexion.commit()
        conexion.close()

def insertar2(g,score,p):
    conexion=sqlite3.connect("puntajes.db")
    try:
        conexion.execute("""CREATE TABLE jugadores(ID integer primary key AUTOINCREMENT, jugador1 text, puntosJ1 integer, jugador2 text,puntosJ2 integer)""")
        conexion.execute("insert into jugadores(jugador1,puntosj1,jugador2,puntosj2) values(?,?,?,?)",(g,score,p,50,))
        conexion.commit()
        conexion.close()
    except sqlite3.OperationalError:
        print("db ya existe")
        conexion.execute("insert into jugadores(jugador1,puntosj1,jugador2,puntosj2) values(?,?,?,?)",(g,score,p,50,))
        conexion.commit()
        conexion.close()

def listar():
    registros=tree.selection()
    for registro in registros:
        tree.delete(registro)
    listaMayor=[]    
    
    conexion=sqlite3.connect("puntajes.db")
    bd=conexion.execute("select * from jugadores")
    for i in bd:
        listaMayor.append(i)
    ordenada=sorted(listaMayor,key=lambda listaMayor:listaMayor[3])
    
    for i in ordenada:
        tree.insert("",0,text=i[0],values=(i[1],i[3],i[2],i[4]))
 
    conexion.close()

    """
    conexion=sqlite3.connect("puntajes.db")
    bd=conexion.execute("select * from jugadores")
    
    for i in bd:
           tabla.insert("",0,text=i[0],values=(i[1],i[3],i[2],i[4]))
        
    conexion.close()"""
ventana=Tk()
ventana.geometry("1050x300")

listaMayor=[]

tree=ttk.Treeview(ventana,columns=('#1','#2','#3','#4'))



tree.heading("#0",text="Numero de juego")
tree.heading("#1",text="Jugador 1")
tree.heading("#2",text="Puntaje")
tree.heading("#3",text="Jugador 2")
tree.heading("#4",text="Puntaje 2")
tree.place(x=20,y=20)
#insertar2("ramiro",310,"eduardo")

btntabla=Button(ventana,text='Tabla',bg="#2E6F78",font=("Orbitron",12),command=lambda:listar())
btntabla.place(x=40,y=380)
ventana.mainloop()

