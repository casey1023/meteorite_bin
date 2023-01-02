from ThreadWithReturnValue import *
import threading
import pygame

#load pic
pic = {}
def load_pics(a, b):
    for i in range(a, b):
        pic[i] = pygame.image.load('res/rick_roll/output_{:0>4}.jpg'.format(i))

def load_gameover_pics():
    threads = 10
    start = 1
    end = 1501
    num = [start]
    for i in range(1, threads):
        num.append(1501 // threads * i)
    num.append(end)

    load = []
    for i in range(1, threads + 1):
        load.append(ThreadWithReturnValue(target = load_pics, args=(num[i - 1], num[i])))
    
    for i in load:
        i.start()
    
    for i in load:
        i.join()
    '''
    load_0 = ThreadWithReturnValue(target = load_pics, args=(1, 375))
    load_1 = ThreadWithReturnValue(target = load_pics, args=(375, 750))
    load_2 = ThreadWithReturnValue(target = load_pics, args = (750, 1125))
    load_3 = ThreadWithReturnValue(target = load_pics, args = (1125, 1501))

    load_0.start()
    load_1.start()
    load_2.start()
    load_3.start()

    load_0.join()
    load_1.join()
    load_2.join()
    load_3.join()
    '''