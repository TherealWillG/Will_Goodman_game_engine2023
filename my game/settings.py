# this file was created by william goodman 10/18
# content from chris bradfield kidscancode.com, 
# this file will work with game settings

# player settings
PLAYER_JUMP = 40
PLAYER_GRAV = 1.5

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 360
HEIGHT = 480
FPS = 30
SCORE = 0

PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, "ice"),
                 (WIDTH/2 - 50, HEIGHT * 3/4, 100, 20, "normal"),
                 (125, HEIGHT - 350, 100, 20,"normal"),
                 (350, 200, 100, 20, "moving"),
                 (175, 100, 50, 20, "moving")]
