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

ProjectileEnemy = []




class Enemy:
    def __init__(self, tag, posX, posY,ZoneDeJeu):
        self.tag=tag
        self.posX=posX
        self.posY=posY
        self.Enemy=ZoneDeJeu.create_oval(X-Rayon, Y-Rayon, X+Rayon, Y+Rayon, fill="red", outline="black", width=5)
        self.ZoneDeJeu = ZoneDeJeu


    def deplacementEnemy(self,posX,posY,DX,DY,Rayon,Largeur,Hauteur):
    
        if posX+Rayon+DX > Largeur:
            posX= 2*(Largeur-Rayon) - posX
            DX = -DX
            posY += DY

        if X-Rayon+DX < 0:
            posX = 2*Rayon-posX
            DX = -DX
            posY += DY

        posX = posX+DX

        ZoneDeJeu.coords(Enemy, posX-Rayon, posY-Rayon, posX+Rayon, posY+Rayon)

        FrameGauche.after(20, self.deplacementEnemy, posX , posY,DX,DY,Rayon,Largeur,Hauteur)

my_enemy = Enemy(1, 200, 300, ZoneDeJeu)


def autoTir(X, Y, PX,PY,DX,DY):
    coordsEnemy = ZoneDeJeu.coords(Enemy)
    X2 = (coordsEnemy[0]+coordsEnemy[2])/2
    Y2 = (coordsEnemy[1]+coordsEnemy[3])/2

    ProjectileEnemylast=ZoneDeJeu.create_line(X2+Rayon, Y2+Rayon, X2+Rayon, Y2+Rayon+30, width=6)
    ProjectileEnemy.append(ProjectileEnemylast)

    deplacementProjectEautoTir(ProjectileEnemylast,PX,PY,Rayon)
    FrameGauche.after(1500,autoTir,X2,Y2,PX,PY,DX,DY)


def deplacementProjectEautoTir(ProjectileEnemylast,PX,PY,Rayon):

    PY += 30
    ZoneDeJeu.move(ProjectileEnemylast, 0, 20)
    
    FrameGauche.after(20,deplacementProjectEautoTir,ProjectileEnemylast,PX,PY,Rayon)





deplacementEnemy(X,Y,DX,DY,Rayon,Largeur,Hauteur)
autoTir(X, Y, PX,PY,DX,DY)

mw.mainloop()


