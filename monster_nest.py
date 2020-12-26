import pygame
import random
from pygame.sprite import Sprite
from game_sprite import GameSprite
class Monster_nest(Sprite):
    def __init__(self,screen):
        super(Monster_nest,self).__init__()
        self.screen=screen
        self.spirit_treehole_x = random.randint(0,1201)
        self.spirit_treehole_y = random.randint(0,801)
        self.spirit_treehole_image = pygame.image.load('image/spirit_treehole.png')
        self.rect_spirit_treehole = self.spirit_treehole_image.get_rect()
        self.rect_spirit_treehole.right = self.spirit_treehole_x
        self.rect_spirit_treehole.centery = self.spirit_treehole_y

    def update(self,bg_move=False,x=0,y=0):
        self.spirit_treehole_x += x
        self.spirit_treehole_y += y
        self.rect_spirit_treehole.right = self.spirit_treehole_x
        self.rect_spirit_treehole.centery = self.spirit_treehole_y
        self.screen.blit(self.spirit_treehole_image,self.rect_spirit_treehole)