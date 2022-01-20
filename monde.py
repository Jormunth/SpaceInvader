from tkinter import *
from PIL import Image, ImageTk
import random
import time
from protection import Protection
import vaisseau as V
import enemy as e
import protection as p



class Monde:

    def __init__(self,fenetre,DIFFICULTEE,DY,VITESSE,LARGEUR,HAUTEUR,CANVAS_WIDTH,CANVAS_HEIGHT):
        
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
        self.myEnemyList=[]
        self.myEnemy = []
        self.FrameGauche=None
        self.ProjectileEnemy = []
        self.Vaisseau = None
        self.enemy_list_object = []
        self.enemy_list_image = []
        self.loadEnemy = None
        self.loaddedEnemy = None
        self.loadSuperEnemy = None
        self.loaddedSuperEnemy = None
        self.loadJoueur = None
        self.loaddedJoueurs = None
        self.loadKatana = None
        self.loaddedKatana = None
        self.loadBarriere = None
        self.loaddedBarriere = None
        self.niveau = 0

        self.create_background_image()
        self.gere_le_monde()

    def gere_le_monde(self):
        self.creerEnemy()
        self.creerJoueur()
        self.creerProtection()
        self.verifNiveau()
        
        aleatoire = random.randint(1,10)
        aleatoire *= 1000
        self.fenetre.FrameGauche.after(aleatoire,self.creerSuperEnnemie)
        
        """ ma_fenetre.ZoneDeJeu.after(20,ma_fenetre.bouger,projectile,ma_fenetre,self.DIFFICULTEE) """
       

    def creerJoueur(self):
        POSX = 800
        POSY = 900

        self.Vaisseau = self.fenetre.ZoneDeJeu.create_image(POSX,POSY, image = self.loaddedJoueurs)
        joueur = V.Vaisseau(self,self.fenetre,800,900,63,self.Vaisseau,self.LARGEUR,self.HAUTEUR,self.enemy_list_object,self.enemy_list_image)

        self.fenetre.ZoneDeJeu.bind('<Key>',joueur.Clavier)
        self.fenetre.ZoneDeJeu.bind('<Button-1>',joueur.creer_projectile)

    def creerEnemy(self):
                
        tag = 0
        PLACEMENT = 10
        NB_ENNEMIE = self.DIFFICULTEE
        LIM_LIGNE = 5
        compteur = 0
        DELTA_Y = 1

        """ frameCntEnemie = 5
        imageEnnemie = [PhotoImage(file='image/Ninja/animation/runRight_2.gif',format = 'gif -index %i' %(i)) for i in range(frameCntEnemie)] """

        while NB_ENNEMIE >= 1:

            if compteur % LIM_LIGNE == 0:
                compteur = 0
                DELTA_Y += 60

            compteur += 1

            tag += 1
            X = (self.LARGEUR/PLACEMENT)*compteur
            Y = self.HAUTEUR/20 + DELTA_Y

            self.enemy_list_object.append(e.Enemy(self,self.fenetre,tag,self.VITESSE, X, Y, self.DY))
            self.enemy_list_image.append(self.fenetre.ZoneDeJeu.create_image(X,Y, image = self.loaddedEnemy))
            NB_ENNEMIE -= 1

        self.enemy_list_object[0].deplacementEnemy(self.VITESSE,self.DY,self.enemy_list_object,self.enemy_list_image,self.LARGEUR,self.enemy_list_object,self.rectangle,self.CANVAS_WIDTH,self.CANVAS_HEIGHT)
        self.enemy_list_object[0].autoTir(self.DIFFICULTEE,self.enemy_list_object,self.enemy_list_image,self.HAUTEUR)

    def creerSuperEnnemie(self):
        X = (self.LARGEUR/2)
        Y = self.HAUTEUR/20
        
        super_enemy_list_object=[]
        super_enemy_list_image=[]
        super_enemy_list_object.append(e.Enemy(self,self.fenetre,1,self.VITESSE*2, X, Y, self.DY))
        super_enemy_list_image.append(self.fenetre.ZoneDeJeu.create_image(X,Y, image = self.loaddedSuperEnemy))
        super_enemy_list_object[0].deplacementEnemy(self.VITESSE*2,0,super_enemy_list_object,super_enemy_list_image,self.LARGEUR,super_enemy_list_object,self.rectangle,self.CANVAS_WIDTH,self.CANVAS_HEIGHT)
        super_enemy_list_object[0].autoTir(self.DIFFICULTEE,super_enemy_list_object,super_enemy_list_image,self.HAUTEUR)

    def create_background_image(self):

        self.loadEnemy = Image.open("image/Ninja/Ninja.png")
        self.loaddedEnemy =ImageTk.PhotoImage(self.loadEnemy)
        self.loadSuperEnemy = Image.open("image/Shieldmaiden/Shieldmaiden.png")
        self.loaddedSuperEnemy =ImageTk.PhotoImage(self.loadSuperEnemy)
        self.loadJoueur = Image.open("image/Samurai/Samurai.png")
        self.loaddedJoueurs =ImageTk.PhotoImage(self.loadJoueur)
        self.loadKatana = Image.open("image/Katana/Katana.png")
        self.loaddedKatana =ImageTk.PhotoImage(self.loadKatana)
        self.loadBarriere = Image.open("image/Fence.png")
        self.loaddedBarriere =ImageTk.PhotoImage(self.loadBarriere)


    def verifNiveau(self):
        if len(self.enemy_list_object) == 0:
            self.niveau += 1
            self.DIFFICULTEE +=4
            self.gere_le_monde()
        else:
            self.fenetre.FrameGauche.after(10,self.verifNiveau)    




    def collision(self,x1,y1,y2,x2):
        tag = self.fenetre.ZoneDeJeu.find_overlapping(x1, y1, x2, y2)
        objets = self.fenetre.ZoneDeJeu.find_withtag(tag)
        self.fenetre.ZoneDeJeu.delete(objets)
        self.projectile.remove(objets)



    def creerProtection(self):
        Protection = p.Protection(self.fenetre,800,900)
        Protection.forme1(60,700,16,30,2,self.fenetre)   


    def collision_enemy_protection(self,px,py,taille,cpx,cpy):
        if cpx>=px-taille and cpx<=px+2*taille:
            if cpy>=py:
                return(True)
        return(False)


    def collision_projectilev_ennemi(self,px,py,taillex,tailley,cpx,cpy):
        if cpx>=px-taillex and cpx<=px+2*taillex:
            if cpy<=py+tailley and cpy>=py:
                return(True)
        return(False)

    def collision_projectilee_vaisseau(self,px,py,taillex,cpx,cpy):
        if cpx>=px-taillex and cpx<=px+2*taillex:
            if cpy+30>=py and cpy<=py+self.tailleVaisseau:
                return(True)
        return(False)
