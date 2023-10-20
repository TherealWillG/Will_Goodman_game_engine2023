# This file was created by Will Goodman on 10/20
import pygame as pg
from pygame.sprite import Sprite
from pygame.math import Vector2 as vec
import os
from settings import *
import random


game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')


class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(GREEN)
        # use an image for player sprite...
        self.game = game
        self.image = pg.image.load(os.path.join(img_folder, 'character.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        print(self.rect.center)
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
        if keys[pg.K_SPACE]:
            self.jump()
    def jump(self):
        hits = pg.sprite.spritecollide(self, self.all_platforms, False)
        if hits:
            print("i can jump")
            self.vel.y = -PLAYER_JUMP
    def update(self):
        # self.rect.x += 5
        # self.rect.y += 5
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        # hits = pg.sprite.spritecollide(self, all_platforms, False)
        # if hits:
        #     print("i've collided...") 
        # if friction - apply here
        self.acc.x += self.vel.x * -0.5
        self.acc.y += self.vel.y * -0.2
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.rect.x > WIDTH:
            self.rect.x = 0
        if self.rect.y > HEIGHT:
            self.rect.y = 0
        self.rect.midbottom = self.pos

# platforms

class Platform(Sprite):
    def __init__(self, x, y, w, h, kind):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kind = kind
    def update(self):
        if self.kind == "moving":
            self.pos = self.rect.x
            self.rect.x = self.pos + 2
        if self.kind == "ice":
            self.image.fill(BLUE)

class Mob(Sprite):
    def __init__(self, x, y, w, h, kind):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kind = kind
    def seeking(self):
        if self.player.rect.x > self.rect.x:
            self.rect.x += 1
        elif self.player.rect.x < self.rect.x:
            self.rect.x -=1
        elif self.player.rect.y > self.rect.y:
            self.rect.y +=1
        elif self.player.rect.y > self.rect.y:
            self.rect.y -=1
    def seeking2(self):
        if self.player.rect.x > self.rect.x:
            self.rect.x += 1
        elif self.player.rect.x < self.rect.x:
            self.rect.x -=1
        elif self.player.rect.y > self.rect.y:
            self.rect.y +=1
        elif self.player.rect.y > self.rect.y:
            self.rect.y -=1
    def update(self):
        self.seeking()