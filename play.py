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
level_init.append({"basic_planet":[[(SCREEN_WIDTH/4,SCREEN_HEIGHT/4)],[(SCREEN_WIDTH*3/4,SCREEN_HEIGHT*3/4),2]]})
level_init.append({"basic_planet":[[(SCREEN_WIDTH/4,SCREEN_HEIGHT/4)],[(SCREEN_WIDTH*3/4,SCREEN_HEIGHT*3/4),1],[(SCREEN_WIDTH/4,SCREEN_HEIGHT*3/4),2],[(SCREEN_WIDTH*3/4,SCREEN_HEIGHT/4),3]]})

def randinscreen():
    return (random.randint(0,SCREEN_WIDTH),random.randint(0,SCREEN_HEIGHT))

def play(screen, call_state,level=0,balls=[]):
    fpsClock = pygame.time.Clock()
    planets=[]
    life=5
    running = True
    my_font = pygame.font.SysFont(font__, 30)
    #create planet
    if level > len(level_init) - 1:
        return {'from': 'play', 'to': 'end_menu', 'end_menu_title': 'The End'}
    else:
        lvlinit=level_init[level]
    for i in lvlinit.keys():
        if i=="basic_planet":
            for j in lvlinit[i]:
                p=basic_planet(screen,*j)
                planets.append(p)
    #start running
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
            balls=[]
            return {'from': 'play', 'to': 'end_menu'}

        for i in balls:
            i.move(mp)
            if i.iscolide(mp,life+5):
                life-=1
                balls.remove(i)
            if i.isinvincible()==False:
                for j in balls:
                    if i!=j and i.iscolide(j.position,j.radius):
                        balls.remove(i)
                        balls.remove(j)
                for p in planets:
                    if  i.iscolide(p.position,p.radius):
                        p.life-=1
                        balls.remove(i)
                    if p.life==0:
                        planets.remove(p)

        for p in planets:
            if (p.position-mp).length()<= life+p.radius:
                life=0
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

    play(screen,call_state,level+1,balls)

if __name__=="__main__":

    screen=gameinit()
    play(screen,{'to': 'main_menu'})
    pygame.quit()
