from gameinit import *
from constant import *
from play import *
from main_menu import *
from end_menu import *
from setting_menu import *

if __name__ == '__main__':
    screen = gameinit()
    stack = [{'to': 'main_menu'}]
    
    while len(stack) > 0:
        current_state = stack[0]
        del stack[0]
        return_state = 0

        if current_state['to'] == 'main_menu':
            return_state = main_menu(screen, current_state)
        
        elif current_state['to'] == 'play':
            return_state = play(screen, current_state)
        
        elif current_state['to'] == 'setting':
            return_state = setting_menu(screen, current_state)
        
        elif current_state['to'] == 'end_menu':
            return_state = end_menu(screen, current_state)
        
        elif current_state['to'] == 'quit':
            pygame.quit()
        
        if return_state != 0:
            stack.append(return_state)

        

