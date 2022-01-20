
from tkinter import *
from PIL import Image, ImageTk

class Projectile:
    def __init__(self,vaisseau,monde,fenetre,px,py,rayon,vitesse):
        self.monde=monde
        self.fenetre=fenetre
        self.py=py
        self.px=px
        self.rayon=rayon
        self.vitesse=vitesse
        self.vaisseau=vaisseau


    def deplacementProjectEautoTir(self,projectilelast,coordsEnemyY,list_projectile,HAUTEUR):


        self.fenetre.ZoneDeJeu.move(projectilelast,0,20)
        self.fenetre.FrameGauche.after(20,self.deplacementProjectEautoTir,projectilelast,coordsEnemyY,list_projectile,HAUTEUR)


    def bouger(self,projectilelast,difficulty):


        self.fenetre.ZoneDeJeu.move(projectilelast,0,-20)
        self.fenetre.ZoneDeJeu.after(100,self.bouger,projectilelast,difficulty)  