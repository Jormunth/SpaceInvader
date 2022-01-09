from tkinter import *
from vaisseau import *
from projectile import *

class Fenetre:
    def __init__(self,Largeur,Hauteur):
        self.Largeur=Largeur
        self.Hauteur=Hauteur
        self.Vaisseau=None
        self.ma_fenetre2=None
        self.mw=None
        self.projectile=None
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
        self.ma_fenetre2.move(self.Vaisseau,u,v)
    
    def creer_projectile(self):
        coords_vaisseau=self.ma_fenetre2(self.Vaisseau)

        projectile=Projectile(20,20,5)
        self.projectile=self.ma_fenetre2.create_oval(projectile.px-vaisseau.TailleVaisseau+projectile.rayon,projectile.py-vaisseau.TailleVaisseau+projectile.rayon,projectile.px+vaisseau.TailleVaisseau-projectile.rayon,projectile.py+vaisseau.TailleVaisseau-projectile.rayon,fill='purple')
        return(1)


ma_fenetre=Fenetre(480,320)
vaisseau=Vaisseau(240,160,20)

ma_fenetre.creer_fenetre(vaisseau.TailleVaisseau,vaisseau.POSX,vaisseau.POSY,Tk,Canvas,Button)
#je créer ma fenêtre dans ma classe, et la stocke dans ma_fenetre2

ma_fenetre.ma_fenetre2.focus_force()

ma_fenetre.ma_fenetre2.bind('<Key>',ma_fenetre.Clavier)
ma_fenetre.ma_fenetre2.bind('<Button-1>',ma_fenetre.creer_projectile)


ma_fenetre.mw.mainloop()