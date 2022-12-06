import pygame


from button import *
from play import * 
from constant import *


def gameinit():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Meteorite Bin')
    return screen