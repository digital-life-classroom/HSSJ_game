import pygame
class Jack():
    def __init__(self):
        self.image=pygame.image.load('images/jack-forward。png')
        self.rect=self.image.get_rect()  #把图片设置为矩形，把图片放入碰撞矩形