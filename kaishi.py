import pygame,sys

class Kaishi():
    def __init__(self):
        self.theInmage=pygame.image.load('image/开始界面.png')
    def kaishi(self,screen):
        screen.blit(self.theInmage,(0,0))