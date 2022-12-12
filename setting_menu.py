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
    
    music_font = pygame.font.SysFont(font__, 30)
    music_word = music_font.render("Music", True, WHITE)
    music_rect = music_word.get_rect(center=(SCREEN_WIDTH/7,SCREEN_HEIGHT/2.5))
    screen.blit(music_word, music_rect)

    back_button = button(SCREEN_WIDTH/2,SCREEN_HEIGHT/7*6,SCREEN_WIDTH/3,SCREEN_HEIGHT/8,text="Back", norm_color=WHITE, on_color=GREY)
    
    norm_color = WHITE
    on_color = GREEN
    left_limit = SCREEN_WIDTH/7*2
    right_limit = SCREEN_WIDTH/7*5
    r = 10
    y = SCREEN_HEIGHT/2.5
    position = (left_limit,y)
    clicked = False
    over = False

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
        screen.blit(music_word, music_rect)

        #is_over
        if((position[0]-mouse_pos[0])**2+(position[1]-mouse_pos[1])**2) < r**2:
            over = True
        else:
            over = False

        if pygame.mouse.get_pressed()[0] and over:
            clicked = True
        if not pygame.mouse.get_pressed()[0]:
            clicked = False

        if clicked:
            if left_limit < mouse_pos[0] < right_limit:
                position = (mouse_pos[0],y)
            elif(left_limit > mouse_pos[0]):
                position = (left_limit,y)
            elif(mouse_pos[0] > right_limit):
                position = (right_limit,y)
            music_slide = pygame.draw.circle(screen,on_color, position, r, 0)

        if not clicked:
            music_slide = pygame.draw.circle(screen,norm_color, position, r, 0)
        pygame.display.flip()
        fpsClock.tick(FPS)

if __name__=="__main__":

    screen=gameinit()
    setting_menu(screen, {'to': 'settings'})
    pygame.quit()