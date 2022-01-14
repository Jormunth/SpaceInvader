from tkinter import *
from PIL import Image, ImageTk
import random
import projectile as project
class Enemy:
    def __init__(self,monde,fenetre,tag,VITESSE,posX, posY,DY):
        self.fenetre = fenetre
        self.tag=tag
        self.posX=posX
        self.posY=posY
        self.VITESSE=VITESSE
        self.DY=DY
        self.ProjectileEnemy = []
        self.monde = monde

    def getTag(self):
        return self.tag

    def getPosX(self):
        self.posX
        return self.posX

    def getPosY(self):
        return self.posY

    def getVITESSE(self):
        return self.VITESSE

    def getDY(self):
        return self.DY

    def deplacer(self, NewposX, NewposY):
        self.posX = NewposX
        self.posY = NewposY
        """ print("Position actuelle", self.posX, " ", self.posY,) """
    
    def tirer(self):
        print("Je tire")



    def deplacementEnemy(self,VITESSE,DY,enemy_list_object,enemy_list_image,LARGEUR):
        
        DX = VITESSE
        DY = 0

        XtremG = enemy_list_object[0].getPosX()
        XtremD = enemy_list_object[-1].getPosX()

        posy=enemy_list_object[-1].getPosY()

        XtremG += DX
        XtremD += DX    

        if posy >=900-30:
            k=0
            for i in range(len(self.myEnemyList)):
                del self.myEnemyList[k]
                self.ZoneDeJeu.delete(self.myEnemy[k])
                del self.myEnemy[k]
                

        else:
            for i in range(len(self.myEnemyList)):
                posx=self.enemy_list_object[i].getPosX()
                posy=self.enemy_list_object[i].getPosY()
                for o in self.rectangle:
                    coords_protection=self.ZoneDeJeu.coords(o)
                    verif_collision=self.fenetre.collision_enemy_protection(coords_protection[0],coords_protection[1],32/2,posx,posy)
                    if verif_collision==True:
                        self.ZoneDeJeu.delete(o)
                        self.rectangle.remove(o)

            if XtremD + 20 > LARGEUR:
                XtremD= 2*LARGEUR - XtremD
                VITESSE = -DX
                DY = 60

            if XtremG -20 < 0:
                XtremG = -XtremG
                VITESSE = -DX
                DY = 60

            for i,val in enumerate(enemy_list_image):
                self.fenetre.ZoneDeJeu.move(enemy_list_image[i],DX,DY)
                enemy_list_object[i].deplacer(enemy_list_object[i].getPosX()+DX,enemy_list_object[i].getPosY()+DY)


        self.fenetre.FrameGauche.after(20,self.deplacementEnemy,VITESSE,self.DY,enemy_list_object,enemy_list_image,LARGEUR)


        
    def autoTir(self,difficulty,enemy_list_object,enemy_list_image,HAUTEUR):
     
        frameCntProj = 2
        """ imageProj = [PhotoImage(file='image/Shuriken/Shuriken.gif',format = 'gif -index %i' %(i)) for i in range(frameCntProj)] """

        max = len(enemy_list_image)-1

        rand=random.randint(0,max)

        coordsEnemyX = enemy_list_object[rand].getPosX()
        coordsEnemyY = enemy_list_object[rand].getPosY()
        
        self.loadShuriken = Image.open("image/Shuriken/Shuriken.png")
        self.loaddedShuriken =ImageTk.PhotoImage(self.loadShuriken)
        ProjectileEnemylast=self.fenetre.ZoneDeJeu.create_image(coordsEnemyX,coordsEnemyY, image = self.loaddedShuriken)

        self.ProjectileEnemy.append(ProjectileEnemylast)
        self.fenetre.FrameGauche.after(750,self.autoTir,difficulty,enemy_list_object,enemy_list_image,HAUTEUR)

        projectile_enemy=project.Projectile(self,self.monde,self.fenetre,self.getPosX,self.getPosY,20,self.VITESSE)
        projectile_enemy.deplacementProjectEautoTir(ProjectileEnemylast,coordsEnemyY,self.ProjectileEnemy,HAUTEUR)
