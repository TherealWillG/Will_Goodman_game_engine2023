# content from kids can code: http://kidscancode.org/blog/
# I recieved a lot of help from Mr. Cozort's example code found on canvas
# I also recieved a huge amount of help from all of my tablemates: Alan, Bradely, Faaris, Nolan, and Isaiah 

# import libraries and modules
'''
the main goal of my game is to attempt to create a simple game that is similar to a mix between pacman and mario
the main objevtive of the game is to collect coins whilst sprites chase you. you are too collect coins before
you are hit too many times. a

'''
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
from settings import *
from sprites import *
import math


vec = pg.math.Vector2

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

# This is the class in which the Game will reside
class Game:
    def __init__(self):
        # init pygame and create a window
        pg.init()
        pg.mixer.init()
        # set the width and height of the game window based on the settings 
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Game...")
        self.clock = pg.time.Clock()
        self.running = True
    # create function for self
    def new(self): 
        # create a group for all sprites
        self.hitpoints = 100
        self.score = 0
        # Meant to create coin collecting sound
        self.coin_sound = pg.mixer.Sound(os.path.join(snd_folder, 'coin.mp3'))
        # meant to create backgroudn image
        self.bgimage = pg.image.load(os.path.join(img_folder, "background.png")).convert()
        # Creates mob hits soudn efffect
        self.punch_sound = pg.mixer.Sound(os.path.join(snd_folder, "punch.mp3"))
        self.all_sprites = pg.sprite.Group()
        self.all_platforms = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()
        self.all_coins = pg.sprite.Group()
        self.level = 0
        # instantiate classes
        self.player = Player(self)
        # add instances to groups
        self.all_sprites.add(self.player)

        for p in PLATFORM_LIST:
            # instantiation of the Platform class
            plat = Platform(*p)
            self.all_sprites.add(plat)
            self.all_platforms.add(plat)
        # Spawn in mobs, 10 of them and determine which class of mob they are, since all mobs are seeking, 
        # i have written "normal"
        for m in range(0,9):
            m = Mob(self, randint(0, WIDTH), randint(0, math.floor(HEIGHT/2)), 20, 20, "normal")
            self.all_sprites.add(m)
            self.all_mobs.add(m)
        # Spawns in coins, these are collected for score.



        self.run()
# allows for game to run 
    def run(self):
        self.playing = True
        self.coin_spawn()
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
# updating the player class
    def update(self):
        self.all_sprites.update()
        if len(self.all_coins) == 0:
            self.coin_spawn()
        if self.player.pos.x < 0:
            self.player.vel
        # this is what prevents the player from falling through the platform when falling down...
        if self.player.vel.y != 0:
            hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
            if hits:
                if self.player.vel.y > 1:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    self.player.vel.x = hits[0].speed*1.5
            # This collects the coin that the player makes contact with, they disappear and then add to your score
            coinhits = pg.sprite.spritecollide(self.player, self.all_coins, True)
            if coinhits:
                print("you got a coin")
                self.score += 10
                self.coin_sound.play()
            # This sets the mob collisions
            mobhits = pg.sprite.spritecollide(self.player, self.all_mobs, False)
            if mobhits:
                # if mob collision occurs, you lose points as well as health,
                self.hitpoints -= 10
                self.score -= 2
                # The playing of this sound triggers for every single contact with a mob, it sounds a bit scuffed
                self.punch_sound.play()
                
        # This prevents the player from walking off of the map, it will teleport them to the other side.
        if self.player.pos.x < 0:
            self.player.pos.x = WIDTH
        if self.player.pos.x > WIDTH:
            self.player.pos.x = 0
        '''
        There is no code that prevents the player from jumping through the bottom of platforms, I decided that in 
        order to add some sort of gameplay variety and movement tech, that jumping through the bottom of platforms 
        would be fine, given that jumping through the bottom of the platform grants a speed boost, kinda like
        a double jump.
        '''
                        
    def coin_spawn(self):
        for c in range (0, 20):
            c = coin(randint(0, WIDTH), randint (0, math.floor(HEIGHT/2)), 20, 20, "normal")
            self.all_sprites.add(c)
            self.all_coins.add(c)
            
    def events(self):
        for event in pg.event.get():
        # check for closed window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        ############ Draw ################
        # draw the background screen
        self.screen.fill(BLACK)
        self.screen.blit(self.bgimage, (0,0))
        # pg.image.load(os.path.join(img_folder, 'background.png')).convert()
        # draw all sprites
        self.all_sprites.draw(self.screen)
        # Draw hitpoint counter
        self.draw_text("Hitpoints: " + str(self.player.hitpoints), 22, WHITE, WIDTH/2, HEIGHT/10)
        # Draw score counter
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH/2, HEIGHT/15)
        

        # buffer - after drawing everything, flip display
        pg.display.flip()
    # Sets the fonts, sizes, and positions of the written text in game
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass

g = Game()
while g.running:
    g.new()


pg.quit()
