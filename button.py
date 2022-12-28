import pygame
from setting import *

constant=readconstant()
locals().update(constant)

class button():
    def __init__(self, x, y, width, height, big = 40, text = '', norm_color = GREY, on_color = WHITE):
        self.norm_color = norm_color
        self.on_color = on_color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.big = big

    def draw(self, screen, mouse_pos, outline = None):
        #Call this method to draw the button on the screen
        if self.text != '':
            font = pygame.font.SysFont(font__, self.big)
            text = font.render(self.text, 1, (0,0,0))
            text_rect = text.get_rect(center = (self.x, self.y))

        if outline:
            rect_outline=pygame.Rect(self.x - 2, self.y - 2, self.width + 4, self.height + 4)
            rect.center = (self.x, self.y)
            pygame.draw.rect(screen, outline, rect_outline, 0)
        
        r = pygame.Rect(self.x, self.y, self.width, self.height)
        r.center = (self.x, self.y)
        if (self.isOver(mouse_pos)):
            pygame.draw.rect(screen, self.on_color, r, 0)
        else:
            pygame.draw.rect(screen, self.norm_color, r, 0)
        screen.blit(text, text_rect)

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x - self.width / 2 and pos[0] < self.x + self.width / 2:
            if pos[1] > self.y - self.height / 2 and pos[1] < self.y + self.height / 2:
                return True
        return False
