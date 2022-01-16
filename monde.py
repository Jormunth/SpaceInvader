from tkinter import *
from PIL import Image, ImageTk
from protection import Protection
import vaisseau as V
import enemy as e
import protection as p



class Monde:

    def __init__(self,fenetre,DIFFICULTEE,DY,VITESSE,LARGEUR,HAUTEUR):
        
        self.LARGEUR = LARGEUR
        self.HAUTEUR = HAUTEUR
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

        self.gere_le_monde()

    def gere_le_monde(self):
        self.creerEnemy()
        self.creerJoueur()
        self.creerProtection()

        """ ma_fenetre.ZoneDeJeu.after(20,ma_fenetre.bouger,projectile,ma_fenetre,self.DIFFICULTEE) """
       

    def creerJoueur(self):
        POSX = 800
        POSY = 900

        self.loadJoueur = Image.open("image/Samurai/Samurai.png")
        self.loaddedJoueurs =ImageTk.PhotoImage(self.loadJoueur)
        self.Vaisseau = self.fenetre.ZoneDeJeu.create_image(POSX,POSY, image = self.loaddedJoueurs)
        joueur = V.Vaisseau(self,self.fenetre,800,900,63,self.Vaisseau,self.LARGEUR,self.HAUTEUR,self.enemy_list_object,self.enemy_list_image)

        self.fenetre.ZoneDeJeu.bind('<Key>',joueur.Clavier)
        self.fenetre.ZoneDeJeu.bind('<Button-1>',joueur.creer_projectile)

    def creerEnemy(self):
                
        tag = 0
        PLACEMENT = self.DIFFICULTEE+1
        NB_ENNEMIE = self.DIFFICULTEE

        """ frameCntEnemie = 5
        imageEnnemie = [PhotoImage(file='image/Ninja/animation/runRight_2.gif',format = 'gif -index %i' %(i)) for i in range(frameCntEnemie)] """
        
        self.loadEnemy = Image.open("image/Ninja/Ninja.png")
        self.loaddedEnemy =ImageTk.PhotoImage(self.loadEnemy)

        while NB_ENNEMIE >= 1:
            
            tag += 1
            X = (self.LARGEUR/PLACEMENT)*tag
            Y = self.HAUTEUR/20

            self.enemy_list_object.append(e.Enemy(self,self.fenetre,tag,self.VITESSE, X, Y, self.DY))
            self.enemy_list_image.append(self.fenetre.ZoneDeJeu.create_image(X,Y, image = self.loaddedEnemy))
            NB_ENNEMIE -= 1

        self.enemy_list_object[0].deplacementEnemy(self.VITESSE,self.DY,self.enemy_list_object,self.enemy_list_image,self.LARGEUR,self.enemy_list_object,self.rectangle)
        self.enemy_list_object[0].autoTir(self.DIFFICULTEE,self.enemy_list_object,self.enemy_list_image,self.HAUTEUR)

    def creerProtection(self):
        Protection = p.Protection(self.fenetre,800,900)
        Protection.forme1(60,700,18,30,2,self.fenetre)   




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
