import pygame
import random
from pygame.sprite import Sprite

class Spirit(Sprite):
    def __init__(self):
        super(Spirit,self).__init__()
        self.image=pygame.image.load("image/spirit.png")
        self.rect=self.image.get_rect()
    def update(self):
        a=random.randint(1,4)
        if a==1:
            self.rect.centerx += 1
        elif a==2:
            self.rect.centerx -= 1
        elif a==3:
            self.rect.centery += 1
        elif a==4:
            self. rect.centery -= 1
        