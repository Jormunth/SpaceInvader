from tkinter import *
import math,random



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




Largeur = 1600
Hauteur = 300
Rayon = 30

X = Largeur/2
Y = Hauteur/2

PX=X
PY=Y

vitesse = 10

DX = vitesse
DY = 30*2

Enemy = ZoneDeJeu.create_oval(X-Rayon, Y-Rayon, X+Rayon, Y+Rayon, fill="red", outline="black", width=5)

ProjectileEnemy = ZoneDeJeu.create_line(X+Rayon, Y+Rayon, X+Rayon, Y+Rayon+30, width=6)

def autoTir():

    ProjectileEnemy = ZoneDeJeu.create_line(X+Rayon, Y+Rayon, X+Rayon, Y+Rayon+30, width=6)
    FrameGauche.after(1500,autoTir)
    deplacementEnemy()


def deplacementEnemy():
    global PX,PY,DX,DY,Rayon

    PY += 30

    ZoneDeJeu.coords(ProjectileEnemy, PX+Rayon, PY-Rayon, PX+Rayon, PY+Rayon+30)
    
    FrameGauche.after(20,deplacementEnemy)

def deplacement():
    global X,Y,DX,DY,Rayon,Largeur,Hauteur

    if X+Rayon+DX > Largeur:
        X= 2*(Largeur-Rayon) - X
        DX = -DX
        Y += DY

    if X-Rayon+DX < 0:
        X = 2*Rayon-X
        DX = -DX
        Y += DY

    X = X+DX

    ZoneDeJeu.coords(Enemy, X-Rayon, Y-Rayon, X+Rayon, Y+Rayon)
    FrameGauche.after(20,deplacement)

deplacement()
deplacementEnemy()
autoTir()

mw.mainloop()
 
