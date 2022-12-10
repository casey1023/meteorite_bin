import pygame
import random
from pygame.math import Vector2
from gameinit import *
from constant import *
from end_menu import *
from ball import *
from planet import *
from pause_menu import *

level_init=[]
level_init.append({"basic_planet":[[(SCREEN_WIDTH/4,SCREEN_HEIGHT/4)],[(SCREEN_WIDTH*3/4,SCREEN_HEIGHT*3/4)]]})
level_init.append({"basic_planet":[[(SCREEN_WIDTH/4,SCREEN_HEIGHT/4)],[(SCREEN_WIDTH*3/4,SCREEN_HEIGHT*3/4)],[(SCREEN_WIDTH/4,SCREEN_HEIGHT*3/4)],[(SCREEN_WIDTH*3/4,SCREEN_HEIGHT/4)]]})

def randinscreen():
    return (random.randint(0,SCREEN_WIDTH),random.randint(0,SCREEN_HEIGHT))

def play(screen, call_state,level=0):
    fpsClock = pygame.time.Clock()
    balls=[]
    planets=[]
    life=5
    running = True
    my_font = pygame.font.SysFont(font__, 30)
    lvlinit=level_init[level]
    for i in lvlinit.keys():
        if i=="basic_planet":
            for j in lvlinit[i]:
                p=basic_planet(screen,*j)
                planets.append(p)
    while running and len(planets):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    #important stop
                    return 0
                elif event.key == pygame.K_RIGHT:
                    b=ball(screen,randinscreen())
                    balls.append(b)
            elif event.type == pygame.QUIT:
                running = False
                return {'from': 'play', 'to': 'quit'}

        screen.fill(BLACK)
        mp=Vector2(pygame.mouse.get_pos())
        if life!=0:
            pygame.draw.circle(screen,WHITE,mp,life+5,0)
        else:
            return {'from': 'play', 'to': 'end_menu'}

        for i in balls:
            i.move(mp)
            if i.iscolide(mp,life+5):
                life-=1
                balls.remove(i)
            for p in planets:
                if i.isinvincible()==False and i.iscolide(p.position,p.radius):
                    p.life-=1
                    balls.remove(i)
                if p.life==0:
                    planets.remove(p)

        for p in planets:
            p.draw()
            b=p.addball(mp)
            if b:
                balls.append(b)

        lifetext = my_font.render('Life : '+str(life), False, (0,0,255))
        screen.blit(lifetext, (5,5))
        lvltext = my_font.render('LVL : '+str(level), False, (0,0,255))
        screen.blit(lvltext, (SCREEN_WIDTH-100,5))
        pygame.display.flip()
        fpsClock.tick(FPS)

    play(screen,call_state,level+1)

if __name__=="__main__":

    screen=gameinit()
    play(screen,{'to': 'main_menu'})
    pygame.quit()
