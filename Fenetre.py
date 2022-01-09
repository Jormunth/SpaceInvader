from tkinter import *
from vaisseau import *
from projectile import *
from protection import *

class Fenetre:
    def __init__(self,Largeur,Hauteur):
        self.Largeur=Largeur
        self.Hauteur=Hauteur
        self.Vaisseau=None
        self.ma_fenetre2=None
        self.mw=None
        self.projectile=[]
        self.rectangle=[]
        #self.bind=None
    
    def creer_fenetre(self,TailleVaisseau,POSX,POSY,Tk,Canvas,Button):
        self.mw=Tk()
        self.mw.title("Vaisseau2")
        self.ma_fenetre2=Canvas(self.mw,width=self.Largeur,height=self.Hauteur,bg='white')
        self.ma_fenetre2.pack(padx=5,pady=5)
        self.Vaisseau=self.ma_fenetre2.create_rectangle(POSX,POSY,TailleVaisseau*2+POSX,TailleVaisseau*2+POSY,fill='maroon')
        ButtonQuit=Button(self.mw,text="Quitter",fg='black',command=self.mw.destroy)
        ButtonQuit.pack()
        
    
    def Clavier(self,event):
        u=0
        v=0
        coords_vaisseau=self.ma_fenetre2.coords(self.Vaisseau)
        if event.keysym=='z' and vaisseau.POSY!=0:
            u=0
            v=-20
        if event.keysym=='s' and vaisseau.POSY+2*vaisseau.TailleVaisseau!=self.Hauteur:
            u=0
            v=20
        if event.keysym=='q' and vaisseau.POSX!=0:
            u=-20
            v=0
        if event.keysym=='d' and vaisseau.POSX+2*vaisseau.TailleVaisseau!=self.Largeur:
            u=20
            v=0
        vaisseau.deplacer(u,v)
        self.ma_fenetre2.move(self.Vaisseau,u,v)
    
    def creer_projectile(self,event):
        projectile=Projectile(vaisseau.POSX+vaisseau.TailleVaisseau,vaisseau.POSY,15,20)
        self.projectile.append(self.ma_fenetre2.create_oval(projectile.px-vaisseau.TailleVaisseau+projectile.rayon,projectile.py-vaisseau.TailleVaisseau+projectile.rayon,projectile.px+vaisseau.TailleVaisseau-projectile.rayon,projectile.py+vaisseau.TailleVaisseau-projectile.rayon,fill='purple'))

    def bouger(self,projectile):
        for t in self.projectile:
            coords_projectile=self.ma_fenetre2.coords(t)
            if coords_projectile[1]>0:
                self.ma_fenetre2.move(t,0,-projectile.vitesse)
            else:
                self.ma_fenetre2.delete(t)
                self.projectile.remove(t)
        self.ma_fenetre2.after(100,ma_fenetre.bouger,projectile)

    def creer_rectangle(self,px,py,taille):
        self.rectangle.append(self.ma_fenetre2.create_rectangle(px,py,px+2*taille,py+2*taille,fill='pink'))
        


ma_fenetre=Fenetre(480,320)
vaisseau=Vaisseau(240,160,20)

ma_fenetre.creer_fenetre(vaisseau.TailleVaisseau,vaisseau.POSX,vaisseau.POSY,Tk,Canvas,Button)
#je créer ma fenêtre dans ma classe, et la stocke dans ma_fenetre2

ma_fenetre.ma_fenetre2.focus_force()

ma_fenetre.ma_fenetre2.bind('<Key>',ma_fenetre.Clavier)
ma_fenetre.ma_fenetre2.bind('<Button-1>',ma_fenetre.creer_projectile)

p2=Protection(20,40,15)
ma_fenetre.creer_rectangle(p2.positionx,p2.positiony,p2.taille)

projectile=Projectile(vaisseau.POSX+vaisseau.TailleVaisseau,vaisseau.POSY,15,15)

ma_fenetre.ma_fenetre2.after(20,ma_fenetre.bouger,projectile)


ma_fenetre.mw.mainloop()