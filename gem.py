import pygame
import random
from game_sprite import GameSprite
from pygame.sprite import Sprite

class Gem(Sprite):
    def __init__(self,screen):
        super(Gem,self).__init__()
        self.screen=screen
        self.pos_x_xlbs=random.randint(0,1201)
        self.pos_y_xlbs=random.randint(0,801)
        self.gem_group_xlbs1=pygame.sprite.OrderedUpdates()
        self.game_gem_xlbs1=GameSprite('image/xlbs_1.png',1)
        self.game_gem_xlbs1.move(self.pos_x_xlbs,self.pos_y_xlbs)
        self.gem_group_xlbs1.add(self.game_gem_xlbs1)

        self.gem_group_xlbs2=pygame.sprite.OrderedUpdates()
        self.game_gem_xlbs2=GameSprite('image/xlbs_2.png',1)
        self.game_gem_xlbs2.move(self.pos_x_xlbs,self.pos_y_xlbs)
        self.gem_group_xlbs2.add(self.game_gem_xlbs2)

        self.x=self.pos_x_xlbs
        self.y=self.pos_y_xlbs
        self.judge=random.randint(0,21)
    def update(self,bg_move=False,x=0,y=0):
        self.x=self.x+x
        self.y=self.y+y
        if self.judge<=15:
            self.gem_group_xlbs1.draw(self.screen)
            self.game_gem_xlbs1.move(self.x,self.y)
        else:
            self.gem_group_xlbs2.draw(self.screen)
            self.game_gem_xlbs2.move(self.x,self.y)