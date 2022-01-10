from tkinter import *



def Clavier(event):
    global POSX,POSY
    print(event)
    touche=event.keysym   
    if touche=='z' and POSY-TailleVaisseau!=0:
        POSY-=20
    if touche=='s' and POSY+TailleVaisseau!=Hauteur:
        POSY+=20
    if touche=='q' and POSX-TailleVaisseau!=0:
        POSX-=20
    if touche=='d' and POSX+TailleVaisseau!=Largeur:
        POSX+=20
    Canevas.coords(Vaisseau,POSX-TailleVaisseau,POSY-TailleVaisseau,POSX+TailleVaisseau,POSY+TailleVaisseau)
    
def CreationProjectile(event):
    global POSX, POSY,r
    i=0
    PPX=POSX
    PPY=POSY
    projectile=Canevas.create_oval(POSX-TailleVaisseau+r,POSY-TailleVaisseau+r,POSX+TailleVaisseau-r,POSY+TailleVaisseau-r,fill='purple')
    Canevas.after(20,bouger,PPX,PPY,projectile,i)


def bouger(PPX,PPY,projectile,i):
    global vitesse_projectile, r
    for t in liste_protection :
        verif=collision_projectile(PPX,PPY,projectile,i,t.positionx,t.positiony,t.taille)
        if verif==True:
            Canevas.delete(projectile)
            t.supprimer_rectangle()
            liste_protection.remove(t)
        verif=False
    if PPY-TailleVaisseau+r-vitesse_projectile*i>0:
        Canevas.move(projectile,0,-vitesse_projectile)
        ''' Canevas.coords(projectile,PPX-TailleVaisseau+r,PPY-TailleVaisseau+r-vitesse_projectile*i,PPX+TailleVaisseau-r,PPY+TailleVaisseau-r-vitesse_projectile*i) '''
        Canevas.after(100,bouger,PPX,PPY,projectile,i+1)
    else:
        Canevas.delete(projectile)


def collision_projectile(PPX,PPY,projectile,i,tx,ty,tt):
    if PPX-TailleVaisseau+r>=tx and PPX+TailleVaisseau-r<=tt*2+tx:
        if PPY-TailleVaisseau+r-vitesse_projectile*i<tt*2+ty:
            return(True)
    return(False)

mw=Tk()
mw.title("Vaisseau")

class Protection:
    def __init__(self,positionx,positiony,taille,Canevas):
        self.positionx=positionx
        self.positiony=positiony
        self.taille=taille
        self.Canevas=Canevas
        self.rectangle = None
    def creer_rectangle(self):
        self.rectangle = self.Canevas.create_rectangle(self.positionx,self.positiony,self.taille*2+self.positionx,self.taille*2+self.positiony,fill='pink')
    def supprimer_rectangle(self):
        if self.rectangle:
            self.Canevas.delete(self.rectangle)
        
        
        
        
vitesse_projectile=5
r=15
Largeur=480
Hauteur=320
POSX=Largeur/2
POSY=Hauteur/2
positionx_protection=Largeur/2
positiony_protection=Hauteur/2
TailleVaisseau=20
TailleProtection=15

Canevas=Canvas(mw,width=Largeur,height=Hauteur,bg='white')

p1=Protection(positionx_protection,positiony_protection,15,Canevas)
p2=Protection(20,40,15,Canevas)

liste_protection=[p1,p2]


p1.creer_rectangle()
p2.creer_rectangle()


Vaisseau=Canevas.create_rectangle(POSX,POSY,TailleVaisseau*2+POSX,TailleVaisseau*2+POSY,fill='maroon')
Canevas.focus_set()

Canevas.bind('<Key>',Clavier)
Canevas.bind('<Button-1>',CreationProjectile)

Canevas.pack(padx=5,pady=5)

ButtonQuit=Button(mw,text="Quitter",fg='black',command=mw.destroy)
ButtonQuit.pack()

mw.mainloop()