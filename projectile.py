# gere toutes les fonctions liees aux projectile qui sont celle de son celle de leur mouvement
# Mathieu Zeman / Gaelle Leroux
# realise entre decembre 2021 et janvier 2022 

from tkinter import *
from PIL import Image, ImageTk

class Projectile:
    def __init__(self,vaisseau,monde,fenetre,px,py,rayon,vitesse,is_running):
        self.monde=monde
        self.fenetre=fenetre
        self.py=py
        self.px=px
        self.rayon=rayon
        self.vitesse=vitesse
        self.vaisseau=vaisseau
        self.is_running=is_running


    def set_is_running(self):
        # met a jour l'etat de is_running afin de terminer la partie
        # entrée : Aucune
        # sortie : Aucune
        self.is_running = False

    def deplacement_projectile_auto_tir(self,projectile_last,coordsEnemyY,list_projectile,HAUTEUR):
        # fonction aui deplaces les shuriken de l'ennemies
        # entree: Aucune
        # sortie : Aucune
        coords_tir=self.fenetre.ZoneDeJeu.coords(projectile_last)
        if len(coords_tir)!=0:
            if coords_tir[1] - 15 < HAUTEUR:
                self.fenetre.ZoneDeJeu.move(projectile_last,0,20)
                if self.is_running == True:
                    self.fenetre.FrameGauche.after(20,self.deplacement_projectile_auto_tir,projectile_last,coordsEnemyY,list_projectile,HAUTEUR)
            else:
                self.fenetre.ZoneDeJeu.delete(projectile_last)
                if projectile_last in list_projectile:
                    list_projectile.remove(projectile_last)
        


    def bouger(self,projectile_last,difficulty):
        # fonction aui deplaces les katana du joueur 
        # entree: Aucune
        # sortie : Aucune
        coords_projectile=self.fenetre.ZoneDeJeu.coords(projectile_last)
        if len(coords_projectile)!=0:
            if coords_projectile[1]>0:
                    self.fenetre.ZoneDeJeu.move(projectile_last,0,-20)
                    if self.is_running == True:
                        self.fenetre.ZoneDeJeu.after(100,self.bouger,projectile_last,difficulty)  
            else:
                self.fenetre.ZoneDeJeu.delete(projectile_last)

        
        