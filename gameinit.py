import pygame


from button import *
from play import * 
from setting import *

constant=readconstant()
locals().update(constant)


def gameinit():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    icon = pygame.image.load('res/icon.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Meteorite Bin')
    return screen