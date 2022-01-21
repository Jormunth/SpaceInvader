
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
        #self.monde.collision_projectilee_vaisseau(projectilelast)
        coords_tir=self.fenetre.ZoneDeJeu.coords(projectilelast)
        if len(coords_tir)!=0:
            if coords_tir[1] - 15 < HAUTEUR:
                self.fenetre.ZoneDeJeu.move(projectilelast,0,20)
                self.fenetre.FrameGauche.after(20,self.deplacementProjectEautoTir,projectilelast,coordsEnemyY,list_projectile,HAUTEUR)
            else:
                self.fenetre.ZoneDeJeu.delete(projectilelast)
                if projectilelast in list_projectile:
                    list_projectile.remove(projectilelast)
        


    def bouger(self,projectilelast,difficulty):
        coords_projectile=self.fenetre.ZoneDeJeu.coords(projectilelast)
        if len(coords_projectile)!=0:
            if coords_projectile[1]>0:
                    self.fenetre.ZoneDeJeu.move(projectilelast,0,-20)
                    self.fenetre.ZoneDeJeu.after(100,self.bouger,projectilelast,difficulty)  
            else:
                self.fenetre.ZoneDeJeu.delete(projectilelast)

        
        