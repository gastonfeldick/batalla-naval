from tkinter import *
from tkinter.ttk import Treeview
import random
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import font
from unicodedata import name
import pygame
import sqlite3
#from basesdedatos import *

def musica():
    print("")
    pygame.mixer.music.load("CORTINA2.WAV")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)

def controlvolumen(value):

    print("")
    res=volumen.get()/100
    pygame.mixer.music.set_volume(res)
    
    print("volumen",res)

def funcion(f,c,num):
    print(f"fila:{f} columna:{c}")

    if bar.get()==0:    # jugador 1
        for i in range(91,181):
            listabotones[i-1].config(state=DISABLED)
        for i in range(91):
            listabotones[i-1].config(state=NORMAL)
        if matriz[f-1][c-1]==1:
            listabotones[num-1].config(bg="#FF1493")
            listabotones[num-1].config(state=DISABLED)
            listaDESABLED.append(listabotones[num-1])
        elif matriz[f-1][c-1]==2:
            listabotones[num-1].config(bg="#696969")
            listabotones[num-1].config(state=DISABLED)
            listaDESABLED.append(listabotones[num-1])
        elif matriz[f-1][c-1]==3:
            listabotones[num-1].config(bg="#00C957")
            listabotones[num-1].config(state=DISABLED)
            listaDESABLED.append(listabotones[num-1])
        elif matriz[f-1][c-1]==4:
            listabotones[num-1].config(bg="#FFF68F")
            listabotones[num-1].config(state=DISABLED)
            listaDESABLED.append(listabotones[num-1])
        else:
            listabotones[num-1].config(bg="blue")
        for i in range(91):
            listabotones[i-1].config(state=DISABLED)
        for i in range(91,181):
            listabotones[i-1].config(state=NORMAL)
        for i in listaDESABLED:
            i.config(state=DISABLED)
        bar.set(1)
    else:#jugador 2
        for i in range(91):
            listabotones[i-1].config(state=DISABLED)
        for i in range(90,181):
            listabotones[i-1].config(state=NORMAL)
        if mj2[f-1][c-1]==1:
            listabotones[num-1].config(bg="#FF1493")
            listabotones[num-1].config(state=DISABLED)
            listaDESABLED.append(listabotones[num-1])
        elif mj2[f-1][c-1]==2:
            listabotones[num-1].config(bg="#696969")
            listabotones[num-1].config(state=DISABLED)
            listaDESABLED.append(listabotones[num-1])
        elif mj2[f-1][c-1]==3:
            listabotones[num-1].config(bg="#00C957")
            listabotones[num-1].config(state=DISABLED)
            listaDESABLED.append(listabotones[num-1])
        elif mj2[f-1][c-1]==4:
            listabotones[num-1].config(bg="#FFF68F")
            listabotones[num-1].config(state=DISABLED)
            listaDESABLED.append(listabotones[num-1])
        else:
            listabotones[num-1].config(bg="blue")

        for i in range(90,181):
            listabotones[i-1].config(state=DISABLED)
        for i in range(91):
            listabotones[i-1].config(state=NORMAL)
        for i in listaDESABLED:
            i.config(state=DISABLED)
        bar.set(0)

    control(f,c,num)
    
