from tkinter import *
import partie as play
import Fenetre as ctk


WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
CANVAS_WIDTH = 1600
CANVAS_HEIGHT = 900

VIE = 3
DIFFICULTEE = 6

DY = 60
VITESSE = 1

ma_fenetre=ctk.Fenetre(WINDOW_WIDTH, WINDOW_HEIGHT, CANVAS_WIDTH, CANVAS_HEIGHT, VIE, DIFFICULTEE, DY, VITESSE)
ma_fenetre.demarrer_partie()

