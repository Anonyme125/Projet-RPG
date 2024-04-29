import pyxel

class personnage:
    def __init__(self) -> None:
        self.x = 60
        self.y = 60
        self.vitesse = 2
        self.direction = 0
        
    def update(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            if self.x < 120:
                self.x += self.vitesse
        if pyxel.btn(pyxel.KEY_LEFT):
            if self.x > 0:
                self.x -= self.vitesse
        if pyxel.btn(pyxel.KEY_DOWN):
            if self.y < 120:
                self.y += self.vitesse
        if pyxel.btn(pyxel.KEY_UP):
            if self.y > 0:
                self.y -= self.vitesse
    
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 8, 8)
        
        
class App:
    def __init__(self):
        pyxel.init(128, 128, title="Déplacement Personnage", fps=30)
        pyxel.load("test.pyxres")
        self.personnage = personnage()
        pyxel.run(self.update, self.draw)
    
    def update(self):
        self.personnage.update()
    
    def draw(self):
        pyxel.cls(0)
        self.personnage.draw()

App()