#from gaelle import TailleVaisseau


class Vaisseau:
    def __init__(self,POSX,POSY,TailleVaisseau):
        self.POSX=POSX
        self.POSY=POSY
        self.TailleVaisseau=TailleVaisseau

    def deplacer(self,u,Hauteur,Largeur):
        if u=='z' and self.POSY-self.TailleVaisseau!=0:
            return(0,-20)
        if u=='s' and self.POSY+self.TailleVaisseau!=Hauteur:
            return(0,20)
        if u=='q' and self.POSX-self.TailleVaisseau!=0:
            return(-20,0)
        if u=='d' and self.POSX+self.TailleVaisseau!=Largeur:
            return(20,0)
    
