import pygame,sys
import random
from settings import Setting
from jack import Jack
from game_function import Game_function
from background import Background
from game_sprite import GameSprite
from jifen import JiFen
from kaishi import Kaishi
from spirit import Spirit
from pygame.sprite import Group
from ai_xin import Ai_xin
from attack import Attack
from gem import Gem
from monster_nest import Monster_nest

def spirit(screen):
    frame_spirit=pygame.time.get_ticks()
    if pygame.time.get_ticks()>frame_spirit:
        x=random.randint(0,1201)
        y=random.randint(0,801)
        spirit=Spirit(screen,x,y)
        spirits.add(spirit)
        frame_spirit+=20000
    spirits.update()