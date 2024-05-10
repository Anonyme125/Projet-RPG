import pyxel

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size =20
        self.speed = 2
        self.dashing = False
        self.dash_distance = 30
        self.dash_frames = 15

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= self.speed
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.x += self.speed

        if pyxel.btn(pyxel.KEY_UP):
            self.y -= self.speed
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.y += self.speed

        if pyxel.btnp(pyxel.KEY_SPACE) and not self.dashing:
            self.dash()

        if self.dashing:
            self.dash_frames -= 1
            if self.dash_frames <= 0:
                self.dashing = False
                self.dash_frames = 5

    def dash(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= self.dash_distance
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.x += self.dash_distance
        elif pyxel.btn(pyxel.KEY_UP):
            self.y -= self.dash_distance
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.y += self.dash_distance
        self.dashing = True

    def draw(self):
        pyxel.rect(self.x, self.y, self.size, self.size, 9)

class Game:
    def __init__(self):
        self.player = Player(80, 60)

    def update(self):
        self.player.update()

    def draw(self):
        pyxel.cls(0)
        self.player.draw()

# Initialisation de l'application Pyxel
pyxel.init(160, 120)

# Création du jeu
game = Game()

# Définition des fonctions de rappel
pyxel.run(game.update, game.draw)
