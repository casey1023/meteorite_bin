import pygame
import constant
from time import time
from ball import *
from math import sin,cos,radians

def pie(scr,color,center,radius,start_angle,stop_angle):
    theta=start_angle
    while theta <= stop_angle:
        pygame.draw.line(scr,color,center, 
        (center[0]+radius*cos(radians(theta)),center[1]+radius*sin(radians(theta))),2)
        theta+=0.5

class basic_planet():
    def __init__(self,screen, position,offset=0,life=2, radius=20, shootinterval=4):
        self.position = Vector2(position)
        self.life=life
        self.radius = radius
        self.screen=screen
        self.t=time()
        self.shootinterval=shootinterval
        self.offset=offset
    def draw(self):
        pie(self.screen,INVBLUE,self.position,self.radius+3,0,360*(time()-self.t)/(self.shootinterval+self.offset))
        pygame.draw.circle(self.screen,constant.BLUE,self.position,self.radius,0)
        font = pygame.font.SysFont(font__, 20)
        text = font.render(str(self.life), 1, WHITE)
        text_rect = text.get_rect(center=self.position)
        self.screen.blit(text, text_rect)
    def addball(self,mp):
        if time()-self.t>=self.shootinterval+self.offset:
        	self.t=time()
        	self.offset=0
        	return ball(self.screen,self.position+(mp-self.position).normalize()*self.radius*1.5,(mp-self.position).normalize()*10)
        else:
        	return 0
