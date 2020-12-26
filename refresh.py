import pygame,sys
import random
from spirit import Spirit

def spirit_refresh(screen,spirits):
    frame_spirit=pygame.time.get_ticks()
    if pygame.time.get_ticks()>frame_spirit:
        x=random.randint(0,1201)
        y=random.randint(0,801)
        spirit=Spirit(screen,x,y)
        spirits.add(spirit)
        frame_spirit+=20000
    spirits.update()