
from tkinter import *
from PIL import Image, ImageTk

class Projectile:
    def __init__(self,vaisseau,monde,fenetre,px,py,rayon,vitesse):
        self.monde=monde
        self.fenetre=fenetre
        self.py=py
        self.px=px
        self.rayon=rayon
        self.vitesse=vitesse
        self.vaisseau=vaisseau


    def deplacementProjectEautoTir(self,list_projectilelast,coordsEnemyY,list_projectile,HAUTEUR):

        for t in list_projectile:
            coords_tir = self.fenetre.ZoneDeJeu.coords(t)
            """
            coords_vaisseau=self.fenetre.ZoneDeJeu.coords(self.vaisseau)
            verif_collisionvaisseau=self.monde.collision_projectilee_vaisseau(coords_vaisseau[0],coords_vaisseau[1],40,coords_tir[0]-15,coords_tir[1]-15)
            if verif_collisionvaisseau==True:
                self.vie=self.vie-1
                print(self.vie)
                self.fenetre.ZoneDeJeu.delete(t)
                if t in list_projectile:
                    list_projectile.remove(t)
            for o in self.rectangle:
                coords_protection=self.fenetre.ZoneDeJeu.coords(o)
                verif=self.monde.collision_enemy_protection(coords_protection[0],coords_protection[1],18,coords_tir[0],coords_tir[1])
                if verif ==True:
                    self.fenetre.ZoneDeJeu.delete(o)
                    self.rectangle.remove(o)
                    self.fenetre.ZoneDeJeu.delete(t)
                    if t in list_projectile:
                        list_projectile.remove(t)
 """
            if coords_tir[1] - 15 < HAUTEUR:
                self.fenetre.ZoneDeJeu.move(list_projectilelast, 0, 20)
                
            else:

                if t in list_projectile:
                    self.fenetre.ZoneDeJeu.delete(t)
                    list_projectile.remove(t)

        self.fenetre.FrameGauche.after(20,self.deplacementProjectEautoTir,list_projectilelast,coordsEnemyY,list_projectile,HAUTEUR)


    def deplacementProjectEautoTir(self,ProjectileEnemylast,coordsEnemyY,ProjectileEnemy,HAUTEUR):

        
        for t in ProjectileEnemy:
            coords_tir = self.ZoneDeJeu.coords(t)
            coords_vaisseau=self.ZoneDeJeu.coords(self.Vaisseau)
            verif_collisionvaisseau=monde.collision_projectilee_vaisseau(coords_vaisseau[0],coords_vaisseau[1],self.tailleVaisseau,coords_tir[0]-15,coords_tir[1]-15)
            if verif_collisionvaisseau==True:
                self.vie=self.vie-1
                self.Texte_vie.set('Vie : ' + str(self.vie))
                self.ZoneDeJeu.delete(t)
                if t in self.ProjectileEnemy:
                    self.ProjectileEnemy.remove(t)
            for o in self.rectangle:
                coords_protection=self.ZoneDeJeu.coords(o)
                verif=ma_fenetre.collision_enemy_protection(coords_protection[0],coords_protection[1],32/2,coords_tir[0],coords_tir[1])
                if verif ==True:
                    self.ZoneDeJeu.delete(o)
                    self.rectangle.remove(o)
                    self.ZoneDeJeu.delete(t)
                    if t in self.ProjectileEnemy:
                        self.ProjectileEnemy.remove(t)

            if coords_tir[1] - 15 < self.Hauteur:
                self.ZoneDeJeu.move(ProjectileEnemylast, 0, 20)
                
            else:
                if t in self.ProjectileEnemy:
                    self.ZoneDeJeu.delete(t)
                    self.ProjectileEnemy.remove(t)

        self.FrameGauche.after(100,self.deplacementProjectEautoTir,ProjectileEnemylast,coordsEnemyY,ma_fenetre)



    def bouger(self,projectile,projectile_list,enemy_list_object):
        for t in projectile_list:
            coords_projectile=self.fenetre.ZoneDeJeu.coords(t)
            k=0
            """ for i in range(len(enemy_list_object)):
                verif_ennemy=self.monde.collision_projectilev_ennemi(self.enemy_list_object[k].getPosX()-39/2,self.enemy_list_object[k].getPosY()-45/2,39/2,45,coords_projectile[0],coords_projectile[1])
                if verif_ennemy ==True:
                    del self.enemy_list_object[k]
                    self.fenetre.ZoneDeJeu.delete(self.myEnemy[k])
                    del self.myEnemy[k]
                    if t in projectile_list:
                        self.fenetre.ZoneDeJeu.delete(t)
                        projectile_list.remove(t)
                    k=k-1
                k=k+1
            for o in self.rectangle:
                coords_protection=self.fenetre.ZoneDeJeu.coords(o)
                verif=self.monde.collision_protection(coords_protection[0],coords_protection[1],18,coords_projectile[0],coords_projectile[1])
                if verif ==True:
                    self.fenetre.ZoneDeJeu.delete(o)
                    self.rectangle.remove(o)
                    if t in self.projectile:
                        self.fenetre.ZoneDeJeu.delete(t)
                        self.projectile.remove(t) """
            if coords_projectile[1]>0:
                self.fenetre.ZoneDeJeu.move(t,0,-self.vitesse)
            else:
                if t in projectile_list:
                    self.fenetre.ZoneDeJeu.delete(t)
                    projectile_list.remove(t)
        self.fenetre.ZoneDeJeu.after(100,self.bouger,projectile,projectile_list,enemy_list_object)


    def bouger(self,projectilelast,difficulty):
        for t in self.projectile:
            coords_projectile=self.ZoneDeJeu.coords(t)
            k=0
            for i in range(len(self.myEnemyList)):
                verif_ennemy=self.collision_projectilev_ennemi(self.myEnemyList[k].getPosX()-39/2,self.myEnemyList[k].getPosY()-45/2,39/2,45,coords_projectile[0],coords_projectile[1])
                if verif_ennemy ==True:
                    self.score=self.score+25
                    self.Texte_score.set('Score : ' + str(self.score))
                    del self.myEnemyList[k]
                    self.ZoneDeJeu.delete(self.myEnemy[k])
                    del self.myEnemy[k]
                    if t in self.projectile:
                        self.ZoneDeJeu.delete(t)
                        self.projectile.remove(t)
                    k=k-1
                k=k+1
            for o in self.rectangle:
                coords_protection=self.ZoneDeJeu.coords(o)
                verif=self.collision_protection(coords_protection[0],coords_protection[1],32/2,coords_projectile[0],coords_projectile[1])
                if verif ==True:
                    self.ZoneDeJeu.delete(o)
                    self.rectangle.remove(o)
                    if t in self.projectile:
                        self.ZoneDeJeu.delete(t)
                        self.projectile.remove(t)
            if coords_projectile[1]>0:
                self.ZoneDeJeu.move(projectilelast,0,-20)
            else:
                if t in self.projectile:
                    self.ZoneDeJeu.delete(t)
                    self.projectile.remove(t)
        self.ZoneDeJeu.after(100,self.bouger,projectilelast,difficulty)  