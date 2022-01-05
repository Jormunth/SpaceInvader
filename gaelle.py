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
    Canevas.after(20,Bouger,PPX,PPY,projectile,i)


def Bouger(PPX,PPY,projectile,i):
    global vitesse_projectile, r
    if PPY-TailleVaisseau+r-15*i>-Hauteur-1000:
        Canevas.coords(projectile,PPX-TailleVaisseau+r,PPY-TailleVaisseau+r-vitesse_projectile*i,PPX+TailleVaisseau-r,PPY+TailleVaisseau-r-vitesse_projectile*i)
        print(PPY-TailleVaisseau+r-15*i)
        Canevas.after(100,Bouger,PPX,PPY,projectile,i+1)
    else:
        Canevas.delete(projectile)
    

mw=Tk()
mw.title("Vaisseau")

vitesse_projectile=3
r=15
Largeur=480
Hauteur=320
POSX=Largeur/2
POSY=Hauteur/2
TailleVaisseau=20

Canevas=Canvas(mw,width=Largeur,height=Hauteur,bg='white')


Vaisseau=Canevas.create_rectangle(POSX,POSY,TailleVaisseau*2+POSX,TailleVaisseau*2+POSY,fill='maroon')
Canevas.focus_set()

Canevas.bind('<Key>',Clavier)
Canevas.bind('<Button-1>',CreationProjectile)

Canevas.pack(padx=5,pady=5)

ButtonQuit=Button(mw,text="Quitter",fg='black',command=mw.destroy)
ButtonQuit.pack()

mw.mainloop()