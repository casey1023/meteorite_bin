import pygame
from gameinit import *
from constant import *
from button import *
from constant import *

pic_setting = pygame.image.load("setting.jpg")
pic_setting_new = pygame.transform.scale(pic_setting,(SCREEN_WIDTH,SCREEN_HEIGHT))

def setting_menu(screen, call_state):
    fpsClock = pygame.time.Clock()

    screen.fill(BLACK)
    font = pygame.font.SysFont(font__, 50)
    title = font.render("Setting", True, WHITE)
    text_rect = title.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4))
    screen.blit(pic_setting_new,(0,0))
    screen.blit(title, text_rect)
    
    back_button = button(SCREEN_WIDTH/2,SCREEN_HEIGHT/7*6,SCREEN_WIDTH/3,SCREEN_HEIGHT/8,text="Back", norm_color=WHITE, on_color=GREY)
    music_slider = pygame.draw.circle(screen,(0,0,0), (35,35), 35, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return {'from': "setting_menu", 'to': 'quit'}
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if back_button.isOver(pos):
                    return {'from': 'setting_menu', 'to': call_state['from']}
        

        mouse_pos = pygame.mouse.get_pos()
        
        screen.blit(pic_setting_new,(0,0))
        back_button.draw(screen,mouse_pos)
        screen.blit(title, text_rect)

        if pygame.mouse.get_pressed()[0]:
            music_slide = pygame.draw.circle(screen,(0,0,0), mouse_pos, 10, 0)

        pygame.display.flip()


        fpsClock.tick(FPS)

if __name__=="__main__":

    screen=gameinit()
    setting_menu(screen, {'to': 'settings'})
    pygame.quit()