def rellenar():

    dif1.config(state=DISABLED)
    dif2.config(state=DISABLED)
    dif3.config(state=DISABLED)
    if dificultad.get()==1:
        destructor.set(6)
        cruceros.set(6)
        des2.set(6)
        cru2.set(6)
    elif dificultad.get()==2:
        destructor.set(6)
        des2.set(6)

    insertarjugadores()

    for r in range(91):
        listabotones[r-1].config(state=NORMAL)

    etijug1.config(state=NORMAL)
    etijug2.config(state=DISABLED)

    #submarinos
    i=0
    while i<4:
        f=random.randint(0,9)
        c=random.randint(0,8)
        if  matriz[f][c]!=0:
            print("repetido")

        else:
            matriz[f][c]=1
            i+=1
           
    #destructores
    if dificultad.get()==3:
        hv=random.randint(0,1)
        i=0
        while i<3:
            if hv==0:#horizontal
                f=random.randint(0,9)
                c=random.randint(0,7)
                if  matriz[f][c]!=0 or matriz[f][c+1]!=0 :
                    print("repetido destructor")
                else:
                    matriz[f][c]=2
                    matriz[f][c+1]=2
                    i+=1
            else:#vertical
                f=random.randint(0,8)
                c=random.randint(0,8)
                if  matriz[f+1][c]!=0 or matriz[f][c]!=0 :
                    print("repetido destructor")
                else:
                    matriz[f][c]=2
                    matriz[f+1][c]=2
                    i+=1
            hv=random.randint(0,1)

    #cruceros
    if dificultad.get()==2 or dificultad.get()== 3:
        hv=random.randint(0,1)
        i=0
        while i<2:
            if hv==0:#horizontal
                f=random.randint(0,9)
                c=random.randint(0,6)
                if  matriz[f][c]!=0 or matriz[f][c+1]!=0 or matriz[f][c+2]!=0:
                    print("repetido cruceros")
                else:
                    matriz[f][c]=3
                    matriz[f][c+1]=3
                    matriz[f][c+2]=3
                    i+=1
            else:
                f=random.randint(0,7)
                c=random.randint(0,8)
                if  matriz[f][c]!=0 or matriz[f+1][c]!=0 or matriz[f+2][c]!=0 :
                    print("repetido cruceros")
                else:
                    matriz[f][c]=3
                    matriz[f+1][c]=3
                    matriz[f+2][c]=3
                    i+=1
            hv=random.randint(0,1)
    
    #acorazado
    hv=random.randint(0,1)
    i=0
    if hv==0:#horizontal
        while i==0:
            f=random.randint(0,9)
            c=random.randint(0,5)
            if  matriz[f][c]!=0 or matriz[f][c+1]!=0 or matriz[f][c+2]!=0 or matriz[f][c+3]!=0:
                print("repetido destructor")
            else:
                matriz[f][c]=4
                matriz[f][c+1]=4
                matriz[f][c+2]=4
                matriz[f][c+3]=4
                i=1
    else:
         while i==0:
        
            f=random.randint(0,6)
            c=random.randint(0,8)
            if  matriz[f][c]!=0 or matriz[f+1][c]!=0 or matriz[f+2][c]!=0 or matriz[f+3][c]!=0 :
                print("repetido destructor")
            else:
                matriz[f][c]=4
                matriz[f+1][c]=4
                matriz[f+2][c]=4
                matriz[f+3][c]=4
                i+=1


    print("hola \n")
    print(matriz)

    #jugador 2
    #submarinos2
    i=0
    while i<4:
        f=random.randint(0,9)
        c=random.randint(0,8)
        if  mj2[f][c]!=0:
            print("repetido")

        else:
            mj2[f][c]=1
            i+=1
           
    #destructores2
    if dificultad.get()==3:
        hv=random.randint(0,1)
        i=0
        while i<3:
            if hv==0:#horizontal
                f=random.randint(0,9)
                c=random.randint(0,7)
                if  mj2[f][c]!=0 or mj2[f][c+1]!=0 :
                    print("repetido destructor")
                else:
                    mj2[f][c]=2
                    mj2[f][c+1]=2
                    i+=1
            else:#vertical
                f=random.randint(0,8)
                c=random.randint(0,8)
                if  mj2[f+1][c]!=0 or mj2[f][c]!=0 :
                    print("repetido destructor")
                else:
                    mj2[f][c]=2
                    mj2[f+1][c]=2
                    i+=1
            hv=random.randint(0,1)

    #cruceros2
    if dificultad.get()==2 or dificultad.get()== 3:
        hv=random.randint(0,1)
        i=0
        while i<2:
            if hv==0:#horizontal
                f=random.randint(0,9)
                c=random.randint(0,6)
                if  mj2[f][c]!=0 or mj2[f][c+1]!=0 or mj2[f][c+2]!=0:
                    print("repetido cruceros")
                else:
                    mj2[f][c]=3
                    mj2[f][c+1]=3
                    mj2[f][c+2]=3
                    i+=1
            else:
                f=random.randint(0,7)
                c=random.randint(0,8)
                if  mj2[f][c]!=0 or mj2[f+1][c]!=0 or mj2[f+2][c]!=0 :
                    print("repetido cruceros")
                else:
                    mj2[f][c]=3
                    mj2[f+1][c]=3
                    mj2[f+2][c]=3
                    i+=1
            hv=random.randint(0,1)
        
    #acorazado2
    hv=random.randint(0,1)
    i=0
    if hv==0:#horizontal
        while i==0:
            f=random.randint(0,9)
            c=random.randint(0,5)
            if  mj2[f][c]!=0 or mj2[f][c+1]!=0 or mj2[f][c+2]!=0 or mj2[f][c+3]!=0:
                print("repetido destructor")
            else:
                mj2[f][c]=4
                mj2[f][c+1]=4
                mj2[f][c+2]=4
                mj2[f][c+3]=4
                i=1
    else:
         while i==0:
        
            f=random.randint(0,6)
            c=random.randint(0,8)
            if  mj2[f][c]!=0 or mj2[f+1][c]!=0 or mj2[f+2][c]!=0 or mj2[f+3][c]!=0 :
                print("repetido destructor")
            else:
                mj2[f][c]=4
                mj2[f+1][c]=4
                mj2[f+2][c]=4
                mj2[f+3][c]=4
                i+=1


    print("hola \n")
    print(matriz)
    print('matrzi jugador 2 \n', mj2)


    btnjugar.config(state=DISABLED)
    btnvolver.config(state=NORMAL)

def control(i,j,Ju):
    sonido1=pygame.mixer.Sound("bomba.wav")
    if Ju<=90:
        if matriz[i-1][j-1]==1:
            aux=submarino.get()
            aux+=1
            submarino.set(aux)
            sonido1.play()
            sonido1.set_volume(1.0)
        elif matriz[i-1][j-1]==2:
            aux=destructor.get()
            aux+=1
            destructor.set(aux)
            sonido1.play()
            sonido1.set_volume(1.0)
            
        elif matriz[i-1][j-1]==3:
            aux=cruceros.get()
            aux+=1
            cruceros.set(aux)
            sonido1.play()
            sonido1.set_volume(1.0)
        elif matriz[i-1][j-1]==4:
            aux=acorazado.get()
            aux+=1
            acorazado.set(aux)
            sonido1.play()
            sonido1.set_volume(1.0)
        etijug1.config(state=DISABLED)
        etijug2.config(state=NORMAL)
    else:
        if mj2[i-1][j-1]==1:
            aux=sub2.get()
            aux+=1
            sub2.set(aux)
            sonido1.play()
            sonido1.set_volume(1.0)
        elif mj2[i-1][j-1]==2:
            aux=des2.get()
            aux+=1
            des2.set(aux)
            sonido1.play()
            sonido1.set_volume(1.0)
        elif mj2[i-1][j-1]==3:
            aux=cru2.get()
            aux+=1
            cru2.set(aux)
            sonido1.play()
            sonido1.set_volume(1.0)
        elif mj2[i-1][j-1]==4:
            aux=aco2.get()
            aux+=1
            aco2.set(aux)
            sonido1.play()
            sonido1.set_volume(1.0)
        etijug1.config(state=NORMAL)
        etijug2.config(state=DISABLED)
    gano(Ju)
      
def gano(jug2):

    print(f"submarino:{submarino.get()} destructor:{destructor.get()} crucero:{cruceros.get()} acorazado:{acorazado.get()}\n")
    print(f"submarino2:{sub2.get()} destructor2:{des2.get()} crucero2:{cru2.get()} acorazado2:{aco2.get()}\n")
    if jug2<=90:
        if submarino.get()==4 and destructor.get()==6 and cruceros.get()==6 and acorazado.get()==4:
            puntosganador=((submarino.get()+destructor.get()+cruceros.get()+acorazado.get())-(sub2.get()+des2.get()+cru2.get()+aco2.get()))*100
            puntosperdedor=10
            insertar(Name1.get(),puntosganador,Name2.get())
            messagebox.showinfo(message=f"GANO {Name1.get()} Puntos: {puntosganador}", title="ganador,")
            dif1.config(state=NORMAL)
            dif2.config(state=NORMAL)
            dif3.config(state=NORMAL)
            for i in listabotones:
                i.config(state=DISABLED)
    else:
        if sub2.get()==4 and des2.get()==6 and cru2.get()==6 and aco2.get()==4:
            puntosganador=((sub2.get()+des2.get()+cru2.get()+aco2.get())-(submarino.get()+destructor.get()+cruceros.get()+acorazado.get()))*100
            puntosperdedor=10
            insertar(Name2.get(),puntosganador,Name1.get())
            print(f"puntosganador:{puntosganador}")
            messagebox.showinfo(message=f"GANO {Name2.get()} Puntos: {puntosganador}", title="ganador")
            dif1.config(state=NORMAL)
            dif2.config(state=NORMAL)
            dif3.config(state=NORMAL)
            for i in listabotones:
                i.config(state=DISABLED)
    
