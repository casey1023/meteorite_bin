import pygame
from ..obj.constant import *
from pygame.math import Vector2
from time import time

class ball():
    def __init__(self,screen, position,init_v=0, radius=5):
        self.position = Vector2(position)
        self.radius = radius
        if init_v:
            self.v=Vector2(init_v)
        else:
            self.v = Vector2(0,0)
        self.screen=screen
        self.t=time()
        self.invincible=True
    def __str__(self):
        return "Position : "+str(self.position)+"\nV : "+str(self.v)
    def move(self,mp):
        p=self.position
        # d=1/ (mp-p).length()**2 * (mp-p).normalize()*2000
        d=(mp-self.position)*0.002
        self.v+=d
        #set speed limit
        speedlimit=12
        if self.v.length()>speedlimit:
            self.v=self.v.normalize()*speedlimit
        self.position += self.v
        #check if hit boarder
        if self.position.x<0 or self.position.x>SCREEN_WIDTH:
            self.v.x=-self.v.x
        if self.position.y<0 or self.position.y>SCREEN_HEIGHT:
            self.v.y=-self.v.y
        if self.invincible:
            pygame.draw.circle(self.screen,INVRED,self.position,self.radius,0)
        else:
            pygame.draw.circle(self.screen,RED,self.position,self.radius,0)
    def iscolide(self,pos2,r2):
        return Vector2(pos2-self.position).length()<=r2+self.radius
    def isinvincible(self):
        if self.invincible and time()-self.t>1.5:
            # print("set to not invincible")
            self.invincible=False
        return self.invincible
