from tkinter import *
import partie as play
import Fenetre as ctk


WINDOW_WIDTH = 1900
WINDOW_HEIGHT = 1008
VIE = 3
DIFFICULTEE = 5
DY = 60
VITESSE = 5

ma_fenetre=ctk.Fenetre(WINDOW_WIDTH, WINDOW_HEIGHT,VIE,DIFFICULTEE,DY,VITESSE)
ma_fenetre.demarrer_partie()

