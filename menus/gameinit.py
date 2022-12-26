import pygame

# from button import *
# from setting import *
from obj.setting import *

def gameinit():
    constant=readconstant()
    locals().update(constant)

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    icon = pygame.image.load('res/icon.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Meteorite Bin')
    return screen