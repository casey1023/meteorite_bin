import pygame
from gameinit import *
from play import *
from setting import *

def main_menu(screen, call_state):
    fpsClock = pygame.time.Clock()
    
    #screen init
    screen.fill(BLACK)
    font = pygame.font.SysFont(font__, 50)
    title = font.render("Meteorite Bin", True, WHITE)
    text_rect = title.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/6))
    screen.blit(title, text_rect)

    #create buttons
    start_button =      button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 7 * 3, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 8, text = "Start")
    setting_button =    button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 7 * 4, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 8,text = "Setting")
    intro_button =      button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 7 * 5, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 8, text = "Introduction",big = 30)
    quit_button =       button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 7 * 6, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 8, text = "Quit")
    res_button =        button(SCREEN_WIDTH / 7*6, SCREEN_HEIGHT / 11*10, SCREEN_WIDTH / 6, SCREEN_HEIGHT / 15, big = 20, text = "Resources")

    while True:
        for event in pygame.event.get():
            #quit game
            if event.type == pygame.QUIT:
                return {'from': "main_menu", 'to': 'quit'}

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                #play
                if start_button.isOver(pos):
                    return {'from': 'main_menu', 'to': 'play'}

                #setting_menu
                elif setting_button.isOver(pos):
                    return {'from': 'main_menu', 'to': 'setting_menu'}
                
                #intro_menu
                elif intro_button.isOver(pos):
                    return {'from': 'main_menu', 'to': 'intro_menu'}
                #res_menu
                elif res_button.isOver(pos):
                    return {'from': 'main_menu', 'to': 'res_menu'}
                #quit
                elif quit_button.isOver(pos):
                    return {'from': "main_menu", 'to': 'quit'}
        
        #get mouse pos
        mouse_pos = pygame.mouse.get_pos()

        #draw button
        start_button.draw(screen,mouse_pos)
        setting_button.draw(screen,mouse_pos)
        intro_button.draw(screen,mouse_pos)
        quit_button.draw(screen,mouse_pos)
        res_button.draw(screen,mouse_pos)
        pygame.display.flip()
        fpsClock.tick(FPS)


if __name__=="__main__":

    screen = gameinit()
    main_menu(screen,{'to': 'main_menu'})
    pygame.quit()
