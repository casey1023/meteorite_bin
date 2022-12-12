import pygame
from constant import *

class slider():
    def __init__(self,low_limit,high_limit,y,radius = 15, initial = 0,
     norm_color= WHITE, on_color= GREEN,linecolor = BLACK):
        self.low_limit = low_limit
        self.high_limit = high_limit
        self.y = y
        self.r = radius
        self.initial = low_limit + (high_limit - low_limit)*initial
        self.activate = False
        self.norm_color = norm_color
        self.on_color = on_color
        self.position = (self.initial,self.y)
        self.line_color = linecolor

    def draw(self,screen,mouse_pos,pres):
        over = self.Over(mouse_pos)
        if pres and over:
            self.activate = True
        if not pres:
            self.activate = False
        pygame.draw.line(screen, self.line_color,(self.low_limit,self.y),(self.high_limit,self.y),width = 5)
        if self.activate:
            self.newpos(mouse_pos[0])
            pygame.draw.circle(screen,self.on_color, self.position, self.r, 0)
        else:
            pygame.draw.circle(screen,self.norm_color, self.position, self.r, 0)

    def Over(self, m_pos):
        if((self.position[0]-m_pos[0])**2+(self.position[1]-m_pos[1])**2) < self.r**2:
            return True
        return False

    # def clicked(self,activate,m_pos):
    #     if self.press and self.Over(m_pos):
    #         return True
    #     elif not self.press:
    #         return False
    #     else:
    #         return activate

    def newpos(self,mouse_x):
        if self.low_limit < mouse_x < self.high_limit:
            self.position =  (mouse_x,self.y)
        elif(self.low_limit >= mouse_x):
            self.position = (self.low_limit , self.y)
        elif(mouse_x >= self.high_limit):
            self.position = (self.high_limit, self.y)
