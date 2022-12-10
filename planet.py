import pygame
import constant
from time import time
from ball import *

class basic_planet():
    def __init__(self,screen, position,offset=0,life=1, radius=20, shootinterval=4):
        self.position = Vector2(position)
        self.life=life
        self.radius = radius
        self.screen=screen
        self.t=time()
        self.shootinterval=shootinterval
        self.offset=offset
    def draw(self):
        pygame.draw.circle(self.screen,constant.BLUE,self.position,self.radius,0)
        font = pygame.font.SysFont(font__, 20)
        text = font.render(str(self.life), 1, WHITE)
        text_rect = text.get_rect(center=self.position)
        self.screen.blit(text, text_rect)
    def addball(self,mp):
        if time()-self.t>=self.shootinterval+self.offset:
        	self.t=time()
        	self.offset=0
        	return ball(self.screen,self.position+(mp-self.position).normalize()*self.radius*1.5,(mp-self.position)*0.02)
        else:
        	return 0
