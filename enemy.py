class Enemy:
    def __init__(self, tag, posX, posY,DY):
        self.tag=tag
        self.posX=posX
        self.posY=posY
        self.DY=DY
        #self.Enemy=ZoneDeJeu.create_oval(X-Rayon, Y-Rayon, X+Rayon, Y+Rayon, fill="red", outline="black", width=5)


    #def deplacer(self,posX,posY,DX,DY,Rayon,Largeur,Hauteur):
    def deplacer(self, posX, posY):
        self.posX = posX
        self.posY = posY
        print("Position actuelle", self.posX, " ", self.posY,)
    
    def tirer(self):
        print("Je tire")


my_enemy = Enemy(100, 100, 200, None)
my_enemy.deplacer(200, 300)
my_enemy.deplacer(150, 125)
my_enemy.tirer()