def restart():
    for i in range(181):
        if i<=90:
            listabotones[i-1].config(state=NORMAL)
        listabotones[i-1].config(bg="cyan")
    for i in range(0,10):
        print(i)
        for j in range(0,9):
            matriz[i][j]=0
            mj2[i][j]=0
    
    submarino.set(0)
    destructor.set(0)
    cruceros.set(0)
    acorazado.set(0)
    bar.set(0)

    sub2.set(0)
    des2.set(0)
    cru2.set(0)
    aco2.set(0)

    listaDESABLED.clear()

    btnjugar.config(state=NORMAL)
    btnvolver.config(state=DISABLED)

    for i in listabotones:
        i.config(state=DISABLED)


    print("matriz \n",matriz)
    print("matriz 2 \n",mj2)
    print(listaDESABLED)

def insertarjugadores():
    ventananueva=Toplevel()
    ventananueva.geometry("300x300")
    etiquetajug1=Label(ventananueva,text="Jugador N°1:")
    entradajug1=Entry(ventananueva,textvariable=Name1)

    etiquetajug2=Label(ventananueva,text="Jugador N°2:")
    entradajug2=Entry(ventananueva,textvariable=Name2)
    etiquetajug1.place(x=60,y=100)
    entradajug1.place(x=140,y=100)

    etiquetajug2.place(x=60,y=150)
    entradajug2.place(x=140,y=150)

def insertar(g,score,p):
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
    listar()

def listar():
    """
    registros=tabla.get_children()
    for registro in registros:
        tabla.delete(registro)

    conexion=sqlite3.connect("puntajes.db")
    bd=conexion.execute("select * from jugadores")
    for i in bd:
        tabla.insert("",0,text=i[0],values=(i[1],i[3],i[2],i[4]))
    conexion.close()"""
    conexion=sqlite3.connect("puntajes.db")
    bd=conexion.execute("select * from jugadores")
    registros=tabla.get_children()
    for registro in registros:
        tabla.delete(registro)
    
    listaMayor=[]
    for i in bd:
        listaMayor.append(i)
    ordenada=sorted(listaMayor,key=lambda listaMayor:listaMayor[3])
    
    for i in ordenada:
        tabla.insert("",0,text=i[0],values=(i[1],i[3],i[2],i[4]))

    conexion.close()

matriz = [[0 for i in range(9)] for i in range(10)] # matriz jugador1
mj2 =  [[0 for i in range(9)] for i in range(10)] # matriz jugador2

ventana=Tk()
ventana.geometry("710x800")
ventana.title('BATALLA NAVAL')
fondo=PhotoImage(file="imagen1.gif")
lblfondo=Label(ventana,image=fondo).place(x=0,y=0)
volumen=IntVar(value=50)
scale=Scale(ventana,orient="vertical",from_=100,to=0,variable=volumen,command=controlvolumen)
scale.place(x=660,y=40, height = 300,width = 50)
pygame.mixer.init()
musica()

#variables cantidad barcos

submarino=IntVar()
destructor=IntVar()
cruceros=IntVar()
acorazado=IntVar()

sub2=IntVar()
des2=IntVar()
cru2=IntVar()
aco2=IntVar()

listaMayor=[]

bar=IntVar(value=0) #turno

dificultad=IntVar(value="1")

dif1=Radiobutton(ventana, text="Facil",variable=dificultad,value=1)
dif2=Radiobutton(ventana, text="Medio",variable=dificultad,value=2)
dif3=Radiobutton(ventana, text="dificil",variable=dificultad, value=3)

dif1.place(x=40,y=680)
dif2.place(x=95,y=680)
dif3.place(x=160,y=680)
#Variablesjugadores
Name1=StringVar(value="jugador 1")
Name2=StringVar(value="jugador 2")


etijug1=Label(ventana,textvariable=Name1,bg='#4D8153',fg='#FFFFFF')
etijug1.place(x=90,y=40)
etijug1.config(font=('Orbitron',12,'bold'))
etijug2=Label(ventana,textvariable=Name2,bg='#4D8153',fg='#FFFFFF',font=("Orbitron", 12,'bold') )
etijug2.place(x=290,y=40)


btnjugar=Button(ventana,text="Jugar",bg="#2E6F78",command=lambda:rellenar())
btnjugar.config(font=("Orbitron",12))
btnjugar.place(x=80,y=380)
btnvolver=Button(ventana,text="Volver a jugar",bg="#2E6F78",state=DISABLED,command=restart)
btnvolver.config(font=("Orbitron",12))
btnvolver.place(x=150,y=380)
btnsalir=Button(ventana,text='salir',bg="#DC2121",command=lambda:ventana.destroy())


btnsalir.config(font=("Orbitron",12))
btnsalir.place(x=300,y=380)

listabotones=[]

listaDESABLED=[]


a1=Button(ventana,text="",command=lambda:funcion(1,1,1),bg="cyan",width=1,height=1)
listabotones.append(a1)
a2=Button(ventana,text="",command=lambda:funcion(1,2,2),bg="cyan",width=1,height=1)
listabotones.append(a2)
a3=Button(ventana,text="",command=lambda:funcion(1,3,3),bg="cyan",width=1,height=1)
listabotones.append(a3)
a4=Button(ventana,text="",command=lambda:funcion(1,4,4),bg="cyan",width=1,height=1)
listabotones.append(a4)
a5=Button(ventana,text="",command=lambda:funcion(1,5,5),bg="cyan",width=1,height=1)
listabotones.append(a5)
a6=Button(ventana,text="",command=lambda:funcion(1,6,6),bg="cyan",width=1,height=1)
listabotones.append(a6)
a7=Button(ventana,text="",command=lambda:funcion(1,7,7),bg="cyan",width=1,height=1)
listabotones.append(a7)
a8=Button(ventana,text="",command=lambda:funcion(1,8,8),bg="cyan",width=1,height=1)
listabotones.append(a8)
a9=Button(ventana,text="",command=lambda:funcion(1,9,9),bg="cyan",width=1,height=1)
listabotones.append(a9)

