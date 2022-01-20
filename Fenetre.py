from ast import alias
from tkinter import *
from vaisseau import *
from projectile import *
from protection import *
import enemy as e
import partie as p
from PIL import Image, ImageTk

class Fenetre:

    def __init__(self,LARGEUR,HAUTEUR,CANVAS_WIDTH,CANVAS_HEIGHT,VIE,DIFFICULTEE,DY,VITESSE):
        self.LARGEUR=LARGEUR
        self.HAUTEUR=HAUTEUR
        self.CANVAS_WIDTH = CANVAS_WIDTH
        self.CANVAS_HEIGHT = CANVAS_HEIGHT
        self.DIFFICULTEE = DIFFICULTEE
        self.DY = DY
        self.VITESSE = VITESSE
        self.ZoneDeJeu=None
        self.mw=None
        self.FrameGauche=None
        self.loadTerrain=None
        self.loaddedTerrain=None
        self.loadKatana=None
        self.loaddedKatana=None
        self.Terrain=None
        self.VIE=VIE
        self.score=0
        self.txt_VIE=None
        self.Texte=None
        self.Texte_score=None
        self.partie = p.Partie(self, self.DIFFICULTEE, self.DY, self.VITESSE,self.LARGEUR,self.HAUTEUR, CANVAS_WIDTH, CANVAS_HEIGHT)
        self.creer_fenetre()

    def creer_fenetre(self):
        self.mw=Tk()
        self.mw.title('Space Invader')
        self.mw['bg']='grey'
        self.mw.geometry(f'{self.LARGEUR}x{self.HAUTEUR}+0+0')

        FrameDroit = Frame(self.mw)
        FrameDroit.pack(side="right")

        ButtonJouer = Button(FrameDroit, text="Jouer", height=5, width=30,command=self.partie.lancementPartie)
        """command=lambda : self.partie.lancementPartie(self.DIFFICULTEE, self.DY, self.VITESSE)"""
        ButtonJouer.pack(pady=50)
        """command=lancementParti(1600,950)"""

        ButtonParametre = Button(FrameDroit, text="Paramètre", height=5, width=30, command=print("paramètre"))
        ButtonParametre.pack(pady=50)

        ButtonQuitter = Button(FrameDroit, text="Quitter", height=5, width=30, command=self.mw.destroy)
        ButtonQuitter.pack(side='bottom', pady=50)

        self.FrameGauche = Frame(self.mw)
        self.FrameGauche.pack(side="left")
        
        self.Texte_VIE=StringVar()
        self.Texte_VIE.set('VIE : ' + str(self.VIE))
        self.Texte_score=StringVar()
        self.Texte_score.set('Score : ' + str(self.score))
        #print(self.Texte_VIE.get())
        Label(self.FrameGauche,textvariable=self.Texte_VIE).pack(padx=1, pady=1)
        Label(self.FrameGauche,textvariable=self.Texte_score).pack(padx=1, pady=1)
        
        
        self.ZoneDeJeu = Canvas(self.FrameGauche, width=self.CANVAS_WIDTH, height = self.CANVAS_HEIGHT)
        self.ZoneDeJeu.pack(padx=10, pady=10)
           
        self.loadEnemy = Image.open("image/Ninja/Ninja.png")
        self.loaddedEnemy =ImageTk.PhotoImage(self.loadEnemy)
        
        self.loadShuriken = Image.open("image/Shuriken/Shuriken.png")
        self.loaddedShuriken =ImageTk.PhotoImage(self.loadShuriken)

        self.create_background_image()

    def create_background_image(self):
        self.loadKatana = Image.open("image/Katana/Katana.png")
        self.loaddedKatana =ImageTk.PhotoImage(self.loadKatana)
        self.loadBarriere = Image.open("image/Fence.png")
        self.loaddedBarriere =ImageTk.PhotoImage(self.loadBarriere)
        self.Terrain = self.ZoneDeJeu.create_image(0,0,anchor=NW,image= self.loaddedTerrain)
    

    def demarrer_partie(self):
        
        self.mw.mainloop()