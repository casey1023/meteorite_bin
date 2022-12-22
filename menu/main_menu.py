import pygame

from gameinit import *
from ..constant import *
from play import *

def main_menu(screen, call_state):
    fpsClock = pygame.time.Clock()
    
    screen.fill(BLACK)
    font = pygame.font.SysFont(font__, 50)
    title = font.render("Meteorite Bin", True, WHITE)
    text_rect = title.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/6))
    screen.blit(title, text_rect)

    start_button=button(SCREEN_WIDTH/2,SCREEN_HEIGHT/7*3,SCREEN_WIDTH/3,SCREEN_HEIGHT/8,text="Start")
    setting_button=button(SCREEN_WIDTH/2,SCREEN_HEIGHT/7*4,SCREEN_WIDTH/3,SCREEN_HEIGHT/8 ,text="Setting")
    quit_button=button(SCREEN_WIDTH/2,SCREEN_HEIGHT/7*5,SCREEN_WIDTH/3,SCREEN_HEIGHT/8,text="Quit")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return {'from': "main_menu", 'to': 'quit'}
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if start_button.isOver(pos):
                    return {'from': 'main_menu', 'to': 'play'}
                elif setting_button.isOver(pos):
                    return {'from': 'main_menu', 'to': 'setting'}
                elif quit_button.isOver(pos):
                    return {'from': "main_menu", 'to': 'quit'}
        
        mouse_pos = pygame.mouse.get_pos()
        start_button.draw(screen,mouse_pos)
        setting_button.draw(screen,mouse_pos)
        quit_button.draw(screen,mouse_pos)

        pygame.display.flip()
        fpsClock.tick(FPS)


if __name__=="__main__":

    screen=gameinit()
    main_menu(screen)
    pygame.quit()