b1=Button(ventana,text="",command=lambda:funcion(2,1,10),bg="cyan",width=1,height=1)
listabotones.append(b1)
b2=Button(ventana,text="",command=lambda:funcion(2,2,11),bg="cyan",width=1,height=1)
listabotones.append(b2)
b3=Button(ventana,text="",command=lambda:funcion(2,3,12),bg="cyan",width=1,height=1)
listabotones.append(b3)
b4=Button(ventana,text="",command=lambda:funcion(2,4,13),bg="cyan",width=1,height=1)
listabotones.append(b4)
b5=Button(ventana,text="",command=lambda:funcion(2,5,14),bg="cyan",width=1,height=1)
listabotones.append(b5)
b6=Button(ventana,text="",command=lambda:funcion(2,6,15),bg="cyan",width=1,height=1)
listabotones.append(b6)
b7=Button(ventana,text="",command=lambda:funcion(2,7,16),bg="cyan",width=1,height=1)
listabotones.append(b7)
b8=Button(ventana,text="",command=lambda:funcion(2,8,17),bg="cyan",width=1,height=1)
listabotones.append(b8)
b9=Button(ventana,text="",command=lambda:funcion(2,9,18),bg="cyan",width=1,height=1)
listabotones.append(b9)

c1=Button(ventana,text="",command=lambda:funcion(3,1,19),bg="cyan",width=1,height=1)
listabotones.append(c1)
c2=Button(ventana,text="",command=lambda:funcion(3,2,20),bg="cyan",width=1,height=1)
listabotones.append(c2)
c3=Button(ventana,text="",command=lambda:funcion(3,3,21),bg="cyan",width=1,height=1)
listabotones.append(c3)
c4=Button(ventana,text="",command=lambda:funcion(3,4,22),bg="cyan",width=1,height=1)
listabotones.append(c4)
c5=Button(ventana,text="",command=lambda:funcion(3,5,23),bg="cyan",width=1,height=1)
listabotones.append(c5)
c6=Button(ventana,text="",command=lambda:funcion(3,6,24),bg="cyan",width=1,height=1)
listabotones.append(c6)
c7=Button(ventana,text="",command=lambda:funcion(3,7,25),bg="cyan",width=1,height=1)
listabotones.append(c7)
c8=Button(ventana,text="",command=lambda:funcion(3,8,26),bg="cyan",width=1,height=1)
listabotones.append(c8)
c9=Button(ventana,text="",command=lambda:funcion(3,9,27),bg="cyan",width=1,height=1)
listabotones.append(c9)

d1=Button(ventana,text="",command=lambda:funcion(4,1,28),bg="cyan",width=1,height=1)
listabotones.append(d1)
d2=Button(ventana,text="",command=lambda:funcion(4,2,29),bg="cyan",width=1,height=1)
listabotones.append(d2)
d3=Button(ventana,text="",command=lambda:funcion(4,3,30),bg="cyan",width=1,height=1)
listabotones.append(d3)
d4=Button(ventana,text="",command=lambda:funcion(4,4,31),bg="cyan",width=1,height=1)
listabotones.append(d4)
d5=Button(ventana,text="",command=lambda:funcion(4,5,32),bg="cyan",width=1,height=1)
listabotones.append(d5)
d6=Button(ventana,text="",command=lambda:funcion(4,6,33),bg="cyan",width=1,height=1)
listabotones.append(d6)
d7=Button(ventana,text="",command=lambda:funcion(4,7,34),bg="cyan",width=1,height=1)
listabotones.append(d7)
d8=Button(ventana,text="",command=lambda:funcion(4,8,35),bg="cyan",width=1,height=1)
listabotones.append(d8)
d9=Button(ventana,text="",command=lambda:funcion(4,9,36),bg="cyan",width=1,height=1)
listabotones.append(d9)

e1=Button(ventana,text="",command=lambda:funcion(5,1,37),bg="cyan",width=1,height=1)
listabotones.append(e1)
e2=Button(ventana,text="",command=lambda:funcion(5,2,38),bg="cyan",width=1,height=1)
listabotones.append(e2)
e3=Button(ventana,text="",command=lambda:funcion(5,3,39),bg="cyan",width=1,height=1)
listabotones.append(e3)
e4=Button(ventana,text="",command=lambda:funcion(5,4,40),bg="cyan",width=1,height=1)
listabotones.append(e4)
e5=Button(ventana,text="",command=lambda:funcion(5,5,41),bg="cyan",width=1,height=1)
listabotones.append(e5)
e6=Button(ventana,text="",command=lambda:funcion(5,6,42),bg="cyan",width=1,height=1)
listabotones.append(e6)
e7=Button(ventana,text="",command=lambda:funcion(5,7,43),bg="cyan",width=1,height=1)
listabotones.append(e7)
e8=Button(ventana,text="",command=lambda:funcion(5,8,44),bg="cyan",width=1,height=1)
listabotones.append(e8)
e9=Button(ventana,text="",command=lambda:funcion(5,9,45),bg="cyan",width=1,height=1)
listabotones.append(e9)

f1=Button(ventana,text="",command=lambda:funcion(6,1,46),bg="cyan",width=1,height=1)
listabotones.append(f1)
f2=Button(ventana,text="",command=lambda:funcion(6,2,47),bg="cyan",width=1,height=1)
listabotones.append(f2)
f3=Button(ventana,text="",command=lambda:funcion(6,3,48),bg="cyan",width=1,height=1)
listabotones.append(f3)
f4=Button(ventana,text="",command=lambda:funcion(6,4,49),bg="cyan",width=1,height=1)
listabotones.append(f4)
f5=Button(ventana,text="",command=lambda:funcion(6,5,50),bg="cyan",width=1,height=1)
listabotones.append(f5)
f6=Button(ventana,text="",command=lambda:funcion(6,6,51),bg="cyan",width=1,height=1)
listabotones.append(f6)
f7=Button(ventana,text="",command=lambda:funcion(6,7,52),bg="cyan",width=1,height=1)
listabotones.append(f7)
f8=Button(ventana,text="",command=lambda:funcion(6,8,53),bg="cyan",width=1,height=1)
listabotones.append(f8)
f9=Button(ventana,text="",command=lambda:funcion(6,9,54),bg="cyan",width=1,height=1)
listabotones.append(f9)

