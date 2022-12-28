from button import *
from setting import *
from gameinit import *
#### DNF

def pause_menu(screen, call_state):
    constant=readconstant()
    locals().update(constant)
    
    fpsClock = pygame.time.Clock()

    screen.fill(BLACK)
    font = pygame.font.SysFont(font__, 50)
    title = font.render("Pause Menu", True, WHITE)
    text_rect = title.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/6))
    screen.blit(title, text_rect)

    back_button=button(SCREEN_WIDTH/2,SCREEN_HEIGHT/7*2.5,SCREEN_WIDTH/3,SCREEN_HEIGHT/8,text="Continue")
    setting_button=button(SCREEN_WIDTH/2,SCREEN_HEIGHT/7*3.5,SCREEN_WIDTH/3,SCREEN_HEIGHT/8,text="Setting")
    main_button=button(SCREEN_WIDTH/2,SCREEN_HEIGHT/7*4.5,SCREEN_WIDTH/3,SCREEN_HEIGHT/8,text="Main Menu")
    quit_button=button(SCREEN_WIDTH/2,SCREEN_HEIGHT/7*5.5,SCREEN_WIDTH/3,SCREEN_HEIGHT/8,text="Quit")

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return {'from': 'pause_menu', 'to': 'play'}
            elif event.type == pygame.QUIT:
                return {'from': "pause_menu", 'to': 'quit'}
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if back_button.isOver(pos):
                    return {'from': 'pause_menu', 'to': 'play'}
                elif setting_button.isOver(pos):
                    return {'from': 'pause_menu', 'to': 'setting_menu'}
                elif main_button.isOver(pos):
                    return {'from': 'pause_menu', 'to': 'main_menu'}
                elif quit_button.isOver(pos):
                    return {'from': "pause_menu", 'to': 'quit'}
        
        mouse_pos = pygame.mouse.get_pos()
        back_button.draw(screen,mouse_pos)
        setting_button.draw(screen,mouse_pos)
        main_button.draw(screen,mouse_pos)
        quit_button.draw(screen,mouse_pos)
        pygame.display.flip()
        fpsClock.tick(FPS)

if __name__=="__main__":

    screen=gameinit()
    print(pause_menu(screen,{'to': 'main_menu'}))
    pygame.quit()
