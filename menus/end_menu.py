import pygame
from button import *
from button import *
from play import *
from setting import *

def end_menu(screen, caller_state):
    constant=readconstant()
    locals().update(constant)

    fpsClock = pygame.time.Clock()

    screen.fill(BLACK)
    font = pygame.font.SysFont(font__, 50)
    if 'end_menu_title' in caller_state:
        title = font.render(caller_state['end_menu_title'], True, WHITE)
    else:
        title = font.render("You Die", True, WHITE)
    text_rect = title.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/6))

    screen.blit(title, text_rect)
    start_button=button(SCREEN_WIDTH/2,SCREEN_HEIGHT/7*3,SCREEN_WIDTH/3,SCREEN_HEIGHT/8,text="Start")
    setting_button=button(SCREEN_WIDTH/2,SCREEN_HEIGHT/7*4,SCREEN_WIDTH/3,SCREEN_HEIGHT/8 ,text="Setting")
    quit_button=button(SCREEN_WIDTH/2,SCREEN_HEIGHT/7*5,SCREEN_WIDTH/3,SCREEN_HEIGHT/8,text="Quit")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                return 0
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if start_button.isOver(pos):
                    return {'from': 'end_menu', 'to': 'play'}
                elif setting_button.isOver(pos):
                    return {'from': 'end_menu', 'to': 'setting_menu'}
                elif quit_button.isOver(pos):
                    return {'from': 'end_menu', 'to': 'quit'}
        
        mouse_pos = pygame.mouse.get_pos()
        start_button.draw(screen,mouse_pos)
        setting_button.draw(screen,mouse_pos)
        quit_button.draw(screen,mouse_pos)

        pygame.display.flip()
        fpsClock.tick(FPS)

        ###############DNF