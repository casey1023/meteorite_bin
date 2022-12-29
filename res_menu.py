import pygame
from gameinit import *
from play import *
from setting import *

def res_menu(screen, call_state):
    fpsClock = pygame.time.Clock()
    
    #screen init
    screen.fill(BLACK)
    font = pygame.font.SysFont(font__, 50)
    title = font.render("Resources", True, WHITE)
    text_rect = title.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/6))
    screen.blit(title, text_rect)

    #words
    font = pygame.font.SysFont(font__, 18)
    words=['Picture Resource:',
        'Ending menu: Image by rorozoa on Freepik',
        'Setting: Freepik',
        'Music and Sound Resource:',
        'Winterglade - Makkon',
        'Never Gonna Give You Up - Rick Astley',
        'Website: Pixabay, Mixkit, Zedge']

    for i in range(len(words)):
        line = font.render(words[i], True, WHITE)
        line_rect = line.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/3 + SCREEN_HEIGHT/20*i))
        screen.blit(line, line_rect)

    #create buttons
    menu_button = button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 7 * 6, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 8, big=30, text = "Back to Menu")

    while True:
        for event in pygame.event.get():
            #quit game
            if event.type == pygame.QUIT:
                return {'from': "res_menu", 'to': 'quit'}

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                #main_menu
                if menu_button.isOver(pos):
                    return {'from': 'res_menu', 'to': 'main_menu'}
        
        #get mouse pos
        mouse_pos = pygame.mouse.get_pos()

        #draw button
        menu_button.draw(screen,mouse_pos)

        pygame.display.flip()
        fpsClock.tick(FPS)

