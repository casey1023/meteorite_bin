import pygame
import random
from pygame.math import Vector2
from gameinit import *
from ball import *
from planet import *
from setting import *
from time import time
from level_map import *

constant=readconstant()
locals().update(constant)
pygame.mixer.init()
pop_sound = pygame.mixer.Sound('res/p.wav')

title=["idk" for i in range(10)]
title[0]="Basic"

invt=5


def randinscreen():
    return (random.randint(0,SCREEN_WIDTH),random.randint(0,SCREEN_HEIGHT))

def play(screen, call_state,level=0,balls=[],planets=[],life=5):
    constant=readconstant()
    locals().update(constant)
    fpsClock = pygame.time.Clock()
    t=time()
    my_font = pygame.font.SysFont(font__, 30)

    #handle if pause
    if call_state["from"]=="pause" and len(planets):
        for p in planets:
            p.t=time()
            p.beforeoffset=True
   
    if level > len(level_init) - 1:
        return {'from': 'play', 'to': 'end_menu', 'end_menu_title': 'The End'},0,[],[],5
    else:
        lvlinit=level_init[level]
    #create planet if not already exist
    if len(planets)==0:
        for i in lvlinit.keys():
            if i=="basic_planet":
                for j in lvlinit[i]:
                    p=basic_planet(screen,*j)
                    planets.append(p)
            elif i=="triple_shoot_planet":
                for j in lvlinit[i]:
                    p=triple_shoot_planet(screen,*j)
                    planets.append(p)
            elif i=="explode_planet":
                for j in lvlinit[i]:
                    p=explode_planet(screen,*j)
                    planets.append(p)
    #start running
    while len(planets):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return {'from': 'play', 'to': 'pause'},level,balls,planets,life
                elif event.key == pygame.K_RIGHT:
                    b=ball(screen,randinscreen())
                    balls.append(b)
                elif event.key == pygame.K_DOWN:#cheat
                    planets.clear()
                    balls.clear()
                    return play(screen,call_state,level+1)
            elif event.type == pygame.QUIT:
                return {'from': 'play', 'to': 'quit'},0,[],[],5

        screen.fill(BLACK)
        mp=Vector2(pygame.mouse.get_pos())
        if life!=0:
            pygame.draw.circle(screen,WHITE,mp,life+5,0)
        else:
            balls.clear()
            planets.clear()
            return {'from': 'play', 'to': 'end_menu'},0,[],[],5

        for i in balls:
            i.move(mp)
            if i.iscolide(mp,life+5):
                life-=1
                pop_sound.play()
                balls.remove(i)
            if i.isinvincible()==False:
                for j in balls:
                    if i!=j and i.iscolide(j.position,j.radius):
                        if i in balls:
                            balls.remove(i)
                        balls.remove(j)
                for p in planets:
                    if  i.iscolide(p.position,p.radius) :
                        if  t+invt<time():
                            p.life-=1
                        if i in balls:
                            balls.remove(i)
                    if p.life==0:
                        planets.remove(p)
                        if isinstance(p,explode_planet):#handle explode planet
                            balls.extend(p.explode())

        for p in planets:
            if (p.position-mp).length()<= life+p.radius and t+invt<time():
                life=0
            p.draw()
            b=p.addball(mp)
            if b:
                balls.extend(b)

        lifetext = my_font.render('Life : '+str(life), False, WHITE)
        screen.blit(lifetext, (5,3))
        lvltext = my_font.render('LVL : '+str(level), False, WHITE)
        screen.blit(lvltext, (SCREEN_WIDTH-100,3))
        titletext = my_font.render(title[level], False, WHITE)
        text_rect = titletext.get_rect(center=(SCREEN_WIDTH/2,20))
        screen.blit(titletext, text_rect)
        pygame.display.flip()
        fpsClock.tick(FPS)

    return play(screen,call_state,level+1,balls)

if __name__=="__main__":

    screen=gameinit()
    print(play(screen,{'from':"test",'to': 'main_menu'}))
    pygame.quit()
