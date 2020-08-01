import pygame
from pygame.sprite import Sprite

class Spirit(Sprite):
    def __init__(self):
        super(Sprite,self).__init__()
        self.image=pygame.image.load("image/spirit.png")
        self.rect=self.image.get_rect()
        