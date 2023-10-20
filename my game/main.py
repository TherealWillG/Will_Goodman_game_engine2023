# content from kids can code: http://kidscancode.org/blog/
# this file was created by Will Goodman on 10/16
# import libraries and modules
from typing import Any
import pygame as pg
from pygame.sprite import Sprite
import random
import os
from settings import *
from random import randint
from sprites import * 

vec = pg.math.Vector2

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')

# game settings 






class Game:
    def __init__(self):
# init pygame and create a window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Game...")
        self.clock = pg.time.Clock()
        self.running = True
    def new(self):
        # create a group for all sprites
        self.all_sprites = pg.sprite.Group()
        self.all_platforms = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()
        # instantiate classes
        self.player = Player(self)


        # add instances to groups
        self.all_sprites.add(self.player)

        for p in PLATFORM_LIST:
            # instantiation of the platform class
            plat = Platform(*p)
            self.all_sprites.add(plat)
            self.all_platforms.add(plat)

        for m in range(0,25):
            m = Mob(randint(0, WIDTH), randint(0, HEIGHT/2), 20, 20, "normal")
            self.all_sprites.add(m)
            self.all_mobs.add(m)
        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update
            self.draw
    def update(self):
        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
        if hits:
            
            self.player.pos.y = hits[0].rect.top
            self.player.vel.y = 0
    def events(self):
        for event in pg.event.get():
        # check for closed window
            if event.type == pg.QUIT:
                self.running = False
    def draw(self):
        self.screen.fill(BLACK)
        pg.display.flip()
    # draw all sprites
        self.all_sprites.draw(self.screen)
        self.draw_text("Score: " + str(SCORE), 22, WHITE, WIDTH/2, HEIGHT/10)
    def draw_text(self, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(self, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
        
    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass

# Game loop

                
    # this prevents the player from jumping up through a platform
    # if player.vel.y < 0:
    #     hits = pg.sprite.spritecollide(player, all_platforms, False)
    #     if hits:
    #         print("ouch")
    #         SCORE -= 1
    #         if player.rect.bottom >= hits[0].rect.top - 5:
    #             player.rect.top = hits[0].rect.bottom
    #             player.acc.y = 5
    #             player.vel.y = 0

    ############ Draw ################
    # draw the background screen

pg.quit()
