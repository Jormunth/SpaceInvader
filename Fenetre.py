from tkinter import *
from vaisseau import *
from projectile import *
from protection import *

class Fenetre:
    def __init__(self,Largeur,Hauteur,tailleVaisseau):
        self.Largeur=Largeur
        self.Hauteur=Hauteur
        self.Vaisseau=None
        self.ZoneDeJeu=None
        self.mw=None
        self.projectile=[]
        self.rectangle=[]
        self.tailleVaisseau=tailleVaisseau
    


    def creer_fenetre(self,TailleVaisseau,POSX,POSY,Tk,Canvas,Button):
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

        FrameGauche = Frame(self.mw)
        FrameGauche.pack(side="left")


        self.ZoneDeJeu = Canvas(FrameGauche, width=1600, height =950)
        Terrain = PhotoImage(file = "image/terrainFond.png")
        self.ZoneDeJeu.create_image(0,0,anchor=NW,image=Terrain)
        self.ZoneDeJeu.pack(padx=10, pady=10)

        
        self.Vaisseau=self.ZoneDeJeu.create_rectangle(POSX,POSY,TailleVaisseau*2+POSX,TailleVaisseau*2+POSY,fill='maroon')
    
    def Clavier(self,event):
        u=0
        v=0
        coords_vaisseau=self.ZoneDeJeu.coords(self.Vaisseau)
        if event.keysym=='z' and coords_vaisseau[1]!=0:
            u=0
            v=-20
        if event.keysym=='s' and coords_vaisseau[3]!=self.Hauteur:
            u=0
            v=20
        if event.keysym=='q' and coords_vaisseau[0]!=0:
            u=-20
            v=0
        if event.keysym=='d' and coords_vaisseau[2]!=self.Largeur:
            u=20
            v=0
        self.ZoneDeJeu.move(self.Vaisseau,u,v)
    
    def creer_projectile(self,event):
        coords_vaisseau=self.ZoneDeJeu.coords(self.Vaisseau)
        projectile=Projectile((coords_vaisseau[0]+coords_vaisseau[2])/2,coords_vaisseau[1],20,20)
        self.projectile.append(self.ZoneDeJeu.create_oval(projectile.px-self.tailleVaisseau+projectile.rayon,projectile.py-self.tailleVaisseau+projectile.rayon,projectile.px+self.tailleVaisseau-projectile.rayon,projectile.py+self.tailleVaisseau-projectile.rayon,fill='purple'))

    def bouger(self,projectile,ma_fenetre):
        for t in self.projectile:
            coords_projectile=self.ZoneDeJeu.coords(t)
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
                self.ZoneDeJeu.delete(t)
                self.projectile.remove(t)
        self.ZoneDeJeu.after(100,ma_fenetre.bouger,projectile,ma_fenetre)

    def creer_rectangle(self,px,py,taille):
        self.rectangle.append(self.ZoneDeJeu.create_rectangle(px,py,px+2*taille,py+2*taille,fill='pink'))

    def collision_protection(self,px,py,taille,cpx,cpy):
        if cpx>=px-taille and cpx<=px+2*taille:
            if cpy<=py+taille*3:
                return(True)
        return(False)

    def forme1(self,x,y,taille_carré,nombre_carréx,nombre_carré_y,ma_fenetre):
        for i in range(nombre_carréx):
            for t in range(nombre_carré_y):
                ma_fenetre.creer_rectangle(x+i*2*taille_carré,y+t*2*taille_carré,taille_carré)
        

        