g1=Button(ventana,text="",command=lambda:funcion(7,1,55),bg="cyan",width=1,height=1)
listabotones.append(g1)
g2=Button(ventana,text="",command=lambda:funcion(7,2,56),bg="cyan",width=1,height=1)
listabotones.append(g2)
g3=Button(ventana,text="",command=lambda:funcion(7,3,57),bg="cyan",width=1,height=1)
listabotones.append(g3)
g4=Button(ventana,text="",command=lambda:funcion(7,4,58),bg="cyan",width=1,height=1)
listabotones.append(g4)
g5=Button(ventana,text="",command=lambda:funcion(7,5,59),bg="cyan",width=1,height=1)
listabotones.append(g5)
g6=Button(ventana,text="",command=lambda:funcion(7,6,60),bg="cyan",width=1,height=1)
listabotones.append(g6)
g7=Button(ventana,text="",command=lambda:funcion(7,7,61),bg="cyan",width=1,height=1)
listabotones.append(g7)
g8=Button(ventana,text="",command=lambda:funcion(7,8,62),bg="cyan",width=1,height=1)
listabotones.append(g8)
g9=Button(ventana,text="",command=lambda:funcion(7,9,63),bg="cyan",width=1,height=1)
listabotones.append(g9)

h1=Button(ventana,text="",command=lambda:funcion(8,1,64),bg="cyan",width=1,height=1)
listabotones.append(h1)
h2=Button(ventana,text="",command=lambda:funcion(8,2,65),bg="cyan",width=1,height=1)
listabotones.append(h2)
h3=Button(ventana,text="",command=lambda:funcion(8,3,66),bg="cyan",width=1,height=1)
listabotones.append(h3)
h4=Button(ventana,text="",command=lambda:funcion(8,4,67),bg="cyan",width=1,height=1)
listabotones.append(h4)
h5=Button(ventana,text="",command=lambda:funcion(8,5,68),bg="cyan",width=1,height=1)
listabotones.append(h5)
h6=Button(ventana,text="",command=lambda:funcion(8,6,69),bg="cyan",width=1,height=1)
listabotones.append(h6)
h7=Button(ventana,text="",command=lambda:funcion(8,7,70),bg="cyan",width=1,height=1)
listabotones.append(h7)
h8=Button(ventana,text="",command=lambda:funcion(8,8,71),bg="cyan",width=1,height=1)
listabotones.append(h8)
h9=Button(ventana,text="",command=lambda:funcion(8,9,72),bg="cyan",width=1,height=1)
listabotones.append(h9)

i1=Button(ventana,text="",command=lambda:funcion(9,1,73),bg="cyan",width=1,height=1)
listabotones.append(i1)
i2=Button(ventana,text="",command=lambda:funcion(9,2,74),bg="cyan",width=1,height=1)
listabotones.append(i2)
i3=Button(ventana,text="",command=lambda:funcion(9,3,75),bg="cyan",width=1,height=1)
listabotones.append(i3)
i4=Button(ventana,text="",command=lambda:funcion(9,4,76),bg="cyan",width=1,height=1)
listabotones.append(i4)
i5=Button(ventana,text="",command=lambda:funcion(9,5,77),bg="cyan",width=1,height=1)
listabotones.append(i5)
i6=Button(ventana,text="",command=lambda:funcion(9,6,78),bg="cyan",width=1,height=1)
listabotones.append(i6)
i7=Button(ventana,text="",command=lambda:funcion(9,7,79),bg="cyan",width=1,height=1)
listabotones.append(i7)
i8=Button(ventana,text="",command=lambda:funcion(9,8,80),bg="cyan",width=1,height=1)
listabotones.append(i8)
i9=Button(ventana,text="",command=lambda:funcion(9,9,81),bg="cyan",width=1,height=1)
listabotones.append(i9)

j1=Button(ventana,text="",command=lambda:funcion(10,1,82),bg="cyan",width=1,height=1)
listabotones.append(j1)
j2=Button(ventana,text="",command=lambda:funcion(10,2,83),bg="cyan",width=1,height=1)
listabotones.append(j2)
j3=Button(ventana,text="",command=lambda:funcion(10,3,84),bg="cyan",width=1,height=1)
listabotones.append(j3)
j4=Button(ventana,text="",command=lambda:funcion(10,4,85),bg="cyan",width=1,height=1)
listabotones.append(j4)
j5=Button(ventana,text="",command=lambda:funcion(10,5,86),bg="cyan",width=1,height=1)
listabotones.append(j5)
j6=Button(ventana,text="",command=lambda:funcion(10,6,87),bg="cyan",width=1,height=1)
listabotones.append(j6)
j7=Button(ventana,text="",command=lambda:funcion(10,7,88),bg="cyan",width=1,height=1)
listabotones.append(j7)
j8=Button(ventana,text="",command=lambda:funcion(10,8,89),bg="cyan",width=1,height=1)
listabotones.append(j8)
j9=Button(ventana,text="",command=lambda:funcion(10,9,90),bg="cyan",width=1,height=1)
listabotones.append(j9)


a1.place(x=50,y=70)
a2.place(x=68,y=70)
a3.place(x=86,y=70)
a4.place(x=104,y=70)
a5.place(x=122,y=70)
a6.place(x=140,y=70)
a7.place(x=158,y=70)
a8.place(x=176,y=70)
a9.place(x=194,y=70)

b1.place(x=50,y=97)
b2.place(x=68,y=97)
b3.place(x=86,y=97)
b4.place(x=104,y=97)
b5.place(x=122,y=97)
b6.place(x=140,y=97)
b7.place(x=158,y=97)
b8.place(x=176,y=97)
b9.place(x=194,y=97)

c1.place(x=50,y=124)
c2.place(x=68,y=124)
c3.place(x=86,y=124)
c4.place(x=104,y=124)
c5.place(x=122,y=124)
c6.place(x=140,y=124)
c7.place(x=158,y=124)
c8.place(x=176,y=124)
c9.place(x=194,y=124)

