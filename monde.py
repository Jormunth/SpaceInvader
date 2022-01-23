# fichier qui gere tout ce qui est liee a la partie ou a au moins deux element en meme temps de la partie en cours
# Mathieu Zeman / Gaelle Leroux
# realise entre decembre 2021 et janvier 2022 

from tkinter import *
from PIL import Image, ImageTk
import random
import time
from protection import Protection
import vaisseau as V
import enemy as e
import protection as p



class Monde:

    def __init__(self,fenetre,DIFFICULTEE,DY,VITESSE,LARGEUR,HAUTEUR,CANVAS_WIDTH,CANVAS_HEIGHT,controle_up,controle_down,controle_left,controle_right,controle_shot):
        
        self.LARGEUR = LARGEUR
        self.HAUTEUR = HAUTEUR
        self.CANVAS_WIDTH = CANVAS_WIDTH
        self.CANVAS_HEIGHT = CANVAS_HEIGHT
        self.fenetre = fenetre
        self.DIFFICULTEE=DIFFICULTEE
        self.DY = DY
        self.VITESSE = VITESSE
        self.projectile=[]
        self.rectangle=[]
        self.my_enemy_list=[]
        self.my_enemy = []
        self.FrameGauche=None
        self.projectile_enemy = []
        self.vaisseau = None
        self.enemy_list_object = []
        self.enemy_list_image = []
        self.lOAD_ENEMY = None
        self.lOADDED_ENEMY = None
        self.lOAD_SUPER_ENEMY = None
        self.lOADDED_SUPER_ENEMY = None
        self.lOAD_JOUEUR = None
        self.lOADDED_JOUEURS = None
        self.lOAD_KATANA = None
        self.lOADDED_KATANA = None
        self.lOAD_BARRIERE = None
        self.lOADDED_BARRIERE = None
        self.lOAD_GAMEOVER = None
        self.RESIZED_GAMEOVER = None
        self.lOADDED_GAMEOVER = None
        self.lOAD_VICTORY = None
        self.RESIZED_VICTORY = None
        self.lOADDED_VICTORY = None
        self.niveau = 0
        self.controle_up=controle_up
        self.controle_down=controle_down
        self.controle_left=controle_left
        self.controle_right=controle_right
        self.controle_shot=controle_shot
        self.joueur=None
        self.protection_barriere=None
        self.super_enemy_list_object=None
        self.super_enemy_list_image=None
        self.is_running=True

        self.create_background_image()
        self.gere_le_monde()

    def gere_le_monde(self):
        # fonction qui lance la creation d'ennemie, du joueur, des barrieres. Elle lance les focntions de verification si le jeu doit continuer ou non
        # entre : Aucune
        # sortie : Aucune
        self.is_running = True
        self.creer_enemy()
        self.creer_joueur()
        self.creer_protection()
        self.verif_win()
        self.verif_is_running()
        
        
        aleatoire = random.randint(1,10)
        aleatoire *= 1000
        
        self.fenetre.FrameGauche.after(aleatoire,self.creer_super_enemy)


    def creer_joueur(self):
        # fonctions qui crée le joueur
        # entrée : Aucune
        # sortie : Aucune

        position_x = 800
        position_y = 850

        self.vaisseau = self.fenetre.ZoneDeJeu.create_image(position_x,position_y, image = self.lOADDED_JOUEURS)
        self.joueur = V.Vaisseau(self,self.fenetre,800,900,63,self.vaisseau,self.LARGEUR,self.HAUTEUR,self.enemy_list_object,self.enemy_list_image,self.controle_up, self.controle_down, self.controle_left, self.controle_right,self.controle_shot, self.is_running)
        self.fenetre.ZoneDeJeu.bind('<Key>',self.joueur.clavier)
        self.fenetre.ZoneDeJeu.bind(f'<{self.controle_shot}>',self.joueur.creer_projectile)
        self.collision_vaisseau()
        
    def creer_enemy(self):
        # fonctions qui ert a la creation de l'ennemie
        # entree : Aucune
        # sortie : Aucune
                
        tag = 0
        PLACEMENT = 10
        NB_ENNEMIE = self.DIFFICULTEE
        LIM_LIGNE = 5
        compteur = 0
        DELTA_Y = 1

        while NB_ENNEMIE >= 1:

            if compteur % LIM_LIGNE == 0:
                compteur = 0
                DELTA_Y += 60

            compteur += 1

            tag += 1
            X = (self.LARGEUR/PLACEMENT)*compteur
            Y = self.HAUTEUR/20 + DELTA_Y

            self.enemy_list_object.append(e.Enemy(self,self.fenetre,tag,self.VITESSE, X, Y, self.DY,self.is_running))
            self.enemy_list_image.append(self.fenetre.ZoneDeJeu.create_image(X,Y, image = self.lOADDED_ENEMY))
            NB_ENNEMIE -= 1

        self.enemy_list_object[0].maj_enemy_liste_objet(self.enemy_list_object)
        self.enemy_list_object[0].deplacement_enemy(self.VITESSE,self.DY,self.enemy_list_image,self.LARGEUR,self.rectangle,self.CANVAS_WIDTH,self.CANVAS_HEIGHT)
        self.enemy_list_object[0].auto_tir(self.DIFFICULTEE,self.enemy_list_image,self.HAUTEUR)

    def creer_super_enemy(self):
        # fonction qui creer notre super enemy
        # entree : Aucune
        # sortie : Aucune
        X = (self.LARGEUR/2)
        Y = self.HAUTEUR/20
        
        self.super_enemy_list_object=[]
        self.super_enemy_list_image=[]
        self.super_enemy_list_object.append(e.Enemy(self,self.fenetre,1,self.VITESSE*2, X, Y, self.DY,self.is_running))
        self.super_enemy_list_image.append(self.fenetre.ZoneDeJeu.create_image(X,Y, image = self.lOADDED_SUPER_ENEMY))
        self.super_enemy_list_object[0].maj_super_ennemy_liste(self.super_enemy_list_object)
        #self.super_enemy_list_object[0].set_ennemy_liste()
        self.super_enemy_list_object[0].deplacement_super_enemy(self.VITESSE*2,0,self.super_enemy_list_image,self.LARGEUR,self.rectangle,self.CANVAS_WIDTH,self.CANVAS_HEIGHT)
        self.super_enemy_list_object[0].Super_auto_tir(self.DIFFICULTEE,self.super_enemy_list_image,self.HAUTEUR)
        self.collision_lance()


    def create_background_image(self):
        # fonction qui creer l'image de fonds et charge les images
        # entrée : Aucune
        # sortie : Aucune

        self.lOAD_ENEMY = Image.open("image/Ninja/Ninja.png")
        self.lOADDED_ENEMY =ImageTk.PhotoImage(self.lOAD_ENEMY)
        self.lOAD_SUPER_ENEMY = Image.open("image/Shieldmaiden/Shieldmaiden.png")
        self.lOADDED_SUPER_ENEMY =ImageTk.PhotoImage(self.lOAD_SUPER_ENEMY)
        self.lOAD_JOUEUR = Image.open("image/Samurai/Samurai.png")
        self.lOADDED_JOUEURS =ImageTk.PhotoImage(self.lOAD_JOUEUR)
        self.lOAD_KATANA = Image.open("image/Katana/Katana.png")
        self.lOADDED_KATANA =ImageTk.PhotoImage(self.lOAD_KATANA)
        self.lOAD_BARRIERE = Image.open("image/Fence.png")
        self.lOADDED_BARRIERE =ImageTk.PhotoImage(self.lOAD_BARRIERE)
        self.lOAD_GAMEOVER = Image.open("image/gameover.png")
        self.RESIZED_GAMEOVER = self.lOAD_GAMEOVER.resize((self.CANVAS_WIDTH,self.CANVAS_HEIGHT), Image.ANTIALIAS)
        self.lOADDED_GAMEOVER =ImageTk.PhotoImage(self.RESIZED_GAMEOVER)
        self.lOAD_VICTORY = Image.open("image/victory.png")
        self.RESIZED_VICTORY = self.lOAD_VICTORY.resize((self.CANVAS_WIDTH,self.CANVAS_HEIGHT), Image.ANTIALIAS)
        self.lOADDED_VICTORY =ImageTk.PhotoImage(self.RESIZED_VICTORY)


    def verif_win(self):
        # fonction qui verifie si le joueur a gagne et fait apparaitre l'ecran de victoire
        # entrée : Aucune
        # sortie : Aucune
        
        if len(self.enemy_list_object) == 0:
            print('win')
            self.is_running = False
            self.joueur.set_is_running()
            for e in self.enemy_list_object:
                e.set_is_running()
            for e in self.super_enemy_list_object:
                e.set_is_running()
            
            self.fenetre.ZoneDeJeu.delete('all')
            self.fenetre.ZoneDeJeu.create_image(0,0,anchor=NW,image = self.lOADDED_VICTORY)
            

        else:
            if self.is_running == True :
                self.fenetre.FrameGauche.after(10,self.verif_win)

    def verif_is_running(self):
        # fonction qui verifie si le joueur a perdu et permet aux autres fonctions de s'arreter tout en affichant l'ecran de fin 
        # entrée : Aucune
        # sortie : Aucune
        if self.fenetre.VIE <= 0:
            print('gameover')
            self.is_running = False
            self.joueur.set_is_running()
            for e in self.enemy_list_object:
                e.set_is_running()
            for e in self.super_enemy_list_object:
                e.set_is_running()
            
            self.fenetre.ZoneDeJeu.delete('all')
            self.fenetre.ZoneDeJeu.create_image(0,0,anchor=NW,image = self.lOADDED_GAMEOVER)
            
        else:
            self.fenetre.FrameGauche.after(20,self.verif_is_running)



    def creer_protection(self):
        # lance les créations des fonctions des barriere et lance les fonctions de vérifications des collisions du katana et du shuriken
        # entrée : Aucune
        # sortie : Aucune
        self.protection_barriere = p.Protection(self.fenetre,800,900)
        self.protection_barriere.forme1(60,700,16,9,2,self.fenetre) 
        self.protection_barriere.forme1(650,700,16,7,3,self.fenetre) 
        self.protection_barriere.forme1(1200,675,16,6,4,self.fenetre) 
        self.collision_katana()  
        self.collision_shuriken()


    def collision_shuriken(self):
        # regarde toutes les collision des shuriken, si ils touchent une barriere, le shuriken et la barriere se font supprimer.
        # entrée : Aucune
        # sortie : Aucune
        liste_rectangle=self.protection_barriere.get_rectangle()
        liste_projectile_enemy=self.enemy_list_object[0].get_liste_projectile()
        if len(liste_projectile_enemy)!=0:
            for o in liste_projectile_enemy:
                coords_shuriken=self.fenetre.ZoneDeJeu.coords(o)
                if len(coords_shuriken)!=0:
                    px=coords_shuriken[0]
                    py=coords_shuriken[1]
                    collision=self.fenetre.ZoneDeJeu.find_overlapping(px-30/2, py-30/2, px+30/2, py+30/2)
                    for i in collision:
                        if i in liste_rectangle :
                            self.fenetre.ZoneDeJeu.delete(i)
                            self.fenetre.ZoneDeJeu.delete(o)
        if self.is_running == True:
            self.fenetre.FrameGauche.after(20,self.collision_shuriken)

    def collision_lance(self):
        # regarde toutes les collision des shuriken, si ils touchent une barriere, le shuriken et la barriere se font supprimer.
        # entrée : Aucune
        # sortie : Aucune
        liste_rectangle=self.protection_barriere.get_rectangle()
        if self.super_enemy_list_object!=[]:
            liste_protection_super_enemy=self.super_enemy_list_object[0].get_liste_projectile2()
            if len(liste_protection_super_enemy)!=0:
                for o in liste_protection_super_enemy:
                    coords_shuriken=self.fenetre.ZoneDeJeu.coords(o)
                    if len(coords_shuriken)!=0:
                        px=coords_shuriken[0]
                        py=coords_shuriken[1]
                        collision=self.fenetre.ZoneDeJeu.find_overlapping(px-30/2, py-30/2, px+30/2, py+30/2)
                        for i in collision:
                            if i in liste_rectangle :
                                            self.fenetre.ZoneDeJeu.delete(i)
                                            self.fenetre.ZoneDeJeu.delete(o)
        if self.is_running == True:
            self.fenetre.FrameGauche.after(20,self.collision_lance)

    def collision_vaisseau(self):
        # regarde toute les collision du samourai, si il se fait touché pa un projectile ennemi il perd 1 ou 2 points en fonction du type de projectile 
        # qui l'a touché, ces meme projectiles se faisant supprimer  
        # entrée : Aucune
        # sortie : Aucune
        px=self.joueur.get_position_x()
        py=self.joueur.get_position_y()
        collision=self.fenetre.ZoneDeJeu.find_overlapping(px-63/2, py-66/2, px+63/2, py+66/2)
        liste_enemy_projectile=self.enemy_list_object[0].get_liste_projectile()
        if collision[len(collision)-1] in liste_enemy_projectile :
            if collision[len(collision)-1]!=2:
                self.fenetre.ZoneDeJeu.delete(collision[len(collision)-1])
                self.fenetre.VIE=self.fenetre.VIE-1
                self.fenetre.Texte_VIE.set('Vie : ' + str(self.fenetre.VIE))
        if self.super_enemy_list_object!=None and self.super_enemy_list_object!=[]:
            projectile_super_ennemy=self.super_enemy_list_object[0].get_liste_projectile2()
            if collision[len(collision)-1] in projectile_super_ennemy:
                if collision[len(collision)-1]!=2:
                    self.fenetre.ZoneDeJeu.delete(collision[len(collision)-1])
                    self.fenetre.VIE=self.fenetre.VIE-2
                    self.fenetre.Texte_VIE.set('Vie : ' + str(self.fenetre.VIE))
        self.fenetre.FrameGauche.after(20,self.collision_vaisseau)

    def collision_katana(self):
        # regarde toutes les collisions des katanas, si ils touchent une barriere ou un ennemi, le katana et la barriere/ennemi sont supprimer
        # entrée : Aucune
        # sortie : Aucune
        liste_katana=self.joueur.get_liste_katana()
        liste_rectangle=self.protection_barriere.get_rectangle()
        if len(liste_katana)!=0:
            for o in liste_katana:
                coords_katana=self.fenetre.ZoneDeJeu.coords(o)
                if len(coords_katana)!=0:
                    px=coords_katana[0]
                    py=coords_katana[1]
                    collision=self.fenetre.ZoneDeJeu.find_overlapping(px-10, py-20, px+10, py+20)
                    ennemy=self.enemy_list_image
                    boss=self.super_enemy_list_image
                    for i in collision:
                        if i in ennemy :
                            self.fenetre.ZoneDeJeu.delete(o)
                            indice=0
                            for t in ennemy:
                                if t==i:
                                    del self.enemy_list_object[indice]
                                    self.enemy_list_image.remove(i)
                                indice=+1
                                self.enemy_list_object[0].maj_enemy_liste_objet(self.enemy_list_object)
                            self.fenetre.ZoneDeJeu.delete(i)
                            self.fenetre.score=self.fenetre.score+25
                            self.fenetre.Texte_score.set('Score : ' + str(self.fenetre.score))
                        if boss!=None:
                            if i in boss :
                                self.fenetre.ZoneDeJeu.delete(o)
                                indice=0
                                for t in boss:
                                    if t==i:
                                        del self.super_enemy_list_object[indice]
                                    indice=+1
                                self.super_enemy_list_image.remove(i)
                                self.fenetre.ZoneDeJeu.delete(i)
                                self.fenetre.score=self.fenetre.score+500
                                self.fenetre.Texte_score.set('Score : ' + str(self.fenetre.score))
                        if i in liste_rectangle :
                            self.fenetre.ZoneDeJeu.delete(i)
                            self.fenetre.ZoneDeJeu.delete(o)
        
        if self.is_running == True:
            self.fenetre.FrameGauche.after(20,self.collision_katana)

                    


                
    


