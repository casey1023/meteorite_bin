import pygame
import constant
from time import time

class basic_planet():
    def __init__(self,screen, position,life=1, radius=30, shootinterval=3):
        self.position = position
        self.life=life
        self.radius = radius
        self.screen=screen
        self.t=time()
        self.shootinterval=shootinterval

    def draw(self):
        pygame.draw.circle(self.screen,constant.BLUE,self.position,self.radius,0)
    