d1.place(x=50,y=151)
d2.place(x=68,y=151)
d3.place(x=86,y=151)
d4.place(x=104,y=151)
d5.place(x=122,y=151)
d6.place(x=140,y=151)
d7.place(x=158,y=151)
d8.place(x=176,y=151)
d9.place(x=194,y=151)

e1.place(x=50,y=178)
e2.place(x=68,y=178)
e3.place(x=86,y=178)
e4.place(x=104,y=178)
e5.place(x=122,y=178)
e6.place(x=140,y=178)
e7.place(x=158,y=178)
e8.place(x=176,y=178)
e9.place(x=194,y=178)

f1.place(x=50,y=205)
f2.place(x=68,y=205)
f3.place(x=86,y=205)
f4.place(x=104,y=205)
f5.place(x=122,y=205)
f6.place(x=140,y=205)
f7.place(x=158,y=205)
f8.place(x=176,y=205)
f9.place(x=194,y=205)

g1.place(x=50,y=232)
g2.place(x=68,y=232)
g3.place(x=86,y=232)
g4.place(x=104,y=232)
g5.place(x=122,y=232)
g6.place(x=140,y=232)
g7.place(x=158,y=232)
g8.place(x=176,y=232)
g9.place(x=194,y=232)

h1.place(x=50,y=259)
h2.place(x=68,y=259)
h3.place(x=86,y=259)
h4.place(x=104,y=259)
h5.place(x=122,y=259)
h6.place(x=140,y=259)
h7.place(x=158,y=259)
h8.place(x=176,y=259)
h9.place(x=194,y=259)

i1.place(x=50,y=286)
i2.place(x=68,y=286)
i3.place(x=86,y=286)
i4.place(x=104,y=286)
i5.place(x=122,y=286)
i6.place(x=140,y=286)
i7.place(x=158,y=286)
i8.place(x=176,y=286)
i9.place(x=194,y=286)

j1.place(x=50,y=313)
j2.place(x=68,y=313)
j3.place(x=86,y=313)
j4.place(x=104,y=313)
j5.place(x=122,y=313)
j6.place(x=140,y=313)
j7.place(x=158,y=313)
j8.place(x=176,y=313)
j9.place(x=194,y=313)


a11=Button(ventana,text="",command=lambda:funcion(1,1,91),bg="cyan",width=1,height=1)
listabotones.append(a11)
a22=Button(ventana,text="",command=lambda:funcion(1,2,92),bg="cyan",width=1,height=1)
listabotones.append(a22)
a33=Button(ventana,text="",command=lambda:funcion(1,3,93),bg="cyan",width=1,height=1)
listabotones.append(a33)
a44=Button(ventana,text="",command=lambda:funcion(1,4,94),bg="cyan",width=1,height=1)
listabotones.append(a44)
a55=Button(ventana,text="",command=lambda:funcion(1,5,95),bg="cyan",width=1,height=1)
listabotones.append(a55)
a66=Button(ventana,text="",command=lambda:funcion(1,6,96),bg="cyan",width=1,height=1)
listabotones.append(a66)
a77=Button(ventana,text="",command=lambda:funcion(1,7,97),bg="cyan",width=1,height=1)
listabotones.append(a77)
a88=Button(ventana,text="",command=lambda:funcion(1,8,98),bg="cyan",width=1,height=1)
listabotones.append(a88)
a99=Button(ventana,text="",command=lambda:funcion(1,9,99),bg="cyan",width=1,height=1)
listabotones.append(a99)

b11=Button(ventana,text="",command=lambda:funcion(2,1,100),bg="cyan",width=1,height=1)
listabotones.append(b11)
b22=Button(ventana,text="",command=lambda:funcion(2,2,101),bg="cyan",width=1,height=1)
listabotones.append(b22)
b33=Button(ventana,text="",command=lambda:funcion(2,3,102),bg="cyan",width=1,height=1)
listabotones.append(b33)
b44=Button(ventana,text="",command=lambda:funcion(2,4,103),bg="cyan",width=1,height=1)
listabotones.append(b44)
b55=Button(ventana,text="",command=lambda:funcion(2,5,104),bg="cyan",width=1,height=1)
listabotones.append(b55)
b66=Button(ventana,text="",command=lambda:funcion(2,6,105),bg="cyan",width=1,height=1)
listabotones.append(b66)
b77=Button(ventana,text="",command=lambda:funcion(2,7,106),bg="cyan",width=1,height=1)
listabotones.append(b77)
b88=Button(ventana,text="",command=lambda:funcion(2,8,107),bg="cyan",width=1,height=1)
listabotones.append(b88)
b99=Button(ventana,text="",command=lambda:funcion(2,9,108),bg="cyan",width=1,height=1)
listabotones.append(b99)

c11=Button(ventana,text="",command=lambda:funcion(3,1,109),bg="cyan",width=1,height=1)
listabotones.append(c11)
c22=Button(ventana,text="",command=lambda:funcion(3,2,110),bg="cyan",width=1,height=1)
listabotones.append(c22)
c33=Button(ventana,text="",command=lambda:funcion(3,3,111),bg="cyan",width=1,height=1)
listabotones.append(c33)
c44=Button(ventana,text="",command=lambda:funcion(3,4,112),bg="cyan",width=1,height=1)
listabotones.append(c44)
c55=Button(ventana,text="",command=lambda:funcion(3,5,113),bg="cyan",width=1,height=1)
listabotones.append(c55)
c66=Button(ventana,text="",command=lambda:funcion(3,6,114),bg="cyan",width=1,height=1)
listabotones.append(c66)
c77=Button(ventana,text="",command=lambda:funcion(3,7,115),bg="cyan",width=1,height=1)
listabotones.append(c77)
c88=Button(ventana,text="",command=lambda:funcion(3,8,116),bg="cyan",width=1,height=1)
listabotones.append(c88)
c99=Button(ventana,text="",command=lambda:funcion(3,9,117),bg="cyan",width=1,height=1)
listabotones.append(c99)

