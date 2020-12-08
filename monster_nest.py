import pygame
import random
from pygame.sprite import Sprite
from game_sprite import GameSprite
class Monster_nest():
    def __init__(self,screen):
        self.screen=screen

        self.spirit_treehole_x = random.randint(0,1201)
        self.spirit_treehole_y = random.randint(0,801)
        self.spirit_treehole_image = pygame.image.load('image/spirit_treehole.png')
        self.rect_spirit_treehole = self.spirit_treehole_image.get_rect()
        self.screen_rect_spirit_treehole = screen.get_rect()
        self.rect_spirit_treehole.centerx = self.screen_rect_spirit_treehole.centerx
        self.rect_spirit_treehole.centery = self.screen_rect_spirit_treehole.centery

    def spirit_treehole(self):
        self.screen.blit(self.spirit_treehole_image,(self.x,self.y))