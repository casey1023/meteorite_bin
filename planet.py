import pygame
from time import time
from ball import *
from math import sin,cos,radians
from setting import *

#get const
constant = readconstant()
locals().update(constant)

def pie(scr, color, center, radius, start_angle, stop_angle):
    theta = start_angle
    while theta <= stop_angle:
        pygame.draw.line(scr, color, center, 
        (center[0] + radius * cos(radians(theta)), center[1] + radius * sin(radians(theta))), 2)
        theta += 1.5

class basic_planet():
    def __init__(self, screen, position, offset = 0, life = 2, radius = 20, shootinterval = 4):
        self.position = Vector2(position)
        self.life = life
        self.radius = radius
        self.screen = screen
        self.t = time()
        self.shootinterval = shootinterval
        self.beforeoffset = True
        self.offset = offset

    def draw(self):
        pie(self.screen, INVBLUE, self.position, self.radius + 3, 0,\
            360 * (time() - self.t) / (self.shootinterval + self.offset * self.beforeoffset))
        pygame.draw.circle(self.screen,BLUE, self.position, self.radius, 0)
        font = pygame.font.SysFont(font__, 20)
        text = font.render(str(self.life), 1, WHITE)
        text_rect = text.get_rect(center = self.position)
        self.screen.blit(text, text_rect)

    def addball(self, mp):
        if time() - self.t >= self.shootinterval + self.offset * self.beforeoffset:
            #print(time() - self.t , self.shootinterval , self.offset , self.beforeoffset)
            self.t = time()
            self.beforeoffset = False
            return [ball(self.screen, self.position + (mp - self.position).normalize() * self.radius * 1.3,\
                (mp - self.position).normalize() * 6)]
        else:
            return 0
    def reset_time(self):
        self.t = time()
        return None

class triple_shoot_planet():
    def __init__(self, screen, position, offset = 0,life = 1, radius = 20, shootinterval = 4):
        self.position = Vector2(position)
        self.life = life
        self.radius = radius
        self.screen = screen
        self.t = time()
        self.shootinterval = shootinterval
        self.beforeoffset = True
        self.offset = offset

    def draw(self):
        pie(self.screen, INVGREEN, self.position, self.radius + 3, 0,\
             360 * (time() - self.t) / (self.shootinterval + self.offset * self.beforeoffset))
        pygame.draw.circle(self.screen, GREEN, self.position, self.radius, 0)
        font = pygame.font.SysFont(font__, 20)
        text = font.render(str(self.life), 1, WHITE)
        text_rect = text.get_rect(center = self.position)
        self.screen.blit(text, text_rect)

    def addball(self, mp):
        if time() - self.t >= self.shootinterval + self.offset * self.beforeoffset:
            self.t = time()
            self.beforeoffset = False
            b1=ball(self.screen, self.position + (mp - self.position).normalize() * self.radius * 1.3, (mp - self.position).normalize()*6)
            b2=ball(self.screen, self.position + (mp - self.position).normalize().rotate(20) * self.radius * 1.3, (mp - self.position).normalize() * 6)
            b3=ball(self.screen, self.position + (mp - self.position).normalize().rotate(-20) * self.radius * 1.3, (mp - self.position).normalize() * 6)
            return [b1, b2, b3]
        else:
            return 0
    def reset_time(self):
        self.t = time()
        return None

class explode_planet():
    def __init__(self, screen, position, offset = 0, life = 1, radius = 20, shootinterval = 4):
        self.position = Vector2(position)
        self.life = life
        self.radius = radius
        self.screen = screen
        self.t = time()
        self.shootinterval = shootinterval
        self.beforeoffset = True
        self.offset = offset

    def draw(self):
        pie(self.screen, INVRED, self.position, self.radius + 3, 0, \
            360 * (time() - self.t) / (self.shootinterval + self.offset * self.beforeoffset))
        pygame.draw.circle(self.screen, RED, self.position, self.radius, 0)
        font = pygame.font.SysFont(font__, 20)
        text = font.render(str(self.life), 1, WHITE)
        text_rect = text.get_rect(center = self.position)
        self.screen.blit(text, text_rect)

    def addball(self, mp):
        if time() - self.t >= self.shootinterval + self.offset * self.beforeoffset:
            self.t = time()
            self.beforeoffset = False
            b1 = ball(self.screen, self.position + (mp - self.position).normalize() * self.radius * 1.3, (mp - self.position).normalize() * 6)
            return [b1]
        else:
            return 0
        
    def explode(self,mp):
        return [ball(self.screen, self.position + (mp - self.position).normalize().rotate(i * 72) * self.radius * 1.3, (mp - self.position).normalize() * 6) for i in range(5)]
    
    def reset_time(self):
        self.t = time()
        return None
