from Fenetre import *

Canevas=canevas(480,320)
vaisseau=Vaisseau(480%2,320%2,20)

Canevas.creer_fenetre()
Canevas.creer_vaisseau(vaisseau.TailleVaisseau,vaisseau.POSX,vaisseau.POSY)