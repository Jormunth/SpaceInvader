from tkinter import *
from vaisseau import *
from projectile import *
from protection import *
import enemy as e
import random,math
from PIL import Image, ImageTk
       
class Tkinter:
    '''
    test
    '''
    def __init__(self,Largeur,Hauteur,tailleVaisseau):
        self.Largeur=Largeur
        self.Hauteur=Hauteur
        self.Vaisseau=None
        self.ZoneDeJeu=None
        self.mw=None
        self.projectile=[]
        self.rectangle=[]
        self.tailleVaisseau=tailleVaisseau
        self.myEnemyList=[]
        self.myEnemy = []
        self.FrameGauche=None
        self.ProjectileEnemy = []
        self.vie=3

    def create_background(self):
        self.loadTerrain = Image.open("image/terrainFond.png")
        self.loaddedTerrain =ImageTk.PhotoImage(self.loadTerrain)
        self.Terrain = self.ZoneDeJeu.create_image(0,0,anchor=NW,image= self.loaddedTerrain)
    


    def creer_fenetre(self,Tk,Canvas,Button):
        self.mw=Tk()
        self.mw.title('Space Invader')
        self.mw['bg']='grey'
        self.mw.geometry('1900x1008+0+0')

        FrameDroit = Frame(self.mw)
        FrameDroit.pack(side="right")

        ButtonJouer = Button(FrameDroit, text="Jouer", height=5, width=30,)
        ButtonJouer.pack(pady=50)

        ButtonParametre = Button(FrameDroit, text="Paramètre", height=5, width=30, command=print("paramètre"))
        ButtonParametre.pack(pady=50)

        ButtonQuitter = Button(FrameDroit, text="Quitter", height=5, width=30, command=self.mw.destroy)
        ButtonQuitter.pack(side='bottom', pady=50)

        self.FrameGauche = Frame(self.mw)
        self.FrameGauche.pack(side="left")


        self.ZoneDeJeu = Canvas(self.FrameGauche, width=self.Largeur, height = self.Hauteur)
        """ Terrain = PhotoImage(file = "image/terrainFond.png") """
        """ self.ZoneDeJeu.create_image(0,0,anchor=NW,image=Terrain) """
        self.ZoneDeJeu.pack(padx=10, pady=10)

    def creerVaisseau(self,TailleVaisseau,POSX,POSY):
        self.Vaisseau=self.ZoneDeJeu.create_rectangle(POSX,POSY,TailleVaisseau*2+POSX,TailleVaisseau*2+POSY,fill='maroon')

    def creerEnemy(self,difficulty,DY):
                
        tag = 0
        Placement = difficulty+1
        nbEnnemie = difficulty
        vitesse =  7+(difficulty/2)

        """ frameCntEnemie = 5
        imageEnnemie = [PhotoImage(file='image/Ninja/animation/runRight_2.gif',format = 'gif -index %i' %(i)) for i in range(frameCntEnemie)] """
        
        self.loadEnemy = Image.open("image/Ninja/Ninja.png")
        self.loaddedEnemy =ImageTk.PhotoImage(self.loadEnemy)
        

        while nbEnnemie >= 1:
            
            tag += 1
            X = (self.Largeur/Placement)*tag
            Y = self.Hauteur/20

            self.myEnemyList.append(e.Enemy(tag, vitesse, X, Y, DY))
            self.myEnemy.append(self.ZoneDeJeu.create_image(X,Y, image = self.loaddedEnemy))
            """ self.myEnemy.append(self.ZoneDeJeu.create_line(X, Y, X, Y+30,width=6)) """

            nbEnnemie -= 1

        
    def deplacementEnemy(self,vitesse,DY,difficulty):
        
        DX = vitesse
        DY = 0

        XtremG = self.myEnemyList[0].getPosX()
        XtremD = self.myEnemyList[-1].getPosX()

        XtremG += DX
        XtremD += DX    


        if XtremD + 20 > self.Largeur:
            XtremD= 2*(self.Largeur) - XtremD
            vitesse = -DX
            DY = 60

        if XtremG -20 < 0:
            XtremG = -XtremG
            vitesse = -DX
            DY = 60

        for i,val in enumerate(self.myEnemy):
            self.ZoneDeJeu.move(self.myEnemy[i],DX,DY)
            self.myEnemyList[i].deplacer(self.myEnemyList[i].getPosX()+DX,self.myEnemyList[i].getPosY()+DY)


        self.FrameGauche.after(20,self.deplacementEnemy,vitesse,DY,difficulty)

        
    def autoTir(self,difficulty,ma_fenetre):

        
        frameCntProj = 2
        """ imageProj = [PhotoImage(file='image/Shuriken/Shuriken.gif',format = 'gif -index %i' %(i)) for i in range(frameCntProj)] """


        max = len(self.myEnemy)-1

        rand=random.randint(0,max)

        coordsEnemyX = self.myEnemyList[rand].getPosX()
        coordsEnemyY = self.myEnemyList[rand].getPosY()
        
        self.loadShuriken = Image.open("image/Shuriken/Shuriken.gif")
        self.loaddedShuriken =ImageTk.PhotoImage(self.loadShuriken)
        ProjectileEnemylast=self.ZoneDeJeu.create_image(coordsEnemyX,coordsEnemyY, image = self.loaddedShuriken)

        self.ProjectileEnemy.append(ProjectileEnemylast)
        self.FrameGauche.after(750,self.autoTir,difficulty,ma_fenetre)

        self.deplacementProjectEautoTir(ProjectileEnemylast,coordsEnemyY,ma_fenetre)

    def deplacementProjectEautoTir(self,ProjectileEnemylast,coordsEnemyY,ma_fenetre):

        
        for t in self.ProjectileEnemy:
            coords_tir = self.ZoneDeJeu.coords(t)
            
            for o in self.rectangle:
                coords_protection=self.ZoneDeJeu.coords(o)
                verif=ma_fenetre.collision_enemy_protection(coords_protection[0],coords_protection[1],18,coords_tir[0],coords_tir[1])
                if verif ==True:
                    self.ZoneDeJeu.delete(o)
                    self.rectangle.remove(o)
                    self.ZoneDeJeu.delete(t)
                    if t in self.ProjectileEnemy:
                        self.ProjectileEnemy.remove(t)

            if coords_tir[1]<self.Hauteur:
                self.ZoneDeJeu.move(ProjectileEnemylast, 0, 20)
                
            else:
                if t in self.ProjectileEnemy:
                    self.ZoneDeJeu.delete(t)
                    self.ProjectileEnemy.remove(t)

        self.FrameGauche.after(20,self.deplacementProjectEautoTir,ProjectileEnemylast,coordsEnemyY,ma_fenetre)


        
        


    def Clavier(self,event):
        u=0
        v=0
        coords_vaisseau=self.ZoneDeJeu.coords(self.Vaisseau)
        if event.keysym=='z' and coords_vaisseau[1]>0:
            u=0
            v=-20
        if event.keysym=='s' and coords_vaisseau[3]<self.Hauteur+10:
            u=0
            v=20
        if event.keysym=='q' and coords_vaisseau[0]>0:
            u=-20
            v=0
        if event.keysym=='d' and coords_vaisseau[2]<self.Largeur:
            u=20
            v=0
        self.ZoneDeJeu.move(self.Vaisseau,u,v)
    
    def creer_projectile(self,event):
        coords_vaisseau=self.ZoneDeJeu.coords(self.Vaisseau)
        projectile=Projectile((coords_vaisseau[0]+coords_vaisseau[2])/2,coords_vaisseau[1],20,20)
        self.projectile.append(self.ZoneDeJeu.create_oval(projectile.px-self.tailleVaisseau+projectile.rayon,projectile.py-self.tailleVaisseau+projectile.rayon,projectile.px+self.tailleVaisseau-projectile.rayon,projectile.py+self.tailleVaisseau-projectile.rayon,fill='purple'))

    def bouger(self,projectile,ma_fenetre,difficulty):
        for t in self.projectile:
            coords_projectile=self.ZoneDeJeu.coords(t)
            k=0
            for i in range(len(self.myEnemyList)):
                verif_ennemy=ma_fenetre.collision_projectilev_ennemi(self.myEnemyList[k].getPosX()-3,self.myEnemyList[k].getPosY(),39/2,coords_projectile[0],coords_projectile[1])
                if verif_ennemy ==True:
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
                verif=ma_fenetre.collision_protection(coords_protection[0],coords_protection[1],18,coords_projectile[0],coords_projectile[1])
                if verif ==True:
                    self.ZoneDeJeu.delete(o)
                    self.rectangle.remove(o)
                    if t in self.projectile:
                        self.ZoneDeJeu.delete(t)
                        self.projectile.remove(t)
            if coords_projectile[1]>0:
                self.ZoneDeJeu.move(t,0,-projectile.vitesse)
            else:
                if t in self.projectile:
                    self.ZoneDeJeu.delete(t)
                    self.projectile.remove(t)
        self.ZoneDeJeu.after(100,ma_fenetre.bouger,projectile,ma_fenetre,difficulty)

    def creer_rectangle(self,px,py,taille):
        self.rectangle.append(self.ZoneDeJeu.create_rectangle(px,py,px+2*taille,py+2*taille,fill='pink'))

    def collision_protection(self,px,py,taille,cpx,cpy):
        if cpx>=px-taille and cpx<=px+2*taille:
            if cpy<=py+taille*3:
                return(True)
        return(False)

    def collision_enemy_protection(self,px,py,taille,cpx,cpy):
        if cpx>=px-taille and cpx<=px+2*taille:
            if cpy>=py:
                return(True)
        return(False)

    def forme1(self,x,y,taille_carré,nombre_carréx,nombre_carré_y,ma_fenetre):
        for i in range(nombre_carréx):
            for t in range(nombre_carré_y):
                ma_fenetre.creer_rectangle(x+i*2*taille_carré,y+t*2*taille_carré,taille_carré)

    def collision_projectilev_ennemi(self,px,py,taille,cpx,cpy):
        if cpx>=px-taille and cpx<=px+2*taille:
            if cpy<=py+taille*3:
                return(True)
        return(False)
        

        

