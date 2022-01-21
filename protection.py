from tkinter import *
from PIL import Image, ImageTk

class Protection:
    def __init__(self,fenetre,positionx,positiony):
        self.fenetre=fenetre
        self.positionx=positionx
        self.positiony=positiony
        self.rectangle = []



    def creer_rectangle(self,px,py,taille):
        """ self.rectangle.append(self.fenetre.ZoneDeJeu.create_rectangle(px,py,px+2*taille,py+2*taille,fill='pink')) """

        self.loadBarriere = Image.open("image/Fence.png")
        self.loaddedBarriere =ImageTk.PhotoImage(self.loadBarriere)
        BarriereLast=self.fenetre.ZoneDeJeu.create_image(px,py, image = self.fenetre.loaddedBarriere)
        self.rectangle.append(BarriereLast)




    def forme1(self,x,y,taille_carré,nombre_carréx,nombre_carré_y,ma_fenetre):
        for i in range(nombre_carréx):
            for t in range(nombre_carré_y):
                self.creer_rectangle(x+i*2*taille_carré,y+t*2*taille_carré,taille_carré)

    def getRectangle(self):
        self.rectangle
        return self.rectangle
        

    def collision_protection(self,px,py,taille,cpx,cpy):
        if cpx>=px-taille and cpx<=px+2*taille:
            if cpy<=py+taille*3:
                return(True)
        return(False)

    def maj_rectangle(self,x):
        l=self.rectangle.remove(x)
        self.rectangle=l