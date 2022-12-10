import pygame
import constant
from pygame.math import Vector2
from time import time

class ball():
    def __init__(self,screen, position,init_v=0, radius=5):
        self.position = position
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
    def move(self,pos):
        mp=Vector2(pos)
        p=Vector2(self.position)
        d=1/ (mp-p).length()**2 * (mp-p).normalize()*1000
        self.v+=d
        self.position += self.v
        if self.position.x<0 or self.position.x>constant.SCREEN_WIDTH:
            self.v.x=-self.v.x
        if self.position.y<0 or self.position.y>constant.SCREEN_HEIGHT:
            self.v.y=-self.v.y
        pygame.draw.circle(self.screen,constant.RED,self.position,self.radius,0)
    def iscolide(self,pos2,r2):
        return Vector2(pos2-self.position).length()<=r2+self.radius
    def isinvincible(self):
        if self.invincible and time()-self.t>1:
            self.invincible=False
        return self.invincible
