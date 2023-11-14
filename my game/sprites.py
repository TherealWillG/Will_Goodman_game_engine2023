# I do not remember the exact date this file was created on but it is for the game code project
# Sources: Kidscancode Chris Bradfield : http://kidscancode.org/blog/, Mr. Cozort, and my tablemates Faaris, Nolan, Bradely, Isaiah, and Alan
# This file was created By Will Goodman

# import the necessary assets
from typing import Any
import pygame as pg
from pygame.sprite import Sprite
from pygame.math import Vector2 as vec
import os
from settings import *


# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

# Create class for player 
class Player(Sprite):
    # initiate player class
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        # set image/character for player class
        self.image = pg.image.load(os.path.join(img_folder, 'character.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        # set the starting hitpoints and score
        self.hitpoints = 100
        self.score = 0
    def controls(self):
        # Set the controls, I chose to use WASD and Space
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
        if keys[pg.K_SPACE]:
            self.jump()
        if keys[pg.K_r]:
            self.pos.x += 5
    def jump(self):
        # The following code ensures that the platforms do not dissappear when hit by player
        hits = pg.sprite.spritecollide(self, self.game.all_platforms, False)
        if hits:
            print("i can jump")
            self.vel.y = -PLAYER_JUMP
        # This following code allows for coins to disappear when you hit them, as well as increase your score when hit
        coinhits = pg.sprite.spritecollide(self, self.game.all_coins, True)
        if coinhits:
            print("you got a coin")
            self.score += 10
        # The following code allows for mobs to damage you, as well as reduce your score when you hit them
        mobhits = pg.sprite.spritecollide(self, self.game.all_mobs, False)
        if mobhits:
            self.hitpoints -= 10
            self.score -= 2
            if self.hitpoints < 0:
                pg.quit()

        
        
            
            

    def update(self):
        # CHECKING FOR COLLISION WITH MOBS HERE>>>>>
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        # if friction - apply here
        self.acc.x += self.vel.x * -PLAYER_FRIC
        # self.acc.y += self.vel.y * -0.3
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
        # if self.pos > WIDTH:
        #     self.pos = vec(WIDTH)
    

# platforms

class Platform(Sprite):
    def __init__(self, x, y, w, h, category):
        Sprite.__init__(self)
        # Sets size and position of platforms
        self.image = pg.Surface((w, h))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.category = category
        self.speed = 0
        # Creates the moving platform type
        if self.category == "moving":
            self.speed = 5
    def update(self):
        # Update to control the speed and places the the platforms are going
        if self.category == "moving":
            self.rect.x += self.speed
            if self.rect.x + self.rect.w > WIDTH or self.rect.x < 0:
                self.speed = -self.speed

class Mob(Sprite):
    def __init__(self, game, x, y, w, h, kind):
        # sets the size and sets the file path for the mobs image, its a ghost image
        Sprite.__init__(self)
        self.image = pg.Surface((w, h,))
        self.image = pg.image.load(os.path.join(img_folder, "ghost.jpg")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kind = kind
        self.game = game
        self.pos = vec(WIDTH/2, HEIGHT/2)
    # by defining all mobs in this class as seeking mobs, they will chase after the player and inflict damage.
    def seeking(self):
        if self.rect.x < self.game.player.rect.x:
            self.rect.x += 2
        if self.rect.x > self.game.player.rect.x:               
            self.rect.x -= 2
        if self.rect.y < self.game.player.rect.y:
            self.rect.y += 2
        if self.rect.y > self.game.player.rect.y:
            self.rect.y -= 2
    def update(self):
        self.seeking()
    
# the following piece of code creates the class for a coin, the main obj of the game is to collect these
class coin(Sprite):
    def __init__(self, x, y, w, h, kind):
        # sources the image for the gold coin, and sets the size and speeds of the coins 
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image = pg.image.load(os.path.join(img_folder, "pixil-frame-0.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kind = kind
        self.speed = 0
        self.pos = vec(WIDTH/2, HEIGHT/2)
    def update(self):
        pass



