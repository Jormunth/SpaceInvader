
class Vaisseau:
    def __init__(self,POSX,POSY,TailleVaisseau):
        self.POSX=POSX
        self.POSY=POSY
        self.TailleVaisseau=TailleVaisseau

    def deplacer(self,u,v):
        self.POSX=self.POSX+u
        self.POSY=self.POSY+v
    
