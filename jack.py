import pygame
class Jack():
    def __init__(self,screen):
        self.screen=screen
        self.image=pygame.image.load('image/jack-forward.png')
        self.rect=self.image.get_rect()  #把图片设置为矩形，把图片放入碰撞矩形