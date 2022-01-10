from tkinter import *
import math,random
import time
import os


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




LARGEUR = 1600
HAUTEUR = 300
RAYON = 30

X = LARGEUR/2
Y = HAUTEUR/2

PX=X
PY=Y

vitesse = 10

DX = vitesse
DY = 30*2

Enemy = ZoneDeJeu.create_oval(X-RAYON, Y-RAYON, X+RAYON, Y+RAYON, fill="red", outline="black", width=5)

"""
img = PhotoImage(file="image/Ninja/animation/runRight_1.gif", format="gif -index 1")"""
""" Enemy=ZoneDeJeu.create_image(X,Y, image = img) """
"""
frameCnt = 5
immmage = [PhotoImage(file='image/Ninja/animation/runRight_1.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]
Enemy=ZoneDeJeu.create_image(X,Y, image = immmage[0])"""
""" 
def update(ind):

    frame = Enemy[1]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    FrameGauche.after(100, update, 1)

    Enemy=ZoneDeJeu.create_image(X,Y, image = immmage[0])


label = Label(FrameGauche)
label.pack() """


ProjectileEnemy = []

def autoTir(X, Y, PX,PY,DX,DY):
    coordsEnemy = ZoneDeJeu.coords(Enemy)
    X2 = coordsEnemy[0]
    Y2 = coordsEnemy[1]

    ProjectileEnemylast=ZoneDeJeu.create_line(X2+RAYON, Y2+RAYON, X2+RAYON, Y2+RAYON+30, width=6)
    ProjectileEnemy.append(ProjectileEnemylast)

    deplacementProjectEautoTir(ProjectileEnemylast,PX,PY,RAYON)
    FrameGauche.after(1500,autoTir,X2,Y2,PX,PY,DX,DY)


def deplacementProjectEautoTir(ProjectileEnemylast,PX,PY,RAYON):

    PY += 30
    ZoneDeJeu.move(ProjectileEnemylast, 0, 20)
    
    FrameGauche.after(20,deplacementProjectEautoTir,ProjectileEnemylast,PX,PY,RAYON)





def deplacementEnemy(X,Y,DX,DY,LARGEUR):
    
    X += DX
    DY = 0

    if X > LARGEUR:
        X= 2*(LARGEUR)-X
        DX = -DX
        DY = 60

    if X < 0:
        X = -X
        DX = -DX
        DY = 60

        

    ZoneDeJeu.move(Enemy, DX, DY)
    FrameGauche.after(20,deplacementEnemy,X,Y,DX,DY,LARGEUR)

""" 
    frame = immmage[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    Enemy=ZoneDeJeu.create_image(800,475, image = frame) """

    

deplacementEnemy(X,Y,DX,DY,LARGEUR)
autoTir(X, Y, PX,PY,DX,DY)


mw.mainloop()


