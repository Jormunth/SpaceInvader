from tkinter import *
from vaisseau import *
from projectile import *
from protection import *
import classTkinter as fen



ma_fenetre=fen.Tkinter(1600,950,15)
vaisseau=Vaisseau(800,900,20)

ma_fenetre.creer_fenetre(Tk,Canvas,Button)
#je créer ma fenêtre dans ma classe, et la stocke dans ZoneDeJeu
ma_fenetre.create_background( )
ma_fenetre.ZoneDeJeu.focus_force()
ma_fenetre.creerVaisseau(vaisseau.TailleVaisseau,vaisseau.POSX,vaisseau.POSY,)

ma_fenetre.ZoneDeJeu.bind('<Key>',ma_fenetre.Clavier)
ma_fenetre.ZoneDeJeu.bind('<Button-1>',ma_fenetre.creer_projectile)

p2=Protection(20,40,18)
p3=Protection(40,60,18)
liste_protection=[p2,p3]
""" for p in liste_protection:
    ma_fenetre.creer_rectangle(p.positionx,p.positiony,p.taille) """

ma_fenetre.forme1(60,700,18,33,2,ma_fenetre)
projectile=Projectile(vaisseau.POSX+vaisseau.TailleVaisseau,vaisseau.POSY,15,15)



difficulty = 6
vitesse = 7+(difficulty/2)
DY = 43+(difficulty*4)

ma_fenetre.ZoneDeJeu.after(20,ma_fenetre.bouger,projectile,ma_fenetre,difficulty)

ma_fenetre.creerEnemy(difficulty,DY)
ma_fenetre.deplacementEnemy(vitesse,DY,difficulty)
ma_fenetre.autoTir(difficulty,ma_fenetre)

ma_fenetre.mw.mainloop()




