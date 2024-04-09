"""                """
# DevZeros School
"""                """
from ursina import *
import random
from ursina.prefabs.hot_reloader import *

app = Ursina()
nums = [load_texture(f"{i}.png") for i in range(10)]


class Flappy(Entity):
    def __init__(self):
        super().__init__(
            model="cube",
            scale=(0.5, 0.4, 0.001),
            texture=load_texture("ucmayan.png"),
            collider="box",
            z=-1,
        )

    def update(self):
        self.y -= 2 * time.dt
        if held_keys["space"]:
            self.texture = load_texture("suzulme.png")

        else:
            self.texture = load_texture("ucmayan.png")
        if self.y <= -2.6:
            self.y = 1

    def input(self, key):
        if key == "space":
            self.y += 0.7
            a = Audio("wing.ogg", volume=2)


class daban(Entity):
    def __init__(self):
        super().__init__(
            model="cube", scale=(25, 8.5, -1), texture=load_texture("sfondo2")
        )

    def update(self):
        self.x -= 0.5 * time.dt
        if self.x <= -2.5:
            self.x = 5.18


class zemin(Entity):
    def __init__(self):
        super().__init__(
            model="cube",
            y=-3.5,
            scale=(26, 1.6, 0.001),
            texture=load_texture("base"),
            z=-2,
        )

    def update(self):
        self.x -= 2.5 * time.dt
        if self.x <= -5:
            self.x = 5.8


cens = 0
dens = 0
zedd = -1


class tup(Entity):
    def __init__(self, rotation=(0, 0, 0), x=7, y=-2):
        super().__init__(
            model="cube",
            y=y,
            x=x,
            scale=(0.8, 5.1, 0.001),
            texture=load_texture("tubo"),
            collider="box",
            rotation=rotation,
            z=-1,
        )

    def update(self):
        self.x -= 2 * time.dt
        global cens
        global zedd
        global dens
        if self.x <= kus.x + 0.007:
            if self.x >= kus.x - 0.001:
                cens += 1

                if cens == 2:
                    cens = 1
                    dens += 1
                    zedd -= 0.001
                    cedds = puan(nums[dens], z=zedd)
                    if dens >= 9:
                        dens = 0


class puan(Entity):
    def __init__(self, texture=nums[0], x=0.2, z=-0.1):
        super().__init__(
            model="cube", texture=texture, scale=(0.4, 0.5, 0.01), z=z, x=x, y=3
        )


zze = zemin()


def mekanizmaa():
    c = 0

    ze = 0
    for i in range(90):
        c += 3.5
        ddd = random.uniform(-4.5, -1.5)
        t = tup(x=7 + c, y=ddd)
        de = t.y + 6.7
        d = tup(rotation=(0, 0, 180), y=de, x=t.x)


kus = Flappy()
daban()


def update():
    kushit = kus.intersects()
    if kushit.hit:
        a = Audio("hit.wav", volume=2)
        kus.rotation = (0, 0, 180)
        application.pause()
        gameover = Entity(
            model="cube",
            texture=load_texture("gameover.png"),
            z=-3,
            scale=(6.5, 1.8),
            x=0.01,
            y=0,
        )


mekanizmaa()


def input(key):
    if held_keys["q"]:
        application.quit()

    if key == "r":
        window.fullscreen = False


app.run()
