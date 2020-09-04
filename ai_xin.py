import pygame
from game_sprite import GameSprite

class Ai_xin():
    def __init__(self,screen):
        self.screen=screen
        # self.ai_xin=pygame.image.load("image/爱心模型2.png")
        # self.ai_xin_rect=ai_xin.get_rect()
        # self.ai_xin_rect.centerx=200
        # self.ai_xin_rect.centery=200
        # self.screen.blit(ai_xin,ai_xin_rect)
        self.ai_xin_group=pygame.sprite.OrderedUpdates()
        self.game_ai_xin=GameSprite('image/aixin.png',7)
        self.ai_xin_group.add(self.game_ai_xin)
        self.frame=0
        self.next_frame=pygame.time.get_ticks()
    def blit_ai_xin(self):
        self.ai_xin_group.draw(self.screen)
    def js_xl(self,xl=7):
        if xl==7:
            self.game_ai_xin.change_image(7)
            self.ai_xin_group.draw(self.screen)
        elif xl==6:
            self.game_ai_xin.change_image(6)
            self.ai_xin_group.draw(self.screen)
        elif xl==5:
            self.game_ai_xin.change_image(5)
            self.ai_xin_group.draw(self.screen)
        elif xl==4:
            self.game_ai_xin.change_image(4)
            self.ai_xin_group.draw(self.screen)
        elif xl==3:
            self.game_ai_xin.change_image(3)
            self.ai_xin_group.draw(self.screen)
        elif xl==2:
            self.game_ai_xin.change_image(2)
            self.ai_xin_group.draw(self.screen)
        elif xl==1:
            self.game_ai_xin.change_image(1)
            self.ai_xin_group.draw(self.screen)