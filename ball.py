import pygame
import constant
from pygame.math import Vector2

class ball():
    def __init__(self, position,screen, radius=5):
        self.position = position
        self.radius = radius
        self.v = Vector2(0,0)
        self.screen=screen
    def __str__(self):
        for i in range(len(balls)):
            if self==balls[i]:
                return "id "+str(i)
    def move(self,pos):
        mp=Vector2(pygame.mouse.get_pos())
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