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




"""         for t in self.projectile:
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
                if t in self.projectile: """


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



def SuperAutoTir(self,difficulty,enemy_list_image,HAUTEUR):

     
        frameCntProj = 2
        """ imageProj = [PhotoImage(file='image/Shuriken/Shuriken.gif',format = 'gif -index %i' %(i)) for i in range(frameCntProj)] """
        if len(self.super_ennemy_liste_object) > 1:

            max = len(self.super_ennemy_liste_object)-1

            rand=random.randint(0,max)
            print(len(self.super_ennemy_liste_object),max,rand)

            coordsEnemyX = self.super_ennemy_liste_object[rand].getPosX()
            coordsEnemyY = self.super_ennemy_liste_object[rand].getPosY()
            

            

            
            self.fenetre.FrameGauche.after(750,self.autoTir,difficulty,enemy_list_image,HAUTEUR)

            projectile_enemy=project.Projectile(self,self.monde,self.fenetre,self.getPosX,self.getPosY,20,self.VITESSE)
            ProjectileEnemylast=self.fenetre.ZoneDeJeu.create_image(coordsEnemyX,coordsEnemyY, image = self.loaddedShuriken)
            self.ProjectileEnemy.append(ProjectileEnemylast)
            projectile_enemy.deplacementProjectEautoTir(ProjectileEnemylast,coordsEnemyY,self.ProjectileEnemy,HAUTEUR)


        else:
            max = len(self.super_ennemy_liste_object)-1

            rand=random.randint(0,max)

            coordsEnemyX = self.super_ennemy_liste_object[rand].getPosX()
            coordsEnemyY = self.super_ennemy_liste_object[rand].getPosY()

            ProjectileEnemylast=self.fenetre.ZoneDeJeu.create_image(coordsEnemyX,coordsEnemyY, image = self.loaddedLance)

            self.ProjectileEnemy.append(ProjectileEnemylast)
            self.fenetre.FrameGauche.after(750,self.SuperAutoTir,difficulty,enemy_list_image,HAUTEUR)

            projectile_enemy=project.Projectile(self,self.monde,self.fenetre,self.getPosX,self.getPosY,20,self.VITESSE)
            projectile_enemy.deplacementProjectEautoTir(ProjectileEnemylast,coordsEnemyY,self.ProjectileEnemy,HAUTEUR)



 def deplacementSuperEnemy(self,VITESSE,DY,enemy_list_image,LARGEUR,rectangle,CANVAS_WIDTH,CANVAS_HEIGHT):
            
            DX = VITESSE
            DY = 0
            most_right = 0
            most_left = CANVAS_WIDTH

            for ennemie in self.super_ennemy_liste_object:
                ennemie_pos_x = ennemie.getPosX()
                if ennemie_pos_x > most_right:
                    most_right = ennemie_pos_x

            for ennemie in self.super_ennemy_liste_object:
                ennemie_pos_x = ennemie.getPosX()
                if ennemie_pos_x < most_left:
                    most_left = ennemie_pos_x

            """ most_left = enemy_list_object[0].getPosX()
            most_right = enemy_list_object[-1].getPosX() """

            posy=self.enemy_list_object[-1].getPosY()

            most_left += DX
            most_right += DX    

            if posy >= CANVAS_HEIGHT-30:
                k=0
                for i in range(len(self.super_ennemy_liste_object)):
                    del self.myEnemyList[k]
                    self.ZoneDeJeu.delete(self.myEnemy[k])
                    del self.myEnemy[k]
                    

            else:
                for i in range(len(self.super_ennemy_liste_object)):
                    posx=self.super_ennemy_liste_object[i].getPosX()
                    posy=self.super_ennemy_liste_object[i].getPosY()
                    for o in rectangle:
                        coords_protection=self.ZoneDeJeu.coords(o)
                        verif_collision=self.fenetre.collision_enemy_protection(coords_protection[0],coords_protection[1],32/2,posx,posy)
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
                    self.super_ennemy_liste_object[i].deplacer(self.super_ennemy_liste_object[i].getPosX()+DX,self.super_ennemy_liste_object[i].getPosY()+DY)


            self.fenetre.FrameGauche.after(20,self.deplacementEnemy,VITESSE,self.DY,enemy_list_image,LARGEUR,rectangle,CANVAS_WIDTH,CANVAS_HEIGHT)

