# gere toutes  les fonctions liees qux protections dont leur creations
# Mathieu Zeman / Gaelle Leroux
# realise entre decembre 2021 et janvier 2022 

from tkinter import *
from PIL import Image, ImageTk

class Protection:
    def __init__(self,fenetre,positionx,positiony):
        self.fenetre=fenetre
        self.positionx=positionx
        self.positiony=positiony
        self.rectangle = []



    def creer_rectangle(self,px,py,taille):
        # fonction qui creer les barrieres
        # entree : Aucune
        # sortie : Aucune

        self.loadBarriere = Image.open("image/Fence.png")
        self.loaddedBarriere =ImageTk.PhotoImage(self.loadBarriere)
        BarriereLast=self.fenetre.ZoneDeJeu.create_image(px,py, image = self.fenetre.lOADDED_BARRIERE)
        self.rectangle.append(BarriereLast)




    def forme1(self,x,y,taille_carré,nombre_carréx,nombre_carré_y,ma_fenetre):
        # fonction qui creer une forme de protection 
        # entree : Aucune
        # sortie : Aucune
        for i in range(nombre_carréx):
            for t in range(nombre_carré_y):
                self.creer_rectangle(x+i*2*taille_carré,y+t*2*taille_carré,taille_carré)

    def get_rectangle(self):
        # fonction qui renvoie la liste des protections
        # entree : Aucune
        # sortie : la liste des protections
        self.rectangle
        return self.rectangle
        

    def maj_rectangle(self,x):
        # fonction qui met a jour la liste des protections
        # entree : l'element a supprimer 
        # sortie : Aucune
        l=self.rectangle.remove(x)
        self.rectangle=l