from gameinit import *
from play import *
from main_menu import *
from end_menu import *
from setting_menu import *
from setting import *

if __name__ == '__main__':
    screen = gameinit()
    stack = [{'to': 'main_menu'}]
    constant=readconstant()
    locals().update(constant)

    pygame.mixer.music.load('res/Winterglade.mp3') 
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(bgm_volume)
    
    while len(stack) > 0:
        current_state = stack[0]
        del stack[0]
        return_state = 0

        if current_state['to'] == 'main_menu':
            return_state = main_menu(screen, current_state)
            # constant=readconstant()
            # locals().update(constant)
            # print(f'main  read {bgm_volume}')
        elif current_state['to'] == 'play':
            return_state = play(screen, current_state)
        
        elif current_state['to'] == 'setting_menu':
            return_state,constant = setting_menu(screen, current_state,constant)
            # constant=readconstant()
            # locals().update(constant)
            # print(f'main  read {bgm_volume}')
        elif current_state['to'] == 'end_menu':
            return_state = end_menu(screen, current_state)
        
        elif current_state['to'] == 'quit':
            pygame.quit()
        
        if return_state != 0:
            stack.append(return_state)

        

