import pyxel
from time import *
from random import *

""" NOTES POUR L'EDITEUR PYXEL
    
    SON :   - SFX
                N = Note normale (note tenue lorsqu'elle est répétée)
                F = Note qui n'est pas tenue lorsqu'elle est répétée  
                V = Tremblement de la note (comme un doigt qui tremble sur une corde de violon)
                S = Transition fuildes entre des notes d'hauteur différente
"""

pyxel.init(128,128, title="déplacement", fps = 30)
pyxel.load("sprite.pyxres")

vaisseau_x = 60
vaisseau_y = 60
dash_timer = 0
type_dash = ""
Nombre_tables = randint(5,15)
coordonees_possibles = [x for x in range (0,129) if x%4 == 0]
coordonees_tables =[]
for _ in range (Nombre_tables*2):
    coordonees_tables.append(coordonees_possibles[randint(0,32)])
    



def dash(dash_timer, y, x, type_dash):
    if dash_timer > 25:
        if "bas" in type_dash:
            if y<= 118:
                y += 5

        if "haut" in type_dash:
            if y >= 5:
                y -= 5

        if "droite" in type_dash:
            if x <= 118:
                x += 5

        if "gauche" in type_dash:
            if x>= 5:
                x -= 5

    if dash_timer > 0:
        dash_timer -= 1
    
    if dash_timer == 0:
        type_dash = ""

    return(dash_timer, y, x, type_dash)





def déplacement(x, y, dash_timer, type_dash):

    if pyxel.btn(pyxel.KEY_RIGHT):      # Déplacement de base avec les flèches
        if x < 120:
            x += 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if x > 0:
            x -= 1
    if pyxel.btn(pyxel.KEY_DOWN):
        if y < 120:
            y += 1
    if pyxel.btn(pyxel.KEY_UP):
        if y > 0:
            y -= 1

    if pyxel.btn(pyxel.KEY_E) and pyxel.btn(pyxel.KEY_DOWN) and dash_timer == 0:        # Déplacement avec ésquive vers le bas, le haut, la droite ou la gauche
        dash_timer = 30
        type_dash += "bas"

    if pyxel.btn(pyxel.KEY_E) and pyxel.btn(pyxel.KEY_UP) and dash_timer == 0:
        dash_timer = 30
        type_dash += "haut"

    if pyxel.btn(pyxel.KEY_E) and pyxel.btn(pyxel.KEY_RIGHT) and dash_timer == 0:
        dash_timer = 30
        type_dash += "droite"

    if pyxel.btn(pyxel.KEY_E) and pyxel.btn(pyxel.KEY_LEFT) and dash_timer == 0:
        dash_timer = 30
        type_dash += "gauche"

    return x, y, dash_timer, type_dash

def update():
    global vaisseau_x, vaisseau_y, dash_timer, type_dash
    vaisseau_x, vaisseau_y, dash_timer, type_dash = déplacement(vaisseau_x, vaisseau_y, dash_timer, type_dash)        # Met à jours à chaque tique les variables x, y, dash_timer
    dash_timer, vaisseau_y, vaisseau_x, type_dash = dash(dash_timer, vaisseau_y, vaisseau_x, type_dash)

def draw():
    pyxel.cls(0)
    for i in range(0,128,8):
        for j in range(0,128,8):
            pyxel.blt(i,j,0,8,0,8,8)       # Dessine après que les variables se soient mises à jours
    for i in range (Nombre_tables):
        pyxel.blt(coordonees_tables[i],coordonees_tables[i+1],0,0,0,8,8)
        pyxel.blt(coordonees_tables[i]+8,coordonees_tables[i+1],0,0,8,8,8)
        pyxel.blt(coordonees_tables[i]-8,coordonees_tables[i+1],0,8,8,8,8)
        pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, 1)
    


pyxel.run(update, draw)
