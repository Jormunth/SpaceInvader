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
        self.controle_up=controle_up
        self.controle_down=controle_down
        self.controle_left=controle_left
        self.controle_right=controle_right
        self.controle_shot=controle_shot
        self.joueur=None
        self.Protection1=None
        self.super_enemy_list_object=None
        self.super_enemy_list_image=None

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
        POSY = 850

        self.Vaisseau = self.fenetre.ZoneDeJeu.create_image(POSX,POSY, image = self.loaddedJoueurs)
        self.joueur = V.Vaisseau(self,self.fenetre,800,900,63,self.Vaisseau,self.LARGEUR,self.HAUTEUR,self.enemy_list_object,self.enemy_list_image,self.controle_up, self.controle_down, self.controle_left, self.controle_right,self.controle_shot)

        self.fenetre.ZoneDeJeu.bind('<Key>',self.joueur.Clavier)
        self.fenetre.ZoneDeJeu.bind(f'<{self.controle_shot}>',self.joueur.creer_projectile)
        self.collision_vaisseau()
        
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

        self.enemy_list_object[0].maj_enemy_liste_objet(self.enemy_list_object)
        self.enemy_list_object[0].deplacementEnemy(self.VITESSE,self.DY,self.enemy_list_image,self.LARGEUR,self.rectangle,self.CANVAS_WIDTH,self.CANVAS_HEIGHT)
        self.enemy_list_object[0].autoTir(self.DIFFICULTEE,self.enemy_list_image,self.HAUTEUR)

    def creerSuperEnnemie(self):
        X = (self.LARGEUR/2)
        Y = self.HAUTEUR/20
        
        self.super_enemy_list_object=[]
        self.super_enemy_list_image=[]
        self.super_enemy_list_object.append(e.Enemy(self,self.fenetre,1,self.VITESSE*2, X, Y, self.DY))
        self.super_enemy_list_image.append(self.fenetre.ZoneDeJeu.create_image(X,Y, image = self.loaddedSuperEnemy))
        self.super_enemy_list_object[0].maj_super_ennemy_liste(self.super_enemy_list_object)
        self.super_enemy_list_object[0].deplacementSuperEnemy(self.VITESSE*2,0,self.super_enemy_list_image,self.LARGEUR,self.rectangle,self.CANVAS_WIDTH,self.CANVAS_HEIGHT)
        self.super_enemy_list_object[0].SuperAutoTir(self.DIFFICULTEE,self.super_enemy_list_image,self.HAUTEUR)

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
        self.Protection1 = p.Protection(self.fenetre,800,900)
        self.Protection1.forme1(60,700,16,30,2,self.fenetre) 
        self.collision_katana()  
        self.collision_shuriken()
        self.collision_lance()


    def collision_shuriken(self):
        liste_rectangle=self.Protection1.getRectangle()
        LP=self.enemy_list_object[0].getListeProjectile()
        if len(LP)!=0:
            for o in LP:
                coords_shuriken=self.fenetre.ZoneDeJeu.coords(o)
                if len(coords_shuriken)!=0:
                    px=coords_shuriken[0]
                    py=coords_shuriken[1]
                    truc=self.fenetre.ZoneDeJeu.find_overlapping(px-30/2, py-30/2, px+30/2, py+30/2)
                    for i in truc:
                        if i in liste_rectangle :
                                        self.fenetre.ZoneDeJeu.delete(i)
                                        self.fenetre.ZoneDeJeu.delete(o)
        self.fenetre.FrameGauche.after(20,self.collision_shuriken)

    def collision_lance(self):
        liste_rectangle=self.Protection1.getRectangle()
        LP=self.super_enemy_list_object[0].getListeProjectile2()
        if len(LP)!=0:
            for o in LP:
                coords_shuriken=self.fenetre.ZoneDeJeu.coords(o)
                if len(coords_shuriken)!=0:
                    px=coords_shuriken[0]
                    py=coords_shuriken[1]
                    truc=self.fenetre.ZoneDeJeu.find_overlapping(px-30/2, py-30/2, px+30/2, py+30/2)
                    for i in truc:
                        if i in liste_rectangle :
                                        self.fenetre.ZoneDeJeu.delete(i)
                                        self.fenetre.ZoneDeJeu.delete(o)
        self.fenetre.FrameGauche.after(20,self.collision_lance)



    def collision_vaisseau(self):
        px=self.joueur.getPosX()
        py=self.joueur.getPosY()
        truc=self.fenetre.ZoneDeJeu.find_overlapping(px-63/2, py-66/2, px+63/2, py+66/2)
        LP=self.enemy_list_object[0].getListeProjectile()
        if truc[len(truc)-1] in LP :
            if truc[len(truc)-1]!=2:
                self.fenetre.ZoneDeJeu.delete(truc[len(truc)-1])
                self.fenetre.VIE=self.fenetre.VIE-1
                self.fenetre.Texte_VIE.set('Vie : ' + str(self.fenetre.VIE))
        if self.super_enemy_list_object!=None and self.super_enemy_list_object!=[]:
            projectile_superEnnemy=self.super_enemy_list_object[0].getListeProjectile()
            if truc[len(truc)-1] in projectile_superEnnemy:
                if truc[len(truc)-1]!=2:
                    self.fenetre.ZoneDeJeu.delete(truc[len(truc)-1])
                    self.fenetre.VIE=self.fenetre.VIE-1
                    self.fenetre.Texte_VIE.set('Vie : ' + str(self.fenetre.VIE))
        self.fenetre.FrameGauche.after(20,self.collision_vaisseau)

    def collision_katana(self):
        liste_katana=self.joueur.getListeKatana()
        liste_rectangle=self.Protection1.getRectangle()
        if len(liste_katana)!=0:
            for o in liste_katana:
                coords_katana=self.fenetre.ZoneDeJeu.coords(o)
                if len(coords_katana)!=0:
                    px=coords_katana[0]
                    py=coords_katana[1]
                    truc=self.fenetre.ZoneDeJeu.find_overlapping(px-10, py-20, px+10, py+20)
                    ennemy=self.enemy_list_image
                    boss=self.super_enemy_list_image
                    for i in truc:
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
                                    #self.super_enemy_list_image[0].maj_super_ennemy_liste(self.super_enemy_list_object)
                                self.super_enemy_list_image.remove(i)
                                self.fenetre.ZoneDeJeu.delete(i)
                                self.fenetre.score=self.fenetre.score+500
                                self.fenetre.Texte_score.set('Score : ' + str(self.fenetre.score))
                        if i in liste_rectangle :
                            self.fenetre.ZoneDeJeu.delete(i)
                            self.fenetre.ZoneDeJeu.delete(o)
        self.fenetre.FrameGauche.after(20,self.collision_katana)

                
            
        



    def collision_enemyprojectile_protection(self,projectile):
        coords_projectile=self.fenetre.ZoneDeJeu.coords(projectile)
        cpx=coords_projectile[0]
        cpy=coords_projectile[1]
        rectangle=self.Protection1.getRectangle()
        taille=32/2
        for o in rectangle:
            coords_protection=self.fenetre.ZoneDeJeu.coords(o)
            px=coords_protection[0]
            py=coords_protection[1]
            if cpx>=px-taille and cpx<=px+2*taille:
                if cpy>=py:
                    self.fenetre.ZoneDeJeu.delete(o)
                    self.rectangle.remove(o)
                    self.fenetre.ZoneDeJeu.delete(projectile)
                    
        
    def collision_protection(self,projectile):
        coords_projectile=self.fenetre.ZoneDeJeu.coords(projectile)
        cpx=coords_projectile[0]
        cpy=coords_projectile[1]
        rectangle=self.Protection1.getRectangle()
        taille=32/2
        for o in rectangle:
            coords_protection=self.fenetre.ZoneDeJeu.coords(o)
            px=coords_protection[0]
            py=coords_protection[1]
            if cpx>=px-taille and cpx<=px+2*taille:
                if cpy<=py+taille*3:
                    self.fenetre.ZoneDeJeu.delete(o)
                    self.rectangle.remove(o)
                    self.fenetre.ZoneDeJeu.delete(projectile)




    def collision_projectilev_ennemi(self,projectile):
        coords_projectile=self.fenetre.ZoneDeJeu.coords(projectile)
        cpx=coords_projectile[0]
        cpy=coords_projectile[1]
        taillex=39/2
        tailley=45
        for i in range(len(self.enemy_list_object)):
            py=self.enemy_list_object[i].getPosy()-39/2
            px=self.enemy_list_object[i].getPosx()-45/2
            if cpx>=px-taillex and cpx<=px+2*taillex:
                if cpy<=py+tailley and cpy>=py:
                    self.fenetre.ZoneDeJeu.delete(i)
                    del self.enemy_list_object[i]
                    self.fenetre.ZoneDeJeu.delete(projectile)


                
    def collision_projectilee_vaisseau(self,projectile):
        coords_projectile=self.fenetre.ZoneDeJeu.coords(projectile)
        cpx=coords_projectile[0]
        cpy=coords_projectile[1]
        px=self.joueur.getPosX()
        py=self.joueur.getPosX()
        taille_vaisseau=self.joueur.getTaille()
        if cpx>=px-taille_vaisseau and cpx<=px+2*taille_vaisseau:
            if cpy+30>=py and cpy<=py+taille_vaisseau:
                self.vie=self.vie-1
                self.Texte_vie.set('Vie : ' + str(self.vie))
                self.fenetre.ZoneDeJeu.delete(projectile)


