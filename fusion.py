from tkinter import *
from vaisseau import *
from projectile import *
from protection import *
import Fenetre as fen





ma_fenetre=fen.Fenetre(1900,1008,15)
vaisseau=Vaisseau(800,900,20)

ma_fenetre.creer_fenetre(vaisseau.TailleVaisseau,vaisseau.POSX,vaisseau.POSY,Tk,Canvas,Button)
#je créer ma fenêtre dans ma classe, et la stocke dans ZoneDeJeu

ma_fenetre.ZoneDeJeu.focus_force()

ma_fenetre.ZoneDeJeu.bind('<Key>',ma_fenetre.Clavier)
ma_fenetre.ZoneDeJeu.bind('<Button-1>',ma_fenetre.creer_projectile)

p2=Protection(20,40,18)
p3=Protection(40,60,18)
liste_protection=[p2,p3]
""" for p in liste_protection:
    ma_fenetre.creer_rectangle(p.positionx,p.positiony,p.taille) """

ma_fenetre.forme1(60,700,18,6,2,ma_fenetre)
projectile=Projectile(vaisseau.POSX+vaisseau.TailleVaisseau,vaisseau.POSY,15,15)

ma_fenetre.ZoneDeJeu.after(20,ma_fenetre.bouger,projectile,ma_fenetre)


ma_fenetre.mw.mainloop()

























