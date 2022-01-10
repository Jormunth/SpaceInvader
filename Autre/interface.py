from tkinter import *
import random,math
import enemy as e


mw = Tk()
mw.title('Space Invader')
mw['bg']='grey'
mw.geometry('1900x1008+0+0')

Terrain = PhotoImage(file = "image/terrainFond.png")

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

ZoneDeJeu = Canvas(FrameGauche, width=1600, height =950)
ZoneDeJeu.pack(padx=10, pady=10)
ZoneDeJeu.create_image(0,0,anchor=NW,image=Terrain)


LARGEUR=1600
HAUTEUR = 300

difficulty = 5

vitesse = 7+(difficulty/2)


tag = 0
Placement = difficulty+1
DY = 43+(difficulty*4)
nbEnnemie = difficulty

frameCntEnemie = 5
imageEnnemie = [PhotoImage(file='image/Ninja/animation/runRight_2.gif',format = 'gif -index %i' %(i)) for i in range(frameCntEnemie)]

frameCntProj = 2
imageProj = [PhotoImage(file='image/Shuriken/Shuriken.gif',format = 'gif -index %i' %(i)) for i in range(frameCntProj)]


myEnemyList=[]
myEnemy = []

while nbEnnemie >= 1:
    
    tag += 1
    X = (LARGEUR/Placement)*tag
    Y = HAUTEUR/2

    myEnemyList.append(e.Enemy(tag, vitesse, X, Y, DY))
    myEnemy.append(ZoneDeJeu.create_image(X,Y, image = imageEnnemie[0]))

    nbEnnemie -= 1




def deplacementEnemy(myEnemyList,myEnemy,vitesse,DY,LARGEUR,difficulty):
    
    DX = vitesse
    DY = 0

    XtremG = myEnemyList[0].getPosX()
    XtremD = myEnemyList[-1].getPosX()

    XtremG += DX
    XtremD += DX    


    if XtremD + 20 > LARGEUR:
        XtremD= 2*(LARGEUR) - XtremD
        vitesse = -DX
        DY = 60

    if XtremG -20 < 0:
        XtremG = -XtremG
        vitesse = -DX
        DY = 60

    for i,val in enumerate(myEnemy):
        ZoneDeJeu.move(myEnemy[i],DX,DY)
        myEnemyList[i].deplacer(myEnemyList[i].getPosX()+DX,myEnemyList[i].getPosY()+DY)


    FrameGauche.after(20,deplacementEnemy,myEnemyList,myEnemy,vitesse,DY,LARGEUR,difficulty)





ProjectileEnemy = []

def autoTir(difficulty,ProjectileEnemy):

    max = len(myEnemy)-1

    rand=random.randint(0,max)

    coordsEnemyX = myEnemyList[rand].getPosX()
    coordsEnemyY = myEnemyList[rand].getPosY()
    ProjectileEnemylast=ZoneDeJeu.create_image(coordsEnemyX,coordsEnemyY, image = imageProj[0])
    """ ProjectileEnemylast=ZoneDeJeu.create_line(coordsEnemyX, coordsEnemyY, coordsEnemyX, coordsEnemyY+30, width=6) """
    ProjectileEnemy.append(ProjectileEnemylast)

    FrameGauche.after(750,autoTir,difficulty,ProjectileEnemy)
    deplacementProjectEautoTir(ProjectileEnemylast,coordsEnemyY)


def deplacementProjectEautoTir(ProjectileEnemylast,coordsEnemyY):

    ZoneDeJeu.move(ProjectileEnemylast, 0, 20)
    
    FrameGauche.after(20,deplacementProjectEautoTir,ProjectileEnemylast,coordsEnemyY)



deplacementEnemy(myEnemyList,myEnemy,vitesse,DY,LARGEUR,difficulty)
autoTir(difficulty,ProjectileEnemy)










mw.mainloop()