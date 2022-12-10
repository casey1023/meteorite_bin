import pygame
import constant
from time import time
from ball import *

class basic_planet():
    def __init__(self,screen, position,life=1, radius=20, shootinterval=3):
        self.position = Vector2(position)
        self.life=life
        self.radius = radius
        self.screen=screen
        self.t=time()
        self.shootinterval=shootinterval
    def draw(self):
        pygame.draw.circle(self.screen,constant.BLUE,self.position,self.radius,0)
    def addball(self,mp):
        if time()-self.t>=self.shootinterval:
        	self.t=time()
        	return ball(self.screen,self.position+(mp-self.position).normalize()*self.radius*1.5,(mp-self.position)*0.03)
        else:
        	return 0
