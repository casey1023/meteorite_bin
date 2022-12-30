import pygame
from gameinit import *
from setting import *
from button import *

rows = 3
columns = 3

def level_menu(screen, call_state, page):
    #get const
    constant = readconstant()
    locals().update(constant)

    fpsClock = pygame.time.Clock()

    #screen init
    screen.fill(BLACK)
    font = pygame.font.SysFont(font__, 50)
    title = font.render("Choose level", True, BLACK)
    text_rect = title.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6))
    screen.blit(title, text_rect)

    #button init
    back_button = button(SCREEN_WIDTH/2,SCREEN_HEIGHT/7*6,SCREEN_WIDTH/3,SCREEN_HEIGHT/8,text="Back", norm_color=WHITE, on_color=GREY)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return {'from': "level_menu", 'to': 'quit'} , constant
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if back_button.isOver(pos):
                    return {'from': 'level_menu', 'to': 'main_menu'} , constant
            
            mouse_pos = pygame.mouse.get_pos()
            back_button.draw(screen,mouse_pos)
            screen.blit(title, text_rect)
            pygame.display.flip()
            fpsClock.tick(FPS)

if __name__ == '__main__':
    screen = gameinit()
    print(level_menu(screen, {'from': "test", 'to': 'main_menu'}, 0))
    pygame.quit()