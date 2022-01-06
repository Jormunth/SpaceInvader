from tkinter import *



def Clavier(event):
    global POSX,POSY
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
    verif=collision_projectile(PPX,PPY,projectile,i)
    if verif==True:
        Canevas.delete(projectile)
    elif PPY-TailleVaisseau+r-vitesse_projectile*i>0:
        Canevas.coords(projectile,PPX-TailleVaisseau+r,PPY-TailleVaisseau+r-vitesse_projectile*i,PPX+TailleVaisseau-r,PPY+TailleVaisseau-r-vitesse_projectile*i)
        Canevas.after(100,bouger,PPX,PPY,projectile,i+1)
    else:
        Canevas.delete(projectile)


def collision_projectile(PPX,PPY,projectile,i):
    if PPX-TailleVaisseau+r>=positionx_protection+20 and PPX+TailleVaisseau-r<=TailleProtection*2+positionx_protection+20:
        if PPY-TailleVaisseau+r-vitesse_projectile*i<TailleProtection*2+positiony_protection+20:
            Canevas.delete(protection)
            return(True)
    return(False)

mw=Tk()
mw.title("Vaisseau")

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

liste_protection_x=[0,20,25,0,20,25]

protection=Canevas.create_rectangle(POSX+20,POSY+20,TailleProtection*2+POSX+20,TailleProtection*2+POSY+20,fill='pink')

Vaisseau=Canevas.create_rectangle(POSX,POSY,TailleVaisseau*2+POSX,TailleVaisseau*2+POSY,fill='maroon')
Canevas.focus_set()

Canevas.bind('<Key>',Clavier)
Canevas.bind('<Button-1>',CreationProjectile)

Canevas.pack(padx=5,pady=5)

ButtonQuit=Button(mw,text="Quitter",fg='black',command=mw.destroy)
ButtonQuit.pack()

mw.mainloop()