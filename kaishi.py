import pygame,sys

class Kaishi():
    def __init__(self,screen):
        self.screen=screen
        self.theInmage=pygame.image.load('image/开始界面.png')
        self.theInmageTwo=pygame.image.load('image/结束界面.png')
        self.theInmageThree=pygame.image.load('image/胜利界面.png')
    def kaishi(self):
        self.screen.blit(self.theInmage,(0,0))
    def jieshu(self):
        self.screen.blit(self.theInmageTwo,(0,0))
    def shengli(self):
        self.screen.blit(self.theInmageThree,(0,0))