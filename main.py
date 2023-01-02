from gameinit import *
from play import *
from main_menu import *
from intro_menu import*
from res_menu import *
from win_menu import *
from gameover_menu import *
from setting_menu import *
from pause_menu import *
from setting import *
from ThreadWithReturnValue import *


if __name__ == '__main__':
    #game init
    screen = gameinit()

    #const init
    constant=readconstant()
    locals().update(constant)

    #music init
    pygame.mixer.init()
    pygame.mixer.music.load('res/Winterglade.mp3') 
    pygame.mixer.music.play(-1, start=2)
    pygame.mixer.music.set_volume(bgm_volume)

    #audio effect
    click_sound = pygame.mixer.Sound('res/metal.wav')
    pop_sound = pygame.mixer.Sound('res/pop.wav')

    #load pics
    first_time = True


    #play basic setting
    balls = []
    planets = []
    life = 5
    level = 0

    #start game
    stack = [{'to': 'main_menu'}]   #work thread

    while len(stack) > 0:

        current_state = stack[0]
        del stack[0]
        return_state = 0
        #main_menu
        if current_state['to'] == 'main_menu':
            #renew game state
            balls = []
            planets = []
            life = 5
            level = 0

            #enter main_menu while threading load_pics
            if first_time:
                load()
                return_state = main_menu(screen, current_state)
                first_time = False
            else:
                return_state = main_menu(screen, current_state)

            #return audio effect
            click_sound.set_volume(constant["sound_volume"])
            click_sound.play()

        #intro_menu
        if current_state['to'] == 'intro_menu':

            #start main_menu
            return_state = intro_menu(screen, current_state)

            #return audio effect
            click_sound.set_volume(constant["sound_volume"])
            click_sound.play()
        
        #res_menu
        if current_state['to'] == 'res_menu':

            #start main_menu
            return_state = res_menu(screen, current_state)

            #return audio effect
            click_sound.set_volume(constant["sound_volume"])
            click_sound.play()

        #play
        elif current_state['to'] == 'play':
            #start play and get current play state
            return_state, level, balls, planets, life = play(screen, current_state,constant, level, balls, planets, life)

        #pause menu
        elif current_state['to'] == 'pause_menu':
            #start pause_menu
            return_state = pause_menu(screen, current_state)
            click_sound.play()
        
        #setting menu
        elif current_state['to'] == 'setting_menu':
            #start setting_menu and get new constant
            return_state, constant = setting_menu(screen, current_state, constant)

            #update constant
            writeconstant(constant)

            #audio effect
            click_sound.set_volume(constant["sound_volume"])
            click_sound.play()

        #win_menu
        elif current_state['to'] == 'win_menu':
            #renew game state
            balls = []
            planets = []
            life = 5
            level = 0
            #start end_menu
            return_state = win_menu(screen, current_state)
            #audio effect
            click_sound.play()
        
        #gameover_menu
        elif current_state['to'] == 'gameover_menu':
            #renew game state
            balls = []
            planets = []
            life = 5
            level = 0
            #start end_menu
            return_state = gameover_menu(screen, current_state)
            #audio effect
            click_sound.play()
        
        #quit
        elif current_state['to'] == 'quit':
            pygame.quit()
        
        #add new work or state in thread
        if return_state != 0:
            stack.append(return_state)

        