d11=Button(ventana,text="",command=lambda:funcion(4,1,118),bg="cyan",width=1,height=1)
listabotones.append(d11)
d22=Button(ventana,text="",command=lambda:funcion(4,2,119),bg="cyan",width=1,height=1)
listabotones.append(d22)
d33=Button(ventana,text="",command=lambda:funcion(4,3,120),bg="cyan",width=1,height=1)
listabotones.append(d33)
d44=Button(ventana,text="",command=lambda:funcion(4,4,121),bg="cyan",width=1,height=1)
listabotones.append(d44)
d55=Button(ventana,text="",command=lambda:funcion(4,5,122),bg="cyan",width=1,height=1)
listabotones.append(d55)
d66=Button(ventana,text="",command=lambda:funcion(4,6,123),bg="cyan",width=1,height=1)
listabotones.append(d66)
d77=Button(ventana,text="",command=lambda:funcion(4,7,124),bg="cyan",width=1,height=1)
listabotones.append(d77)
d88=Button(ventana,text="",command=lambda:funcion(4,8,125),bg="cyan",width=1,height=1)
listabotones.append(d88)
d99=Button(ventana,text="",command=lambda:funcion(4,9,126),bg="cyan",width=1,height=1)
listabotones.append(d99)

e11=Button(ventana,text="",command=lambda:funcion(5,1,127),bg="cyan",width=1,height=1)
listabotones.append(e11)
e22=Button(ventana,text="",command=lambda:funcion(5,2,128),bg="cyan",width=1,height=1)
listabotones.append(e22)
e33=Button(ventana,text="",command=lambda:funcion(5,3,129),bg="cyan",width=1,height=1)
listabotones.append(e33)
e44=Button(ventana,text="",command=lambda:funcion(5,4,130),bg="cyan",width=1,height=1)
listabotones.append(e44)
e55=Button(ventana,text="",command=lambda:funcion(5,5,131),bg="cyan",width=1,height=1)
listabotones.append(e55)
e66=Button(ventana,text="",command=lambda:funcion(5,6,132),bg="cyan",width=1,height=1)
listabotones.append(e66)
e77=Button(ventana,text="",command=lambda:funcion(5,7,133),bg="cyan",width=1,height=1)
listabotones.append(e77)
e88=Button(ventana,text="",command=lambda:funcion(5,8,134),bg="cyan",width=1,height=1)
listabotones.append(e88)
e99=Button(ventana,text="",command=lambda:funcion(5,9,135),bg="cyan",width=1,height=1)
listabotones.append(e99)

f11=Button(ventana,text="",command=lambda:funcion(6,1,136),bg="cyan",width=1,height=1)
listabotones.append(f11)
f22=Button(ventana,text="",command=lambda:funcion(6,2,137),bg="cyan",width=1,height=1)
listabotones.append(f22)
f33=Button(ventana,text="",command=lambda:funcion(6,3,138),bg="cyan",width=1,height=1)
listabotones.append(f33)
f44=Button(ventana,text="",command=lambda:funcion(6,4,139),bg="cyan",width=1,height=1)
listabotones.append(f44)
f55=Button(ventana,text="",command=lambda:funcion(6,5,140),bg="cyan",width=1,height=1)
listabotones.append(f55)
f66=Button(ventana,text="",command=lambda:funcion(6,6,141),bg="cyan",width=1,height=1)
listabotones.append(f66)
f77=Button(ventana,text="",command=lambda:funcion(6,7,142),bg="cyan",width=1,height=1)
listabotones.append(f77)
f88=Button(ventana,text="",command=lambda:funcion(6,8,143),bg="cyan",width=1,height=1)
listabotones.append(f88)
f99=Button(ventana,text="",command=lambda:funcion(6,9,144),bg="cyan",width=1,height=1)
listabotones.append(f99)

g11=Button(ventana,text="",command=lambda:funcion(7,1,145),bg="cyan",width=1,height=1)
listabotones.append(g11)
g22=Button(ventana,text="",command=lambda:funcion(7,2,146),bg="cyan",width=1,height=1)
listabotones.append(g22)
g33=Button(ventana,text="",command=lambda:funcion(7,3,147),bg="cyan",width=1,height=1)
listabotones.append(g33)
g44=Button(ventana,text="",command=lambda:funcion(7,4,148),bg="cyan",width=1,height=1)
listabotones.append(g44)
g55=Button(ventana,text="",command=lambda:funcion(7,5,149),bg="cyan",width=1,height=1)
listabotones.append(g55)
g66=Button(ventana,text="",command=lambda:funcion(7,6,150),bg="cyan",width=1,height=1)
listabotones.append(g66)
g77=Button(ventana,text="",command=lambda:funcion(7,7,151),bg="cyan",width=1,height=1)
listabotones.append(g77)
g88=Button(ventana,text="",command=lambda:funcion(7,8,152),bg="cyan",width=1,height=1)
listabotones.append(g88)
g99=Button(ventana,text="",command=lambda:funcion(7,9,153),bg="cyan",width=1,height=1)
listabotones.append(g99)

h11=Button(ventana,text="",command=lambda:funcion(8,1,154),bg="cyan",width=1,height=1)
listabotones.append(h11)
h22=Button(ventana,text="",command=lambda:funcion(8,2,155),bg="cyan",width=1,height=1)
listabotones.append(h22)
h33=Button(ventana,text="",command=lambda:funcion(8,3,156),bg="cyan",width=1,height=1)
listabotones.append(h33)
h44=Button(ventana,text="",command=lambda:funcion(8,4,157),bg="cyan",width=1,height=1)
listabotones.append(h44)
h55=Button(ventana,text="",command=lambda:funcion(8,5,158),bg="cyan",width=1,height=1)
listabotones.append(h55)
h66=Button(ventana,text="",command=lambda:funcion(8,6,159),bg="cyan",width=1,height=1)
listabotones.append(h66)
h77=Button(ventana,text="",command=lambda:funcion(8,7,160),bg="cyan",width=1,height=1)
listabotones.append(h77)
h88=Button(ventana,text="",command=lambda:funcion(8,8,161),bg="cyan",width=1,height=1)
listabotones.append(h88)
h99=Button(ventana,text="",command=lambda:funcion(8,9,162),bg="cyan",width=1,height=1)
listabotones.append(h99)

