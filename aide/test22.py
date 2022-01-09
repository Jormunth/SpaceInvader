from tkinter import *
import time
import os
mw = Tk()
FrameGauche = Frame(mw)
FrameGauche.pack(side="left")
ZoneDeJeu = Canvas(FrameGauche, width=1600, height =950, bg="white")
ZoneDeJeu.pack(padx=10, pady=10)
frameCnt = 6
immmage = [PhotoImage(file='image/Ninja/animation/runRight_2.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = immmage[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    Enemy=ZoneDeJeu.create_image(800,475, image = frame)
    mw.after(100, update, ind)
Enemy=ZoneDeJeu.create_image(800,475, image = immmage[0])

FrameGauche.after(0, update, 0)
mw.mainloop()