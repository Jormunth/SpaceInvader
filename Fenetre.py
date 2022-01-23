# gere toutes la partie interface utilisateur de tkinter
# Mathieu Zeman / Gaelle Leroux
# realise entre decembre 2021 et janvier 2022 

from tkinter import *
from tkinter import messagebox
from tkinter.tix import Tree
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
        self.LOAD_TERRAIN=None
        self.LOADDED_TERRAIN=None
        self.LOAD_KATANA=None
        self.LOADDED_KATANA=None
        self.Terrain=None
        self.VIE=VIE
        self.score=0
        self.txt_VIE=None
        self.Texte=None
        self.Texte_score=None
        self.Texte_VIE=None
        self.partie = None
        self.controle_up='z'
        self.controle_down='s'
        self.controle_left='q'
        self.controle_right='d'
        self.controle_shot='space'

        self.creer_fenetre()

    def creer_fenetre(self):
        # fonction qui creer la fenetre principal ainsi que son contenu
        # entree : Aucune
        # sortie : Aucune

        self.mw=Tk()
        self.mw.title('Space Invader')
        self.mw['bg']='grey'
        self.mw.geometry(f'{self.LARGEUR}x{self.HAUTEUR}+0+0')

        FrameDroit = Frame(self.mw)
        FrameDroit.pack(side="right")

        ButtonJouer = Button(FrameDroit, text="Jouer", height=5, width=30,command=self.create_parti)
        ButtonJouer.pack(pady=50)

        ButtonQuitter = Button(FrameDroit, text="Quitter", height=5, width=30, command=self.mw.destroy)
        ButtonQuitter.pack(side='bottom', pady=50)

        self.FrameGauche = Frame(self.mw)
        self.FrameGauche.pack(side="left")




        barremenu = Menu(self.mw)
        self.mw.config(menu = barremenu)
        option_menu = Menu(barremenu, tearoff = 0, )
        barremenu.add_cascade(label = "Option", menu = option_menu)
        option_menu.add_command(label = "Contrôle", command = self.controle)
        option_menu.add_command(label = "Option de jeu", command = self.fenetre_parametre)
        option_menu.add_separator()
        option_menu.add_command(label = "Quitter le logiciel", command = self.quitter)

        apropos = Menu(barremenu, tearoff = 0)
        barremenu.add_cascade(label = "À Propos", menu = apropos)
        apropos.add_command(label = "À Propos", command = self.a_propos)





        self.Texte_VIE=StringVar()
        self.Texte_VIE.set('VIE : ' + str(self.VIE))
        self.Texte_score=StringVar()
        self.Texte_score.set('Score : ' + str(self.score))
        #print(self.Texte_VIE.get())
        Label(self.FrameGauche,textvariable=self.Texte_VIE).pack(padx=1, pady=1)
        Label(self.FrameGauche,textvariable=self.Texte_score).pack(padx=1, pady=1)
        
        
        self.ZoneDeJeu = Canvas(self.FrameGauche, width=self.CANVAS_WIDTH, height = self.CANVAS_HEIGHT)
        self.ZoneDeJeu.pack(padx=10, pady=10)
           
        self.lOAD_ENEMY = Image.open("image/Ninja/Ninja.png")
        self.lOADDED_ENEMY =ImageTk.PhotoImage(self.lOAD_ENEMY)
        
        self.lOAD_SHURIKEN = Image.open("image/Shuriken/Shuriken.png")
        self.lOADDED_SHURIKEN =ImageTk.PhotoImage(self.lOAD_SHURIKEN)

        self.create_background_image()

    def create_background_image(self):
        # fonction qui affiche l'image de fonds
        # entree : Aucune
        # sortie : Aucune
        self.LOAD_TERRAIN = Image.open("image/terrainFond.png")
        self.LOADDED_TERRAIN =ImageTk.PhotoImage(self.LOAD_TERRAIN)
        self.LOAD_KATANA = Image.open("image/Katana/Katana.png")
        self.LOADDED_KATANA =ImageTk.PhotoImage(self.LOAD_KATANA)
        self.LOAD_BARRIERE = Image.open("image/Fence.png")
        self.lOADDED_BARRIERE =ImageTk.PhotoImage(self.LOAD_BARRIERE)
        self.Terrain = self.ZoneDeJeu.create_image(0,0,anchor=NW,image= self.LOADDED_TERRAIN)

    def create_parti(self):
        # fonctions qui permet de creer l'objet de la classe partie lorsque le bouton joue est enclenche
        # entree : Aucune
        # sortie : Aucune
        self.partie = p.Partie(self, self.DIFFICULTEE, self.DY, self.VITESSE,self.LARGEUR,self.HAUTEUR, self.CANVAS_WIDTH, self.CANVAS_HEIGHT,self.controle_up, self.controle_down, self.controle_left, self.controle_right,self.controle_shot)
        self.partie.lancementPartie()
    
    def controle(self):
        # fonction qui creer la fenetre de controle de touche de son contenu ainsi que son contenu
        # entree : Aucune
        # sortie : Aucune
        fenetre_parametre_controle = Toplevel(self.mw)

        placement_x = int(self.LARGEUR/3)
        placement_y = int(self.HAUTEUR/3)

        fenetre_parametre_controle.title('Fenetre Parametre')
        fenetre_parametre_controle['bg']='grey'
        fenetre_parametre_controle.geometry(f'400x400+{placement_x}+{placement_y}')

        #label de difficultee
        label_controle = Label(fenetre_parametre_controle, text = "Changement des contrôles", bg='grey', fg='white')
        label_controle.pack(pady=20)
        label_right = Label(fenetre_parametre_controle, text = "Droite", bg='grey', fg='white')
        label_right.pack(pady=10)
        entry_controle_right = Entry(fenetre_parametre_controle, bg='white',fg='black')
        entry_controle_right.pack()
        label_left = Label(fenetre_parametre_controle, text = "Gauche", bg='grey', fg='white')
        label_left.pack(pady=10)
        entry_controle_left = Entry(fenetre_parametre_controle, bg='white',fg='black')
        entry_controle_left.pack()
        label_up = Label(fenetre_parametre_controle, text = "Haut", bg='grey', fg='white')
        label_up.pack(pady=10)
        entry_controle_up = Entry(fenetre_parametre_controle, bg='white',fg='black')
        entry_controle_up.pack()
        label_down = Label(fenetre_parametre_controle, text = "Bas", bg='grey', fg='white')
        label_down.pack(pady=10)
        entry_controle_down = Entry(fenetre_parametre_controle, bg='white',fg='black')
        entry_controle_down.pack()
        label_shot = Label(fenetre_parametre_controle, text = "Tire", bg='grey', fg='white')
        label_shot.pack(pady=10)
        entry_controle_shot = Entry(fenetre_parametre_controle, bg='white',fg='black')
        entry_controle_shot.pack()

        button_valide_controle = Button(fenetre_parametre_controle, text='valider', pady=5,command = lambda: self.get_entry_controle(entry_controle_right,entry_controle_left,entry_controle_up,entry_controle_down,entry_controle_shot))
        button_valide_controle.pack()


    def difficultee(self):
        pass

    def quitter(self):
        pass

    def quitter_logiciel(self):
        # creation du bouton quitter
        # entree : Aucune
        # sortie : Aucune
        self.mw.destroy()

    def a_propos(self):
        # creation du a propos
        # entree : Aucune
        # sortie : Aucune
        mon_message = messagebox.showinfo("À Propos", 'Ce Space Invader a été réaliser pour le "TP4" du module "Développement logiciel en Python (S5)" du cursus 3ETI par \n Mathieu ZEMAN et Gaëlle LEROUX')


    def fenetre_parametre(self):
        # creation des parametres de difficulte et vitesse que
        # entree : Aucune
        # sortie : Aucune
        fenetre_parametre = Toplevel(self.mw)

        placement_x = int(self.LARGEUR/3)
        placement_y = int(self.HAUTEUR/3)

        fenetre_parametre.title('Fenetre Parametre')
        fenetre_parametre['bg']='grey'
        fenetre_parametre.geometry(f'300x300+{placement_x}+{placement_y}')

        #label de difficultee
        label_difficultee = Label(fenetre_parametre, text = "Difficulté", bg='grey', fg='white')
        label_difficultee.pack(pady=15)
        #Input utilisateur des Distributeur
        entry_difficultee = Entry(fenetre_parametre, bg='white',fg='black')
        entry_difficultee.pack()
        # Création du bouton de validation du nom du distributeur 
        button_valide_difficultee = Button(fenetre_parametre, text='valider', pady=5,command = lambda: self.getEntryDiff(entry_difficultee))
        button_valide_difficultee.pack()



        #label de difficultee
        label_vitesse = Label(fenetre_parametre, text = "Vitesse", bg='grey', fg='white')
        label_vitesse.pack(pady=15)
        #Input utilisateur des Distributeur
        entry_vitesse = Entry(fenetre_parametre, bg='white',fg='black')
        entry_vitesse.pack()
        # Création du bouton de validation du nom du distributeur 
        button_valide_vitesse = Button(fenetre_parametre, text='valider', pady=5,command = lambda: self.get_entry_vit(entry_vitesse))
        button_valide_vitesse.pack()

    def getEntryDiff(self,entry_difficultee):
         #Récupération des donnees de difficultee entree par l'utilisateur
         # entree : Aucune
        # sortie : Aucune
        
        res = entry_difficultee.get()
        if res.isdigit():
            res = int(res)
            self.DIFFICULTEE = res
        else:
            fenetre_parametre = Toplevel(self.mw)

            placement_x = int(self.LARGEUR/3.5)
            placement_y = int(self.HAUTEUR/2.5)

            fenetre_parametre.title('Erreur')
            fenetre_parametre['bg']='grey'
            fenetre_parametre.geometry(f'500x50+{placement_x}+{placement_y}')

            #label de difficultee
            label_difficultee = Label(fenetre_parametre, text = "Mauvais interaction, vérifier que vous avez bien rentrer un nombre essentiellement", bg='grey', fg='white')
            label_difficultee.pack(pady=15)
            
        entry_difficultee.delete(0,'end')
        entry_difficultee.configure(text="")

    def get_entry_vit(self,entry_vitesse): 
        #Récupération des donnes de vitesse entree par l'utilisateur
        # entree : Aucune
        # sortie : Aucune
        res = entry_vitesse.get()
        if res.isdigit():
            res = int(res)
            self.VITESSE = res
        else:
            fenetre_parametre = Toplevel(self.mw)

            placement_x = int(self.LARGEUR/3.5)
            placement_y = int(self.HAUTEUR/2)

            fenetre_parametre.title('Erreur')
            fenetre_parametre['bg']='grey'
            fenetre_parametre.geometry(f'500x50+{placement_x}+{placement_y}')

            #label de difficultee
            label_difficultee = Label(fenetre_parametre, text = "Mauvais interaction, vérifier que vous avez bien rentrer un nombre essentiellement", bg='grey', fg='white')
            label_difficultee.pack(pady=15)
            
        entry_vitesse.delete(0,'end')
        entry_vitesse.configure(text="")

    def get_entry_controle(self,entry_controle_right,entry_controle_left,entry_controle_up,entry_controle_down,entry_controle_shot):    
        #Récupération des nouvelles touche de controle du personnage entree par l'utilisateur
        # entree : Aucune
        # sortie : Aucune
        res1 = entry_controle_right.get()
        res2 = entry_controle_left.get()
        res3 = entry_controle_up.get()
        res4 = entry_controle_down.get()
        res5 = entry_controle_shot.get()

        if res1.isalpha() != False or res2.isalpha() != False or res3.isalpha() != False or res4.isalpha() != False or res5.isalpha() != False:

            self.controle_right=res1
            self.controle_left=res2
            self.controle_up=res3
            self.controle_down=res4
            self.controle_shot=res5
        else:
            fenetre_parametre = Toplevel(self.mw)

            placement_x = int(self.LARGEUR/3.5)
            placement_y = int(self.HAUTEUR/2)

            fenetre_parametre.title('Erreur')
            fenetre_parametre['bg']='grey'
            fenetre_parametre.geometry(f'500x50+{placement_x}+{placement_y}')

            #label de difficultee
            label_difficultee = Label(fenetre_parametre, text = "Mauvais interaction, vérifier que vous avez bien inscrit le nom de la touche", bg='grey', fg='white')
            label_difficultee.pack(pady=15)
            
        entry_controle_right.delete(0,'end')
        entry_controle_right.configure(text="")
            
        entry_controle_left.delete(0,'end')
        entry_controle_left.configure(text="")
            
        entry_controle_up.delete(0,'end')
        entry_controle_up.configure(text="")
            
        entry_controle_down.delete(0,'end')
        entry_controle_down.configure(text="")
            
        entry_controle_shot.delete(0,'end')
        entry_controle_shot.configure(text="")
        







    def demarrer_partie(self):
        # fonction qui demarre la partie 
        # entree : Aucune
        # sortie : Aucune
        self.mw.mainloop()

