import pygame
import random
from pygame.math import Vector2
from gameinit import *
from ball import *
from planet import *
from setting import *
from time import time
from level_map import *

#get const
# constant = readconstant()
# locals().update(constant)

#audio effect init
pygame.mixer.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
pop_sound = pygame.mixer.Sound('res/p.wav')
smoke_bomb_sound = pygame.mixer.Sound(file = 'res/smoke_bomb.wav')


#invincible time
invt=2


def randinscreen():
    return (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))

def play(screen, call_state,constant, level = 0, balls = [], planets = [], life = 5):
    #get const
    # constant = readconstant()
    # locals().update(constant)

    #hide cursor
    pygame.mouse.set_visible(0)

    #update ball FPS
    ball.FPS_update(constant)

    #get highest level
    highest_level = get_highest_level()

    fpsClock = pygame.time.Clock()
    t = time()		#get start time

    my_font = pygame.font.SysFont(font__, 30)

    #highest lvl text
    highest_level_font = pygame.font.SysFont(font__, 25)
    highest_level_text = highest_level_font.render("HIGHEST_LVL:" + str(highest_level), True, WHITE)
    highest_level_text_rect = highest_level_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/15))
    screen.blit(highest_level_text, highest_level_text_rect)

    #handle if pause
    if call_state["from"] == "pause_menu" and len(planets):
        for p in planets:
            p.reset_time()
            p.beforeoffset = True
	
	#if ended
    if level > len(level_init) - 1:
        return {'from': 'play', 'to': 'win_menu'}, 0, [], [], 5
    else:
        lvlinit=level_init[level]
	
    #create planet if not already exist
    if len(planets)==0:

        for i in lvlinit.keys():
            if i == "basic_planet":
                for j in lvlinit[i]:
                    p = basic_planet(screen, *j)
                    planets.append(p)

            elif i == "triple_shoot_planet":
                for j in lvlinit[i]:
                    p = triple_shoot_planet(screen, *j)
                    planets.append(p)

            elif i == "explode_planet":
                for j in lvlinit[i]:
                    p = explode_planet(screen, *j)
                    planets.append(p)

    #start running
    while len(planets):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
				#pause
                if event.key == pygame.K_ESCAPE:
                    return {'from': 'play', 'to': 'pause_menu'}, level, balls, planets, life
				
				#random add ball
                elif event.key == pygame.K_RIGHT:	#random add 
                    b = ball(screen, randinscreen())
                    balls.append(b)

				#cheat
                elif event.key == pygame.K_DOWN:
                    planets.clear()
                    balls.clear()
                    return {'from': 'play', 'to': 'play'}, level + 1, [], [], 5
			
			#quit game
            elif event.type == pygame.QUIT:
                return {'from': 'play', 'to': 'quit'}, 0, [], [], 5


        screen.fill(BLACK)
        mp=Vector2(pygame.mouse.get_pos())	#get mouse position

		#update mouse position and check if the player is died
        if life != 0:
            pygame.draw.circle(screen, WHITE, mp, life + 5, 0)
        else:
            balls.clear()
            planets.clear()
            return {'from': 'play', 'to': 'gameover_menu'}, 0, [], [], 5

		#deal with balls
        for i in balls:

			#update ball pos
            i.move(mp)

			#check collide with mouse
            if i.iscolide(mp, life + 5):
                life -= 1
                balls.remove(i)
                #audio effect
                pop_sound.set_volume(constant["sound_volume"])
                pop_sound.play()
			

            if i.isinvincible() == False:
				#check collide with other balls
                for j in balls:
                    if i != j and i.iscolide(j.position, j.radius):
                        if i in balls:
                            balls.remove(i)
                        balls.remove(j)
				
				#check collide with other planets
                for p in planets:
                    if  i.iscolide(p.position, p.radius):
						#check whether in invincible time
                        if  t + invt < time():
                            p.life -= 1
						
                        if i in balls:
                            balls.remove(i)
					
					#remove dead planet
                    if p.life <= 0:
                        planets.remove(p)
                        smoke_bomb_sound.set_volume(constant["sound_volume"])
                        smoke_bomb_sound.play()
						
						#handle explode planet
                        if isinstance(p,explode_planet):
                            balls.extend(p.explode(mp))

		#check mouse collide with planets
        for p in planets:
            if (p.position - mp).length() <= life + p.radius and t + invt < time():
                life = 0
            p.draw()

            b = p.addball(mp)
            if b:
                balls.extend(b)

        #get mouse pos
        mouse_pos = pygame.mouse.get_pos()

        lifetext = my_font.render('Life : ' + str(life), False, WHITE)
        screen.blit(lifetext, (5, 3))
        lvltext = my_font.render('LVL : ' + str(level), False, WHITE)
        screen.blit(lvltext, (SCREEN_WIDTH - 100, 3))
        screen.blit(highest_level_text, highest_level_text_rect)
        titletext = my_font.render(title[level], False, WHITE)
        text_rect = titletext.get_rect(center = (SCREEN_WIDTH / 2, 20))
        screen.blit(titletext, text_rect)
        pygame.display.flip()
        fpsClock.tick(constant['FPS'])

    constant['finished_level'][level] = 1
    writeconstant(constant)
    return {'from': 'play', 'to': 'play'}, level + 1, [], [], 5

if __name__=="__main__":

    screen = gameinit()
    print(play(screen, {'from': "test", 'to': 'main_menu'}))
    pygame.quit()
