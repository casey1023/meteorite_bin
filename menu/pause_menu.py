from ..obj.button import *
from ..constant import *


#### DNF

def pause_menu(screen, call_state):
    fpsClock = pygame.time.Clock()

    screen.fill(BLACK)
    font = pygame.font.SysFont(font__, 50)
    title = font.render("Pause Menu", True, WHITE)
    text_rect = title.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/6))
    screen.blit(title, text_rect)

    back_button=button(SCREEN_WIDTH/2,SCREEN_HEIGHT/7*3,SCREEN_WIDTH/3,SCREEN_HEIGHT/8,text="Back")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if back_button.isOver(pos):
                    return 0
            
        mouse_pos = pygame.mouse.get_pos()
        back_button.draw(screen,mouse_pos)

        pygame.display.flip()
        fpsClock.tick(FPS)