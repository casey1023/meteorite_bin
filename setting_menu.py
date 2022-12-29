import pygame
from gameinit import *
from button import *
from slider import *
from setting import *

pic_setting = pygame.image.load("res/setting.jpg")
pic_setting_new = pygame.transform.scale(pic_setting,(SCREEN_WIDTH,SCREEN_HEIGHT))

def setting_menu(screen, call_state,constant):
    # constant=readconstant()
    # locals().update(constant)
    # print(f'setting read {bgm_volume}')
    print(constant)
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

    sound_font = pygame.font.SysFont(font__, 30)
    sound_word = sound_font.render("Sound", True, WHITE)
    sound_rect = sound_word.get_rect(center=(SCREEN_WIDTH/7,SCREEN_HEIGHT/2))
    screen.blit(sound_word, sound_rect)

    back_button = button(SCREEN_WIDTH/2,SCREEN_HEIGHT/7*6,SCREEN_WIDTH/3,SCREEN_HEIGHT/8,text="Back", norm_color=WHITE, on_color=GREY)
    music_slider = slider(SCREEN_WIDTH/7*2,SCREEN_WIDTH/7*5,SCREEN_HEIGHT/2.5, initial = constant["bgm_volume"])
    sound_slider = slider(SCREEN_WIDTH/7*2,SCREEN_WIDTH/7*5,SCREEN_HEIGHT/2, initial = constant["sound_volume"], pop_sound = True)
    print(sound_slider.pop_sound)
    

    # pygame.mixer.music.load('res/Winterglade.mp3') 
    # pygame.mixer.music.play()
    # pygame.mixer.music.set_volume(bgm_volume)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return {'from': "setting_menu", 'to': 'quit'} , constant
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if back_button.isOver(pos):
                    return {'from': 'setting_menu', 'to': call_state['from']} , constant
        

        mouse_pos = pygame.mouse.get_pos()
        screen.blit(pic_setting_new,(0,0))
        back_button.draw(screen,mouse_pos)
        screen.blit(title, text_rect)
        screen.blit(music_word, music_rect)
        screen.blit(sound_word, sound_rect)
        music_slider.draw(screen,mouse_pos,pygame.mouse.get_pressed()[0])
        sound_slider.draw(screen,mouse_pos,pygame.mouse.get_pressed()[0])
        constant["bgm_volume"] = music_slider.value()
        constant["sound_volume"] = sound_slider.value()
        
        pygame.mixer.music.set_volume(constant["bgm_volume"])
        pop_sound.set_volume(constant["sound_volume"])
        pygame.display.flip()
        fpsClock.tick(FPS)

if __name__=="__main__":

    screen=gameinit()
    setting_menu(screen, {'to': 'settings'})
    pygame.quit()