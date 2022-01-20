from tkinter import *
import partie as play
import Fenetre as ctk


WINDOW_WIDTH = 2044
WINDOW_HEIGHT = 1072
CANVAS_WIDTH = 1800
CANVAS_HEIGHT = 1000

VIE = 3
DIFFICULTEE = 18
DY = 60
VITESSE = 1

ma_fenetre=ctk.Fenetre(WINDOW_WIDTH, WINDOW_HEIGHT, CANVAS_WIDTH, CANVAS_HEIGHT, VIE, DIFFICULTEE, DY, VITESSE)
ma_fenetre.demarrer_partie()

