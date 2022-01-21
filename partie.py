from tkinter import *
from vaisseau import *
from projectile import *
from protection import *
import monde as m
import enemy as e
import Fenetre as ctk
from PIL import Image, ImageTk


class Partie:

    def __init__(self, fenetre,DIFFICULTEE,DY,VITESSE,LARGEUR,HAUTEUR,CANVAS_WIDTH,CANVAS_HEIGHT,controle_up,controle_down,controle_left,controle_right,controle_shot):
        self.DIFFICULTEE = DIFFICULTEE
        self.DY = DY
        self.VITESSE = VITESSE
        self.fenetre = fenetre
        self.LARGEUR = LARGEUR
        self.HAUTEUR = HAUTEUR
        self.CANVAS_WIDTH = CANVAS_WIDTH
        self.CANVAS_HEIGHT = CANVAS_HEIGHT
        self.loadTerrain = None
        self.loaddedTerrain = None
        self.controle_up=controle_up
        self.controle_down=controle_down
        self.controle_left=controle_left
        self.controle_right=controle_right
        self.controle_shot=controle_shot
        

    def lancementPartie(self):
        
        self.fenetre.ZoneDeJeu.delete('all')


        self.loadTerrain = Image.open("image/terrainFond.png")
        self.loaddedTerrain =ImageTk.PhotoImage(self.loadTerrain)
        self.Terrain = self.fenetre.ZoneDeJeu.create_image(0,0,anchor=NW,image= self.loaddedTerrain)

        self.fenetre.ZoneDeJeu.focus_force()
        
        """
        -AJOUTER LE RESET DU SCORE ET DES VIE DANS LE LABEL DE LA CLASSE TK
        """

        monde=m.Monde(self.fenetre,self.DIFFICULTEE, self.DY,self.VITESSE,self.LARGEUR,self.HAUTEUR,self.CANVAS_WIDTH,self.CANVAS_HEIGHT,self.controle_up, self.controle_down, self.controle_left, self.controle_right,self.controle_shot)