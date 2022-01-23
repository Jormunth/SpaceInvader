# gere toutes les fonctions liees au samourai qui sont celle de son nottament celle de son mouvement et la creation de ses projectile
# Mathieu Zeman / Gaelle Leroux
# realise entre decembre 2021 et janvier 2022 

from tkinter import *
from PIL import Image, ImageTk
import projectile as project
class Vaisseau:
    def __init__(self,monde,fenetre,position_x,position_y,taille_vaisseau,vaisseau,LARGEUR,HAUTEUR,enemy_list_object,enemy_list_image,controle_up,controle_down,controle_left,controle_right,controle_shot,is_running):
        self.fenetre=fenetre
        self.position_x=position_x
        self.position_y=position_y
        self.taille_vaisseau=taille_vaisseau
        self.vaisseau=vaisseau
        self.LARGEUR = LARGEUR
        self.HAUTEUR = HAUTEUR
        self.projectile_list = []
        self.monde=monde
        self.is_running=is_running
        self.enemy_list_object=enemy_list_object
        self.enemy_list_image=enemy_list_image
        self.controle_up=controle_up
        self.controle_down=controle_down
        self.controle_left=controle_left
        self.controle_right=controle_right
        self.controle_shot=controle_shot

    def set_is_running(self):
        # met a jour l'etat de is_running afin de terminer la partie
        # entrée : Aucune
        # sortie : Aucune
        self.is_running = False

    def deplacer(self,u,v):
        # fonction  qui met a jour les positions x et y du samourai
        # entrée : de combien c'est deplacer en y et x le samourai
        # sortie : Aucune
        self.position_x=self.position_x+u
        self.position_y=self.position_y+v
    
    def clavier(self,event):
        # la fonction regarde sur quelle touche le joueur a appuyé et appelle la fonction qui déplacera le samoura avec les parametres de mouvement 
        # entrée : la touche sur laquelle le joueur a cliquée
        # sortie : Aucune
        u=0
        v=0
        coords_vaisseau=self.fenetre.ZoneDeJeu.coords(self.vaisseau)
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
        self.fenetre.ZoneDeJeu.move(self.vaisseau,u,v)
    
    
    def creer_projectile(self,event):
        # focntion qui crée des projectiles des que la touche correspondantes est presse
        # entrée : la touche sur lauelle le joueur a appuyé
        # sortie : Aucune
        coords_vaisseau=self.fenetre.ZoneDeJeu.coords(self.vaisseau)
        projectile=project.Projectile(self,self.monde,self.fenetre,(coords_vaisseau[0]+coords_vaisseau[0])/2,coords_vaisseau[1],20,20,self.is_running)
        
        projectile_last=self.fenetre.ZoneDeJeu.create_image(projectile.px,projectile.py, image = self.fenetre.LOADDED_KATANA)
        self.projectile_list.append(projectile_last)
        projectile.bouger(projectile_last,self.projectile_list)


    def get_position_x(self):
        # retourne la position en x du samourai
        # entrée : Aucune
        # sortie : la position en x du samourai
        return self.position_x

    def get_position_y(self):
        # retourne la position en y du samourai
        # entrée : Aucune
        # sortie : la position en y du samourai
        return self.position_y

    def get_taille(self):
        # retourne la taille du samourai
        # entrée : Aucune
        # sortie : la taille du samourai
        return self.taille_vaisseau

    def get_liste_katana(self):
        # retourne la liste des projectiles lancee par le samourai
        # entrée : Aucune
        # sortie : la la liste des projectile lancee par le samourai
        return self.projectile_list

    def maj_katana(self,x):
        # met a jour la liste des projectiles du samourai
        # entrée : la liste des projectiles du samourai
        # sortie : Aucune
        l=self.projectile_list.remove(x)
        self.projectile_list=l