import pygame
from button import *
from button import *
from play import *
from setting import *
from load_pics import *

def load():
    load_gameover_pics()

def gameover_menu(screen, caller_state):
    #get const
    constant=readconstant()
    locals().update(constant)

    fpsClock = pygame.time.Clock()

    #screen init
    screen.fill(BLACK)
    font = pygame.font.SysFont(font__, 50)
    title = font.render("Gameover", True, BLACK)


    text_rect = title.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6))
    screen.blit(title, text_rect)
    
    #play music
    if caller_state['from']=='play':
        pygame.mixer.init()
        pygame.mixer.music.load('res/rick_roll_cut.mp3')
        pygame.mixer.music.play(-1)
        music_start_time = time()
        constant['music_start_time'] = music_start_time
    
    #if sync pic
    cnt_pic = 1
    if caller_state['from']=='setting_menu':
        cnt_pic = round((time() - constant['music_start_time']) * 25) % 1501
    print(cnt_pic)


    #button init
    start_button=   button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 7 * 3, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 8, text = "Start", not_fill_in = 1)
    setting_button= button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 7 * 4, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 8, text = "Setting", not_fill_in = 1)
    quit_button=    button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 7 * 5, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 8, text = "Quit", not_fill_in = 1)
    
    while True:
        for event in pygame.event.get():
            #quit
            if event.type == pygame.QUIT:
                return {'from': 'gameover_menu', 'to': 'quit'}
            
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                #play
                if start_button.isOver(pos):
                    pygame.mixer.init()
                    pygame.mixer.music.load('res/Winterglade.mp3') 
                    pygame.mixer.music.play(-1, start=2)
                    return {'from': 'gameover_menu', 'to': 'play'}
                
                #setting_menu
                elif setting_button.isOver(pos):
                    writeconstant(constant)
                    return {'from': 'gameover_menu', 'to': 'setting_menu'}
                
                #quit
                elif quit_button.isOver(pos):
                    return {'from': 'gameover_menu', 'to': 'quit'}
        
        #get mouse pos
        mouse_pos = pygame.mouse.get_pos()

        screen.blit(pic[cnt_pic],(0, 0))
        screen.blit(title, text_rect)
        #draw button
        start_button.draw(screen,mouse_pos)
        setting_button.draw(screen,mouse_pos)
        quit_button.draw(screen,mouse_pos)
        
        cnt_pic += 1
        if cnt_pic >= 1500:
            cnt_pic = 1
        pygame.display.flip()
        fpsClock.tick(25)

        ###############DNF