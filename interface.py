from tkinter import *
import math,random
from  import Enemy

def deplacer(event):
    touche=event.keysym  
    if touche =='<RIGHT>':
        my_enemy.deplacer(my_enemy.posX + 20, my_enemy.posY)
    if touche =='<LEFT>':
        my_enemy.deplacer(my_enemy.posX - 20, my_enemy.posY)
     #mettre à jour l'image


mw = Tk()
mw.title('Space Invader')
mw['bg']='grey'
mw.geometry('1900x1008+0+0')



FrameDroit = Frame(mw)
FrameDroit.pack(side="right")

ButtonJouer = Button(FrameDroit, text="Jouer", height=5, width=30,)
ButtonJouer.pack(pady=50)

ButtonParametre = Button(FrameDroit, text="Paramètre", height=5, width=30, command=print("paramètre"))
ButtonParametre.pack(pady=50)

ButtonQuitter = Button(FrameDroit, text="Quitter", height=5, width=30, command=mw.destroy)
ButtonQuitter.pack(side='bottom', pady=50)

FrameGauche = Frame(mw)
FrameGauche.pack(side="left")

ZoneDeJeu = Canvas(FrameGauche, width=1600, height =950, bg="white")
ZoneDeJeu.pack(padx=10, pady=10)

my_enemy = Enemy(100, 100, 200, None)


Enemy = ZoneDeJeu.create_oval(my_enemy, , fill="red", outline="black", width=5)

Canevas.bind('<Left>', deplacer)
Canevas.bind('<Right>',deplacer)






mw.mainloop()