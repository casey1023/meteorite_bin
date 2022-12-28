import pygame
import random
from pygame.math import Vector2
from gameinit import *
from ball import *
from planet import *
from setting import *
from time import time

constant=readconstant()
locals().update(constant)
pygame.mixer.init()
pop_sound = pygame.mixer.Sound('res/p.wav')
level_init=[]

#lv1
level_init.append({"basic_planet":[[(SCREEN_WIDTH/4,SCREEN_HEIGHT/4),0,1,20,3],[(SCREEN_WIDTH*3/4,SCREEN_HEIGHT*3/4),1.5,1,20,3]]})
#lv2
level_init.append({"basic_planet":[[(SCREEN_WIDTH/4,SCREEN_HEIGHT/4)],[(SCREEN_WIDTH*3/4,SCREEN_HEIGHT*3/4),1],[(SCREEN_WIDTH/4,SCREEN_HEIGHT*3/4),2],[(SCREEN_WIDTH*3/4,SCREEN_HEIGHT/4),3]]})
#lv3
level_init.append({"basic_planet":[[(SCREEN_WIDTH*2/4,SCREEN_HEIGHT/4)],[(SCREEN_WIDTH/4,SCREEN_HEIGHT*2/4),1],[(SCREEN_WIDTH*3/4,SCREEN_HEIGHT*2/4),2],[(SCREEN_WIDTH/2,SCREEN_HEIGHT*3/4)]]})
#lv4
level_init.append({"basic_planet":[[(SCREEN_WIDTH*15/30,SCREEN_HEIGHT/30),0,1],[(SCREEN_WIDTH*15/30,SCREEN_HEIGHT*3/30),1,1],[(SCREEN_WIDTH*15/30,SCREEN_HEIGHT*5/30),2,1],[(SCREEN_WIDTH*15/30,SCREEN_HEIGHT*7/30),3,1]
,[(SCREEN_WIDTH*15/30,SCREEN_HEIGHT*9/30),0,1],[(SCREEN_WIDTH*15/30,SCREEN_HEIGHT*11/30),1,1],[(SCREEN_WIDTH*15/30,SCREEN_HEIGHT*13/30),2,1],[(SCREEN_WIDTH*15/30,SCREEN_HEIGHT*15/30),3,1]
,[(SCREEN_WIDTH*15/30,SCREEN_HEIGHT*17/30),0,1],[(SCREEN_WIDTH*15/30,SCREEN_HEIGHT*19/30),1,1],[(SCREEN_WIDTH*15/30,SCREEN_HEIGHT*21/30),2,1],[(SCREEN_WIDTH*15/30,SCREEN_HEIGHT*23/30),3,1]
,[(SCREEN_WIDTH*15/30,SCREEN_HEIGHT*25/30),0,1],[(SCREEN_WIDTH*15/30,SCREEN_HEIGHT*27/30),1,1],[(SCREEN_WIDTH*15/30,SCREEN_HEIGHT*29/30),2,1]]})
#lv5
level_init.append({"basic_planet":[[(SCREEN_WIDTH*15/30,SCREEN_HEIGHT*5/30),1,10,100,0.5]]})
#lv6
level_init.append({"basic_planet":[[(SCREEN_WIDTH*7.5/30,SCREEN_HEIGHT*6/30),0,2,20,0.5],[(SCREEN_WIDTH*15/30,SCREEN_HEIGHT*6/30),0,2,20,0.5],[(SCREEN_WIDTH*22.5/30,SCREEN_HEIGHT*6/30),0,2,20,0.5]
,[(SCREEN_WIDTH*7.5/30,SCREEN_HEIGHT*24/30),4,2,20,0.5],[(SCREEN_WIDTH*15/30,SCREEN_HEIGHT*24/30),4,2,20,0.5],[(SCREEN_WIDTH*22.5/30,SCREEN_HEIGHT*24/30),4,2,20,0.5]]})
#lv7
level_init.append({"basic_planet":[[(SCREEN_WIDTH*25/30,SCREEN_HEIGHT*5/30),0,2,7,0.5]]})
#lv8
level_init.append({"basic_planet":[[(SCREEN_WIDTH*5/30,SCREEN_HEIGHT*5/30),0,1,10,2],[(SCREEN_WIDTH*15/30,SCREEN_HEIGHT*5/30),1,2,15,2],[(SCREEN_WIDTH*25/30,SCREEN_HEIGHT*5/30),0,1,10,2]
,[(SCREEN_WIDTH*5/30,SCREEN_HEIGHT*15/30),1,2,15,2],[(SCREEN_WIDTH*25/30,SCREEN_HEIGHT*15/30),1,2,15,2]
,[(SCREEN_WIDTH*5/30,SCREEN_HEIGHT*25/30),0,1,10,2],[(SCREEN_WIDTH*15/30,SCREEN_HEIGHT*25/30),1,2,15,2],[(SCREEN_WIDTH*25/30,SCREEN_HEIGHT*25/30),0,1,10,2]]})
#lv9(先打眼睛)
level_init.append({"basic_planet":[[(SCREEN_WIDTH*10/30,SCREEN_HEIGHT*10/30),1,2,20,20],[(SCREEN_WIDTH*20/30,SCREEN_HEIGHT*10/30),1,2,20,20]
,[(SCREEN_WIDTH*15/30,SCREEN_HEIGHT*25/30),0,1,20,1.5],[(SCREEN_WIDTH*13/30,SCREEN_HEIGHT*24.4/30),1,1,20,1.5],[(SCREEN_WIDTH*17/30,SCREEN_HEIGHT*24.4/30),1,1,20,1.5],[(SCREEN_WIDTH*11/30,SCREEN_HEIGHT*23.5/30),2,1,20,1.5],[(SCREEN_WIDTH*19/30,SCREEN_HEIGHT*23.5/30),2,1,20,1.5],[(SCREEN_WIDTH*9/30,SCREEN_HEIGHT*22/30),3,1,20,1.5],[(SCREEN_WIDTH*21/30,SCREEN_HEIGHT*22/30),3,1,20,1.5]]})
#lv10
#lv11
#lv12
#lv13
#lv14
# #lvmax

