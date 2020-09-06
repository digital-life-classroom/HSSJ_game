import pygame
from game_sprite import GameSprite
class Attack():
    def __init__(self,screen):
        self.screen=screen
        self.hyjq_group=pygame.sprite.OrderedUpdates()
        self.game_hyjq=GameSprite('image/火焰剑气.png',4)
        self.hyjq_group.add(self.game_hyjq)
    def hyjq_gj(self):
        for i in range(4):
            self.game_hyjq.change_image(i)