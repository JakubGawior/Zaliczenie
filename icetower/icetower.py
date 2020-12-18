import pgzrun
import numpy as np

class Flat(Actor):
    def react(self):
        if np.abs(ice.center[1]+ice.size[1]/2-self.center[1]+self.size[1]/2) < 15:
            ice.vy = 0
            ice.bottom = self.top
        elif np.abs(ice.center[1]-ice.size[1]/2-self.center[1]-self.size[1]/2) < 15:
            ice.vy = 0
            ice.top = self.bottom
        elif np.abs(ice.center[0]+ice.size[0]/2-self.center[0]+self.size[0]/2) < 15:
            moveall(6)
        elif np.abs(ice.center[0]-ice.size[0]/2-self.center[0]-self.size[0]/2) < 15:
            moveall(-6)

    def move(self):
        pass

class Coin(Actor):
    def react(self):
        if ice.colliderect(self):
            objs.remove(self)
            ice.points = ice.points+1

    def move(self):
        pass

def amimate(self, pos):
    pass


class Flaga(Actor):
    def react(self):
        if ice.colliderect(self):
            ice.win = True

    def move(self):
        pass

def newgame():
    ice.pos = (330, HEIGHT-150)
    ice.vy = 10
    ice.time = 0
    ice.dir = "right"
    ice.dead = False
    ice.points = 0
    ice.win = False

    for i in range(len(objs)):
        objs.remove(objs[0])
    file = open("map.dat")
    i = 0

    for line in file:
        for j in range(len(line)):
            if line[j] == 'F':
                objs.append(Flat('flat.png', (j * 33, 33 * i)))
            elif line[j] == 'D':
                objs.append(Flat('platformdirt.png', (j * 33, 33 * i)))
            elif line[j] == 'I':
                objs.append(Flat('platformicy.png', (j * 33, 33 * i)))
            elif line[j] == 'B':
                objs.append(Flat('platformbrick.png', (j * 33, 33 * i)))
            elif line[j] == 'o':
                objs.append(Coin('coin.png', (j * 33, 33 * i)))
            elif line[j] == 'f':
                objs.append(Flaga('flaga.png', (j * 33, 33 * i)))
        i = i + 1
        #music.play('song.mp3')


def draw():
    screen.fill((100, 100, 100))
    for obj in objs:
        obj.draw()
    ice.draw()
    screen.draw.text(str(ice.points), color="black", midtop=(WIDTH/8*0.5, 10), fontsize=50, shadow=(0, 1))
    if ice.win:
        screen.draw.text("!!! YOU WIN !!!", color="yellow", midtop=(WIDTH/2, 2), fontsize=170, shadow=(0, 0))

def moveall(x):
    if x == 0:
        if 0 <= ice.x:
            ice.x = ice.x - x
        elif ice.x < 0:
            ice.x < 0
    else:
        if 0 <= ice.x < WIDTH / 2:
            ice.x = ice.x - x
        elif ice.x > WIDTH / 2:
            ice.x = WIDTH / 2
        elif ice.x >= WIDTH / 2:
            for obj in objs:
                obj.x = obj.x + x

def move(dt):
    if ice.dir == "right":
        ice.image = "ice.png"
    else:
        ice.image = "ice2.png"

    uy = ice.vy
    ice.vy = ice.vy+2000.0*dt
    ice.y = ice.y+(uy+ice.vy)*0.5*dt

    if keyboard.right:
        if ice:
            moveall(-2)
        ice.dir = "right"
        if ice.time < 8:
            ice.image = "ice2.png"
        else:
            ice.image = "ice.png"

    if keyboard.left:
        if ice:
            moveall(2)
        ice.dir = "left"
        if ice.time < 8:
            ice.image = "ice2.png"
        else:
            ice.image = "ice.png"

    for obj in objs:
        if ice.colliderect(obj):
            obj.react()
    if ice.vy != 0 and ice.dir == "right":
        ice.image = "ice.png"
    elif ice.vy != 0 and ice.dir == "left":
        ice.image = "ice2.png"
    if ice.bottom > HEIGHT:
        ice.dead = True

def update(dt):
    if not ice.win:
        move(dt)
        for obj in objs:
            obj.move()
            if obj.image == "flaga.png":
                if np.abs(obj.center[0]-ice.center[0]) < 1:
                    ice.win = True
    if ice.dead:
        newgame()

def on_key_down(key):
    if key == keys.SPACE and ice.vy == 0:
        ice.vy = -800

HEIGHT = 990
WIDTH = 660
TITLE = "IcyTower"

ice = Actor("ice.png", (330, HEIGHT-100))
ice.vy = 0
ice.time = 0
ice.dir = "right"
ice.dead = False
ice.points = 0
ice.win = False
objs = []
newgame()

pgzrun.go()

