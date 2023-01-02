import pygame
from setting import *

constant=readconstant()
locals().update(constant)

class button():
    def __init__(self, x, y, width, height, big = 40, text = '', norm_color = GREY, on_color = WHITE, not_fill_in = 0):
        self.norm_color = norm_color
        self.on_color = on_color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.big = big
        self.not_fill_in = not_fill_in

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
            pygame.draw.rect(screen, self.on_color, r, self.not_fill_in)
        else:
            pygame.draw.rect(screen, self.norm_color, r, self.not_fill_in)
        screen.blit(text, text_rect)

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x - self.width / 2 and pos[0] < self.x + self.width / 2:
            if pos[1] > self.y - self.height / 2 and pos[1] < self.y + self.height / 2:
                return True
        return False

class Checkbox:
    working = {}
    def __init__(self, surface, x, y, color = (230, 230, 230), caption = "", outline_color = (0, 0, 0),
                 check_color=(0, 0, 0), font_size = 40, font_color = (0, 0, 0), text_offset = (28, 1), current_FPS = 60):
        self.surface = surface
        self.x = x
        self.y = y
        self.color = color
        self.caption = caption
        self.oc = outline_color
        self.cc = check_color
        self.fs = font_size
        self.fc = font_color
        self.to = text_offset
        # checkbox object
        self.checkbox_obj = pygame.Rect(self.x, self.y, 12, 12)
        self.checkbox_outline = self.checkbox_obj.copy()
        # variables to test the different states of the checkbox
        self.active = False
        self.click = False
        if str(current_FPS) == self.caption:
            self.checked = True
            self.unchecked = False
            Checkbox.working[self.caption] = True
        else:
            self.checked = False
            self.unchecked = True
            Checkbox.working[self.caption] = False

    def _draw_button_text(self):
        self.font = pygame.font.SysFont(font__, self.fs)
        self.font_surf = self.font.render(self.caption, True, self.fc)
        w, h = self.font.size(self.caption)
        self.font_pos = (self.x + 12 / 2 - w / 2 + self.to[0], self.y + 12 / 2 - h / 2 + self.to[1])
        self.surface.blit(self.font_surf, self.font_pos)

    def draw(self):
        if self.checked:
            pygame.draw.rect(self.surface, self.color, self.checkbox_obj)
            pygame.draw.rect(self.surface, self.oc, self.checkbox_outline, 1)
            pygame.draw.circle(self.surface, self.cc, (self.x + 6, self.y + 6), 4)

        elif self.unchecked:
            pygame.draw.rect(self.surface, self.color, self.checkbox_obj)
            pygame.draw.rect(self.surface, self.oc, self.checkbox_outline, 1)
        self._draw_button_text()

    def _update(self, event_object):
        x, y = event_object.pos
        # self.x, self.y, 12, 12
        px, py, w, h = self.checkbox_obj  # getting check box dimensions
        if px < x < px + w and py < y < py + h:
            self.active = True
        else:
            self.active = False

    def _mouse_up(self):
        if self.active and not self.checked and self.click:
                self.checked = True
                self.unchecked = False
                Checkbox.working[self.caption] = True
                for i in Checkbox.working.keys():
                    if i != self.caption:
                        Checkbox.working[i] = False

        elif self.active and self.checked and self.click:
            self.checked = False
            self.unchecked = True
            Checkbox.working[self.caption] = False
            for i in Checkbox.working.keys():
                if i != self.caption:
                    Checkbox.working[i] = True

        if self.click is True and self.active is False:
            for i in Checkbox.working.keys():
                if Checkbox.working[i] == True and i != self.caption:
                    self.checked = False
                    self.unchecked = True
                    Checkbox.working[self.caption] = False
            self.active = False
    
    def clear(self):
        if self.active is False:
            for i in Checkbox.working.keys():
                if Checkbox.working[i] == True and i != self.caption:
                    self.checked = False
                    self.unchecked = True
                    Checkbox.working[self.caption] = False
            self.active = False

    def update_checkbox(self, event_object):
        if event_object.type == pygame.MOUSEBUTTONDOWN:
            self.click = True
            # self._mouse_down()
        if event_object.type == pygame.MOUSEBUTTONUP:
            self._mouse_up()
        if event_object.type == pygame.MOUSEMOTION:
            self._update(event_object)

    def is_checked(self):
        if self.checked is True:
            return True
        else:
            return False

    def is_unchecked(self):
        if self.checked is False:
            return True
        else:
            return False