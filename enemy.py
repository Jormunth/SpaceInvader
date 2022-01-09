class Enemy:
    def __init__(self, tag,vitesse,posX, posY,DY):
        self.tag=tag
        self.posX=posX
        self.posY=posY
        self.vitesse=vitesse
        self.DY=DY


    def getTag(self):
        return self.tag

    def getPosX(self):
        self.posX
        return self.posX

    def getPosY(self):
        return self.posY

    def getVitesse(self):
        return self.vitesse

    def getDY(self):
        return self.DY

    def deplacer(self, NewposX, NewposY):
        self.posX = NewposX
        self.posY = NewposY
        """ print("Position actuelle", self.posX, " ", self.posY,) """
    
    def tirer(self):
        print("Je tire")

""" 
my_enemy = Enemy(100, 100, 200, None)
my_enemy.deplacer(200, 300)
my_enemy.deplacer(150, 125)
my_enemy.tirer()
 """