i11=Button(ventana,text="",command=lambda:funcion(9,1,163),bg="cyan",width=1,height=1)
listabotones.append(i11)
i22=Button(ventana,text="",command=lambda:funcion(9,2,164),bg="cyan",width=1,height=1)
listabotones.append(i22)
i33=Button(ventana,text="",command=lambda:funcion(9,3,165),bg="cyan",width=1,height=1)
listabotones.append(i33)
i44=Button(ventana,text="",command=lambda:funcion(9,4,166),bg="cyan",width=1,height=1)
listabotones.append(i44)
i55=Button(ventana,text="",command=lambda:funcion(9,5,167),bg="cyan",width=1,height=1)
listabotones.append(i55)
i66=Button(ventana,text="",command=lambda:funcion(9,6,168),bg="cyan",width=1,height=1)
listabotones.append(i66)
i77=Button(ventana,text="",command=lambda:funcion(9,7,169),bg="cyan",width=1,height=1)
listabotones.append(i77)
i88=Button(ventana,text="",command=lambda:funcion(9,8,170),bg="cyan",width=1,height=1)
listabotones.append(i88)
i99=Button(ventana,text="",command=lambda:funcion(9,9,171),bg="cyan",width=1,height=1)
listabotones.append(i99)

j11=Button(ventana,text="",command=lambda:funcion(10,1,172),bg="cyan",width=1,height=1)
listabotones.append(j11)
j22=Button(ventana,text="",command=lambda:funcion(10,2,173),bg="cyan",width=1,height=1)
listabotones.append(j22)
j33=Button(ventana,text="",command=lambda:funcion(10,3,174),bg="cyan",width=1,height=1)
listabotones.append(j33)
j44=Button(ventana,text="",command=lambda:funcion(10,4,175),bg="cyan",width=1,height=1)
listabotones.append(j44)
j55=Button(ventana,text="",command=lambda:funcion(10,5,176),bg="cyan",width=1,height=1)
listabotones.append(j55)
j66=Button(ventana,text="",command=lambda:funcion(10,6,177),bg="cyan",width=1,height=1)
listabotones.append(j66)
j77=Button(ventana,text="",command=lambda:funcion(10,7,178),bg="cyan",width=1,height=1)
listabotones.append(j77)
j88=Button(ventana,text="",command=lambda:funcion(10,8,179),bg="cyan",width=1,height=1)
listabotones.append(j88)
j99=Button(ventana,text="",command=lambda:funcion(10,9,180),bg="cyan",width=1,height=1)
listabotones.append(j99)

a11.place(x=250,y=70)
a22.place(x=268,y=70)
a33.place(x=286,y=70)
a44.place(x=304,y=70)
a55.place(x=322,y=70)
a66.place(x=340,y=70)
a77.place(x=358,y=70)
a88.place(x=376,y=70)
a99.place(x=394,y=70)

b11.place(x=250,y=97)
b22.place(x=268,y=97)
b33.place(x=286,y=97)
b44.place(x=304,y=97)
b55.place(x=322,y=97)
b66.place(x=340,y=97)
b77.place(x=358,y=97)
b88.place(x=376,y=97)
b99.place(x=394,y=97)

c11.place(x=250,y=124)
c22.place(x=268,y=124)
c33.place(x=286,y=124)
c44.place(x=304,y=124)
c55.place(x=322,y=124)
c66.place(x=340,y=124)
c77.place(x=358,y=124)
c88.place(x=376,y=124)
c99.place(x=394,y=124)

d11.place(x=250,y=151)
d22.place(x=268,y=151)
d33.place(x=286,y=151)
d44.place(x=304,y=151)
d55.place(x=322,y=151)
d66.place(x=340,y=151)
d77.place(x=358,y=151)
d88.place(x=376,y=151)
d99.place(x=394,y=151)

e11.place(x=250,y=178)
e22.place(x=268,y=178)
e33.place(x=286,y=178)
e44.place(x=304,y=178)
e55.place(x=322,y=178)
e66.place(x=340,y=178)
e77.place(x=358,y=178)
e88.place(x=376,y=178)
e99.place(x=394,y=178)

f11.place(x=250,y=205)
f22.place(x=268,y=205)
f33.place(x=286,y=205)
f44.place(x=304,y=205)
f55.place(x=322,y=205)
f66.place(x=340,y=205)
f77.place(x=358,y=205)
f88.place(x=376,y=205)
f99.place(x=394,y=205)

g11.place(x=250,y=232)
g22.place(x=268,y=232)
g33.place(x=286,y=232)
g44.place(x=304,y=232)
g55.place(x=322,y=232)
g66.place(x=340,y=232)
g77.place(x=358,y=232)
g88.place(x=376,y=232)
g99.place(x=394,y=232)

h11.place(x=250,y=259)
h22.place(x=268,y=259)
h33.place(x=286,y=259)
h44.place(x=304,y=259)
h55.place(x=322,y=259)
h66.place(x=340,y=259)
h77.place(x=358,y=259)
h88.place(x=376,y=259)
h99.place(x=394,y=259)

i11.place(x=250,y=286)
i22.place(x=268,y=286)
i33.place(x=286,y=286)
i44.place(x=304,y=286)
i55.place(x=322,y=286)
i66.place(x=340,y=286)
i77.place(x=358,y=286)
i88.place(x=376,y=286)
i99.place(x=394,y=286)

j11.place(x=250,y=313)
j22.place(x=268,y=313)
j33.place(x=286,y=313)
j44.place(x=304,y=313)
j55.place(x=322,y=313)
j66.place(x=340,y=313)
j77.place(x=358,y=313)
j88.place(x=376,y=313)
j99.place(x=394,y=313)


for i in listabotones:
    i.config(state=DISABLED)



tabla=Treeview(ventana,columns=('#1','#2','#3','#4'))

tabla.heading("#0",text="Numero de juego")
tabla.heading("#1",text="Jugador 1")
tabla.heading("#2",text="Puntaje")
tabla.heading("#3",text="Jugador 2")
tabla.heading("#4",text="Puntaje 2")

tabla.column("#0",width=100)
tabla.column("#1",width=200)
tabla.column("#2",width=100)
tabla.column("#3",width=200)
tabla.column("#4",width=100)
tabla.place(x=3,y=450)

btntabla=Button(ventana,text='Tabla',bg="#2E6F78",font=("Orbitron",12),command=lambda:listar())
btntabla.place(x=430,y=380)
ventana.mainloop()
