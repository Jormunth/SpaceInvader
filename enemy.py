# gere toutes les fonctions liees aux ennemies qui sont celle de son nottament celle de son mouvement et la creation de ses projectile
# Mathieu Zeman / Gaelle Leroux
# realise entre decembre 2021 et janvier 2022 


from tkinter import *
from PIL import Image, ImageTk
import random
import projectile as project
class Enemy:
    def __init__(self,monde,fenetre,tag,VITESSE,position_x, position_y,DY,is_running):
        self.fenetre = fenetre
        self.tag=tag
        self.load_shuriken = None
        self.loadded_shuriken = None
        self.load_lance = None
        self.loadded_lance = None
        self.position_x=position_x
        self.position_y=position_y
        self.VITESSE=VITESSE
        self.DY=DY
        self.Projectile_enemy = []
        self.monde = monde
        self.enemy_list_object=None
        self.super_ennemy_liste_object=None
        self.Projectile_enemy2 = ["coucou"]
        self.super_ennemy=None
        self.is_running=is_running

        self.image()

    def get_tag(self):
        # fonction qui renvoie le tag de l'Enemy
        # entree : Aucune
        # sortie : Aucune
        return self.tag

    def get_position_x(self):
        # fonction qui renvoie la position x de l'ennemie
        # entree : Aucune
        # sortie : la position en x de l'ennemie
        self.position_x
        return self.position_x

    def get_position_y(self):
        # fonction qui renvoie la position y de l'ennemie
        # entree : Aucune
        # sortie : la position en y de l'ennemie
        return self.position_y


    def deplacer(self, NewposX, NewposY):
        # met a jour la position des ennemie_pos_x
        # entrée : Aucune
        # sortie : Aucune
        self.position_x = NewposX
        self.position_y = NewposY
    


    def image(self):
        # fonction qui charge les images 
        # entrée: Aucune
        # sortie : Aucune

        self.load_shuriken = Image.open("image/Shuriken/Shuriken.png")
        self.loadded_shuriken =ImageTk.PhotoImage(self.load_shuriken)

        self.load_lance = Image.open("image/Shieldmaiden/Lance2.png")
        self.loadded_lance =ImageTk.PhotoImage(self.load_lance)

    def deplacement_enemy(self,VITESSE,DY,enemy_list_image,LARGEUR,rectangle,CANVAS_WIDTH,CANVAS_HEIGHT):
        # fonction qui deplace les ennemie
        # entrée : Aucune
        # sortie : Aucune
        
        DX = VITESSE
        DY = 0
        most_right = 0
        most_left = CANVAS_WIDTH

        for ennemie in self.enemy_list_object:
            ennemie_pos_x = ennemie.get_position_x()
            if ennemie_pos_x > most_right:
                most_right = ennemie_pos_x

        for ennemie in self.enemy_list_object:
            ennemie_pos_x = ennemie.get_position_x()
            if ennemie_pos_x < most_left:
                most_left = ennemie_pos_x

        """ most_left = enemy_list_object[0].get_position_x()
        most_right = enemy_list_object[-1].getPosX() """

        position_y=self.enemy_list_object[-1].get_position_y()

        most_left += DX
        most_right += DX    

        if position_y >= CANVAS_HEIGHT-30:
            k=0
            for i in range(len(self.enemy_list_object)):
                del self.myEnemyList[k]
                self.ZoneDeJeu.delete(self.myEnemy[k])
                del self.myEnemy[k]
                

        else:
            for i in range(len(self.enemy_list_object)):
                position_x=self.enemy_list_object[i].get_position_x()
                position_y=self.enemy_list_object[i].get_position_y()
                for o in rectangle:
                    coords_protection=self.ZoneDeJeu.coords(o)
                    verif_collision=self.fenetre.collision_enemy_protection(coords_protection[0],coords_protection[1],32/2,position_x,position_y)
                    if verif_collision==True:
                        self.ZoneDeJeu.delete(o)
                        self.rectangle.remove(o)

            if most_right + 32 > CANVAS_WIDTH:
                most_right= 2*CANVAS_WIDTH - most_right
                VITESSE = -DX
                DY = 60

            if most_left -32 < 0:
                most_left = -most_left
                VITESSE = -DX
                DY = 60

            for i,val in enumerate(enemy_list_image):
                self.fenetre.ZoneDeJeu.move(enemy_list_image[i],DX,DY)
                self.enemy_list_object[i].deplacer(self.enemy_list_object[i].get_position_x()+DX,self.enemy_list_object[i].get_position_y()+DY)

        if self.is_running != False:
            self.fenetre.FrameGauche.after(20,self.deplacement_enemy,VITESSE,self.DY,enemy_list_image,LARGEUR,rectangle,CANVAS_WIDTH,CANVAS_HEIGHT)


    def deplacement_super_enemy(self,VITESSE,DY,enemy_list_image,LARGEUR,rectangle,CANVAS_WIDTH,CANVAS_HEIGHT):
        # fonction qui deplace le super ennemie
        # entrée : Aucune
        # sortie : Aucune

        if self.super_ennemy!=[]:
            
            DX = VITESSE
            DY = 0
            most_right = 0
            most_left = CANVAS_WIDTH

            for ennemie in self.super_ennemy_liste_object:
                ennemie_pos_x = ennemie.get_position_x()
                if ennemie_pos_x > most_right:
                    most_right = ennemie_pos_x

            for ennemie in self.super_ennemy_liste_object:
                ennemie_pos_x = ennemie.get_position_x()
                if ennemie_pos_x < most_left:
                    most_left = ennemie_pos_x

            """ most_left = enemy_list_object[0].getPosX()
            most_right = enemy_list_object[-1].getPosX() """
            if self.super_ennemy_liste_object!=[]:
                position_y=self.super_ennemy_liste_object[-1].get_position_y()

                most_left += DX
                most_right += DX    

                if position_y >= CANVAS_HEIGHT-30:
                    k=0
                    for i in range(len(self.super_ennemy_liste_object)):
                        del self.myEnemyList[k]
                        self.ZoneDeJeu.delete(self.myEnemy[k])
                        del self.myEnemy[k]
                        

                else:
                    for i in range(len(self.super_ennemy_liste_object)):
                        position_x=self.super_ennemy_liste_object[i].get_position_x()
                        position_y=self.super_ennemy_liste_object[i].get_position_y()
                        for o in rectangle:
                            coords_protection=self.ZoneDeJeu.coords(o)
                            verif_collision=self.fenetre.collision_enemy_protection(coords_protection[0],coords_protection[1],32/2,position_x,position_y)
                            if verif_collision==True:
                                self.ZoneDeJeu.delete(o)
                                self.rectangle.remove(o)

                    if most_right + 32 > CANVAS_WIDTH:
                        most_right= 2*CANVAS_WIDTH - most_right
                        VITESSE = -DX
                        DY = 60

                    if most_left -32 < 0:
                        most_left = -most_left
                        VITESSE = -DX
                        DY = 60

                    for i,val in enumerate(enemy_list_image):
                        self.fenetre.ZoneDeJeu.move(enemy_list_image[i],DX,DY)
                        self.super_ennemy_liste_object[i].deplacer(self.super_ennemy_liste_object[i].get_position_x()+DX,self.super_ennemy_liste_object[i].get_position_y()+DY)

            if self.is_running == True:
                self.fenetre.FrameGauche.after(20,self.deplacement_super_enemy,VITESSE,self.DY,enemy_list_image,LARGEUR,rectangle,CANVAS_WIDTH,CANVAS_HEIGHT)

    def auto_tir(self,difficulty,enemy_list_image,HAUTEUR):
        # fonction qui gere le tire automatique des ennemie
        # entree : Aucune
        # sortie : Aucune

     
        frameCntProj = 2
        """ imageProj = [PhotoImage(file='image/Shuriken/Shuriken.gif',format = 'gif -index %i' %(i)) for i in range(frameCntProj)] """
        if len(self.enemy_list_object) > 1:

            max = len(self.enemy_list_object)-1

            rand=random.randint(0,max)

            coordsEnemyX = self.enemy_list_object[rand].get_position_x()
            coordsEnemyY = self.enemy_list_object[rand].get_position_y()
            

            

            if self.is_running == True:
                self.fenetre.FrameGauche.after(750,self.auto_tir,difficulty,enemy_list_image,HAUTEUR)

            projectile_enemy=project.Projectile(self,self.monde,self.fenetre,self.get_position_x,self.get_position_y,20,self.VITESSE,self.is_running)
            Projectile_enemy_last=self.fenetre.ZoneDeJeu.create_image(coordsEnemyX,coordsEnemyY, image = self.loadded_shuriken)
            self.Projectile_enemy.append(Projectile_enemy_last)
            projectile_enemy.deplacement_projectile_auto_tir(Projectile_enemy_last,coordsEnemyY,self.Projectile_enemy,HAUTEUR)


        else:
            max = len(self.enemy_list_object)-1

            rand=random.randint(0,max)

            coordsEnemyX = self.enemy_list_object[rand].get_position_x()
            coordsEnemyY = self.enemy_list_object[rand].get_position_y()

            Projectile_enemy_last=self.fenetre.ZoneDeJeu.create_image(coordsEnemyX,coordsEnemyY, image = self.loadded_lance)

            self.Projectile_enemy.append(Projectile_enemy_last)
            if self.is_running == True:
                self.fenetre.FrameGauche.after(750,self.auto_tir,difficulty,enemy_list_image,HAUTEUR)

            projectile_enemy=project.Projectile(self,self.monde,self.fenetre,self.get_position_x,self.get_position_y,20,self.VITESSE)
            projectile_enemy.deplacement_projectile_auto_tir(Projectile_enemy_last,coordsEnemyY,self.Projectile_enemy,HAUTEUR)

    def Super_auto_tir(self,difficulty,enemy_list_image,HAUTEUR):
        # fonction qui gere le tire automatique du super ennemie
        # entree : Aucune
        # sortie : Aucune
     
        frameCntProj = 2
        """ imageProj = [PhotoImage(file='image/Shuriken/Shuriken.gif',format = 'gif -index %i' %(i)) for i in range(frameCntProj)] """
        if len(self.super_ennemy_liste_object) > 1:

            max = len(self.super_ennemy_liste_object)-1

            rand=random.randint(0,max)

            coordsEnemyX = self.super_ennemy_liste_object[rand].get_position_x()
            coordsEnemyY = self.super_ennemy_liste_object[rand].get_position_y()
            

            

            if self.is_running == True:
                self.fenetre.FrameGauche.after(750,self.Super_auto_tir,difficulty,enemy_list_image,HAUTEUR)

            projectile_enemy=project.Projectile(self,self.monde,self.fenetre,self.get_position_x,self.get_position_y,20,self.VITESSE)
            Projectile_enemy_last=self.fenetre.ZoneDeJeu.create_image(coordsEnemyX,coordsEnemyY, image = self.loadded_shuriken)
            self.Projectile_enemy2.append(Projectile_enemy_last)
            projectile_enemy.deplacement_projectile_auto_tir(Projectile_enemy_last,coordsEnemyY,self.Projectile_enemy,HAUTEUR)


        else:
            max = len(self.super_ennemy_liste_object)-1
            if max>=0:

                rand=random.randint(0,max)

                coordsEnemyX = self.super_ennemy_liste_object[rand].get_position_x()
                coordsEnemyY = self.super_ennemy_liste_object[rand].get_position_y()

                Projectile_enemy_last=self.fenetre.ZoneDeJeu.create_image(coordsEnemyX,coordsEnemyY, image = self.loadded_lance)

                self.Projectile_enemy2.append(Projectile_enemy_last)

                if self.is_running == True:
                    self.fenetre.FrameGauche.after(750,self.Super_auto_tir,difficulty,enemy_list_image,HAUTEUR)

                projectile_enemy=project.Projectile(self,self.monde,self.fenetre,self.get_position_x,self.get_position_y,20,self.VITESSE,self.is_running)
                projectile_enemy.deplacement_projectile_auto_tir(Projectile_enemy_last,coordsEnemyY,self.Projectile_enemy2,HAUTEUR)

    def set_is_running(self):
        # fonction qui met  jour is running
        # entree : Aucune
        # sortie : Aucune
        self.is_running = False
        
    def get_liste_projectile(self):
        # fonction qui retourne la liste des projectiles des enemies
        # entree : Aucune
        # sortie :la liste des projectiles des ennemie
        return(self.Projectile_enemy)

    def get_liste_projectile2(self):
        # fonction qui retourne la liste des projectiles du super ennemie
        # entree : Aucune
        # sortie :la liste des projectiles du super ennemie
        return(self.Projectile_enemy2)

    def maj_enemy_liste_objet(self,x):
        # fonction qui met a jour la liste qui contient les objets des ennemies
        # entree : la liste qui contient les objets des ennemie
        # sortie : Aucune
        self.enemy_list_object=x

    def maj_super_ennemy_liste(self,x):
        # fonction qui met a jour la liste des supers ennemie
        # entree : la liste des supers ennemie
        # sortie : Aucune
        self.super_ennemy_liste_object=x

    def set_ennemy_liste(self,x):
        # fonction qui met a jour la liste des ennemie
        # entree : la liste des ennemie
        # sortie : Aucune
        self.super_ennemy=x

