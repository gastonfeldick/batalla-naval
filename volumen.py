from tkinter import *
import pygame



def musica(value):
    print("")
    res=volumen.get()/100
    pygame.mixer.music.set_volume(res)
    
    print("volumen",res)

ventana=Tk()

ventana.geometry("700x450")
pygame.mixer.init()
pygame.mixer.music.load("CORTINA2.WAV")
pygame.mixer.music.play(-1)
volumen=IntVar(value=50)
musica(1)

scale=Scale(ventana,orient="vertical",from_=100,to=0,variable=volumen,command=musica)
scale.place(x=500,y=20, height = 300,width = 400 )



ventana.mainloop()