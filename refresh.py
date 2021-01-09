import pygame,sys
import random
from spirit import Spirit
from gem import Gem

def spirit_refresh(screen,spirits,frame_spirit):
    if pygame.time.get_ticks()>frame_spirit:
        x=random.randint(0,1201)
        y=random.randint(0,801)
        spirit=Spirit(screen,x,y)
        spirits.add(spirit)
        frame_spirit+=30000
    spirits.update()
    return frame_spirit
def gem_refresh(screen,gems,frame_gem):
    if pygame.time.get_ticks()>frame_gem:
        gem=Gem(screen)
        gems.add(gem)
        frame_gem+=30000
    gems.update()
    return frame_gem
def treehole_spirit_refresh(screen,spirits,frame_treehole_spirit,spirit_treehole_x,spirit_treehole_y):
    if pygame.time.get_ticks()>frame_treehole_spirit:
        spirit=Spirit(screen,spirit_treehole_x,spirit_treehole_y)
        spirits.add(spirit)
        frame_treehole_spirit+=20000
    spirits.update()
    return frame_treehole_spirit