# level_init.append({"basic_planet":[[(SCREEN_WIDTH/4,SCREEN_HEIGHT/4)],[(SCREEN_WIDTH*3/4,SCREEN_HEIGHT*3/4),2]]})
# level_init.append({"basic_planet":[[(SCREEN_WIDTH/4,SCREEN_HEIGHT/4)],[(SCREEN_WIDTH*3/4,SCREEN_HEIGHT*3/4),1],[(SCREEN_WIDTH/4,SCREEN_HEIGHT*3/4),2],[(SCREEN_WIDTH*3/4,SCREEN_HEIGHT/4),3]]})

title=["idk" for i in range(10)]

def randinscreen():
    return (random.randint(0,SCREEN_WIDTH),random.randint(0,SCREEN_HEIGHT))

def play(screen, call_state,level=0,balls=[],planets=[],life=5):
    constant=readconstant()
    locals().update(constant)
    fpsClock = pygame.time.Clock()
    t=time()
    running = True
    my_font = pygame.font.SysFont(font__, 30)
   
    if level > len(level_init) - 1:
        return {'from': 'play', 'to': 'end_menu', 'end_menu_title': 'The End'},0,[],[],5
    else:
        lvlinit=level_init[level]
     #create planet
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
    while running and len(planets):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    #important stop
                    return {'from': 'play', 'to': 'pause'},level,balls,planets,life
                elif event.key == pygame.K_RIGHT:
                    b=ball(screen,randinscreen())
                    balls.append(b)
                elif event.key == pygame.K_DOWN:#cheat
                    planets.clear()
                    balls.clear()
                    return play(screen,call_state,level+1)
            elif event.type == pygame.QUIT:
                running = False
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
                    if  i.iscolide(p.position,p.radius):
                        p.life-=1
                        if i in balls:
                            balls.remove(i)
                    if p.life==0:
                        planets.remove(p)
                        if isinstance(p,explode_planet):#handle explode planet
                            balls.extend(p.explode())

        for p in planets:
            if (p.position-mp).length()<= life+p.radius and t+1<time():
                life=0
            p.draw()
            b=p.addball(mp)
            if b:
                balls.extend(b)

        lifetext = my_font.render('Life : '+str(life), False, (0,0,255))
        screen.blit(lifetext, (5,5))
        lvltext = my_font.render('LVL : '+str(level), False, (0,0,255))
        screen.blit(lvltext, (SCREEN_WIDTH-100,5))
        titletext = my_font.render(title[level], False, (0,0,255))
        text_rect = titletext.get_rect(center=(SCREEN_WIDTH/2,10))
        screen.blit(titletext, text_rect)
        pygame.display.flip()
        fpsClock.tick(FPS)

    return play(screen,call_state,level+1,balls)

if __name__=="__main__":

    screen=gameinit()
    play(screen,{'to': 'main_menu'})
    pygame.quit()
