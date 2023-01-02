import pygame
from pygame.math import Vector2
from time import time
from setting import *

#get const
constant = readconstant()
locals().update(constant)

class ball():
    ball_FPS = constant['FPS']
    def __init__(self, screen, position, init_v = 0, radius = 5):
        self.position = Vector2(position)
        self.radius = radius
        if init_v:
            self.v = Vector2(init_v)
        else:
            self.v = Vector2(0, 0)
        self.screen = screen
        self.t = time()
        self.invincible = True

    def __str__(self):
        return "Position : " + str(self.position) + "\nV : " + str(self.v)
    
    def move(self, mp):
        p = self.position

        # gravity
        #d = 1 / (mp-p).length()**2 * (mp-p).normalize() * 1000 * (60/ball.ball_FPS)
        # original
        d = (mp - self.position) * 0.0015 * (60/ball.ball_FPS)
        self.v += d
        #  * (60/ball.ball_FPS)

        #set speed limit
        speedlimit = 12
        if self.v.length() > speedlimit:
            self.v = self.v.normalize() * speedlimit
        self.position += self.v * (60/ball.ball_FPS)

        #check if hit boarder
        if (self.position.x < 0 and self.v.x < 0) or (self.position.x > SCREEN_WIDTH and self.v.x > 0):
            self.v.x = -self.v.x
            self.v = self.v * 0.95

        if (self.position.y < 0 and self.v.y < 0) or (self.position.y > SCREEN_HEIGHT and self.v.y > 0):
            self.v.y = -self.v.y
            self.v = self.v * 0.95

        if self.invincible:
            pygame.draw.circle(self.screen, LIGHTRED, self.position, self.radius, 0)

        else:
            pygame.draw.circle(self.screen, RED, self.position, self.radius, 0)
        
        return None
        
    def iscolide(self, pos2, r2):
        return Vector2(pos2 - self.position).length() <= r2 + self.radius

    def isinvincible(self):
        if self.invincible and time() - self.t > 1.5:
            # print("set to not invincible")
            self.invincible = False
        return self.invincible
    
    def FPS_update(constant):
        # constant = readconstant()
        # locals().update(constant)
        ball.ball_FPS = constant['FPS']
