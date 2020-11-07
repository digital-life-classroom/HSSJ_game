import pygame
from game_sprite import GameSprite
class Attack():
    def __init__(self,screen):
        self.screen=screen
        self.hyjq_group=pygame.sprite.OrderedUpdates()
        self.game_hyjq=GameSprite('image/attack_1.png',5)
        self.hyjq_group.add(self.game_hyjq)

        self.frame=0
        self.next_frame=pygame.time.get_ticks()
        self.frame_2=0
        self.next_frame_2=pygame.time.get_ticks()
        self.frame_3=0
        self.next_frame_3=pygame.time.get_ticks()

        self.fq_group=pygame.sprite.OrderedUpdates()
        self.game_fq=GameSprite('image/attack_2.png',3)
        self.fq_group.add(self.game_fq)

        self.js_group=pygame.sprite.OrderedUpdates()
        self.game_js=GameSprite('image/defense_1.png',2)
        self.js_group.add(self.game_js)
    def blitme(self,x,y):
        self.game_hyjq.move(x,y)
        self.hyjq_group.draw(self.screen)
    def hyjq_gj(self,x,y):
        if pygame.time.get_ticks()>self.next_frame:
            self.frame=(self.frame+1)%5
            self.next_frame+=120
        self.game_hyjq.move(x,y)
        self.game_hyjq.change_image(self.frame)
        # self.game_hyjq.retate(60)
        # self.game_hyjq.change_image(5)
        self.hyjq_group.draw(self.screen)
    def fq_gj(self,x,y):
        if pygame.time.get_ticks()>self.next_frame_2:
            self.frame_2=(self.frame_2+1)%3
            self.next_frame_2+=240
        self.game_fq.move(x,y)
        self.game_fq.change_image(self.frame_2)
        self.fq_group.draw(self.screen)
    def js_fy(self):
        if pygame.time.get_ticks()>self.next_frame_3:
            self.frame_3=(self.frame_3+1)%2
            self.next_frame_3+=300
        self.game_js.move(600,400)
        self.game_js.change_image(self.frame_3)
        self.js_group.draw(self.screen)