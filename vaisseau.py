from tkinter import *
from PIL import Image, ImageTk
import projectile as project
class Vaisseau:
    def __init__(self,monde,fenetre,POSX,POSY,TailleVaisseau,Vaisseau,LARGEUR,HAUTEUR,enemy_list_object,enemy_list_image,controle_up,controle_down,controle_left,controle_right,controle_shot):
        self.fenetre=fenetre
        self.POSX=POSX
        self.POSY=POSY
        self.TailleVaisseau=TailleVaisseau
        self.Vaisseau=Vaisseau
        self.LARGEUR = LARGEUR
        self.HAUTEUR = HAUTEUR
        self.projectile_list = []
        self.monde=monde
        self.enemy_list_object=enemy_list_object
        self.enemy_list_image=enemy_list_image
        self.controle_up=controle_up
        self.controle_down=controle_down
        self.controle_left=controle_left
        self.controle_right=controle_right
        self.controle_shot=controle_shot


    def deplacer(self,u,v):
        self.POSX=self.POSX+u
        self.POSY=self.POSY+v
    
    def Clavier(self,event):
        u=0
        v=0
        coords_vaisseau=self.fenetre.ZoneDeJeu.coords(self.Vaisseau)
        if event.keysym==self.controle_up and coords_vaisseau[1]>0:
            u=0
            v=-20
        if event.keysym==self.controle_down and coords_vaisseau[1]<self.HAUTEUR+10:
            u=0
            v=20
        if event.keysym==self.controle_left and coords_vaisseau[0]>0:
            u=-20
            v=0
        if event.keysym==self.controle_right and coords_vaisseau[0]<self.LARGEUR:
            u=20
            v=0
        self.deplacer(u,v)
        self.fenetre.ZoneDeJeu.move(self.Vaisseau,u,v)
    
    
    def creer_projectile(self,event):
        coords_vaisseau=self.fenetre.ZoneDeJeu.coords(self.Vaisseau)
        projectile=project.Projectile(self,self.monde,self.fenetre,(coords_vaisseau[0]+coords_vaisseau[0])/2,coords_vaisseau[1],20,20)
        
        Projectilelast=self.fenetre.ZoneDeJeu.create_image(projectile.px,projectile.py, image = self.fenetre.loaddedKatana)
        self.projectile_list.append(Projectilelast)
        projectile.bouger(Projectilelast,self.projectile_list)


    def getPosX(self):
        return self.POSX

    def getPosY(self):
        return self.POSY

    def getTaille(self):
        return self.TailleVaisseau

    def getListeKatana(self):
        return self.projectile_list

    def maj_katana(self,x):
        l=self.projectile_list.remove(x)
        self.projectile_list=l