import pygame
import random
from game_sprite import GameSprite
from pygame.sprite import Sprite

class Gem(Sprite):
    def __init__(self,screen):
        super(Gem,self).__init__()
        self.screen=screen
        self.xlbs_1_image=pygame.image.load('image/xlbs_1.png')
        self.rect_xlbs_1=self.xlbs_1_image.get_rect()
        self.screen_rect_xlbs_1=screen.get_rect()
        self.rect_xlbs_1.centerx=self.screen_rect_xlbs_1.centerx
        self.rect_xlbs_1.centery=self.screen_rect_xlbs_1.centery

        self.xlbs_2_image=pygame.image.load('image/xlbs_2.png')
        self.rect_xlbs_2=self.xlbs_2_image.get_rect()
        self.screen_rect_xlbs_2=screen.get_rect()
        self.rect_xlbs_2.centerx=self.screen_rect_xlbs_2.centerx
        self.rect_xlbs_2.centery=self.screen_rect_xlbs_2.centery
        self.x=random.randint(0,1201)
        self.y=random.randint(0,801)
        self.judge=random.randint(0,21)
    def update(self,bg_move=False,x=0,y=0):
        self.x=self.x+x
        self.y=self.y+y
        if self.judge<=15:
            self.screen.blit(self.xlbs_1_image,(self.x,self.y))
        else:
            self.screen.blit(self.xlbs_2_image,(self.x,self.y))