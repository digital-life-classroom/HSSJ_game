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
        self.next_frame_4=pygame.time.get_ticks()
        self.next_frame_5 = pygame.time.get_ticks()
        self.next_frame_5 += 7000

        self.frame_3=0
        self.next_frame_3=pygame.time.get_ticks()

        self.fq_group=pygame.sprite.OrderedUpdates()
        self.game_fq=GameSprite('image/attack_2.png',6)
        self.fq_group.add(self.game_fq)

        self.js_group=pygame.sprite.OrderedUpdates()
        self.game_js=GameSprite('image/defense_1.png',2)
        self.js_group.add(self.game_js)

        self.jq_speed=0
        self.fq_speed=0
        self.angle=0
    def blitme(self,x,y):
        self.game_hyjq.move(x,y)
        self.hyjq_group.draw(self.screen)

    def hyjq_gj(self,x,y):
        t=x
        r=y
        if pygame.time.get_ticks()>self.next_frame:
            self.frame=(self.frame+1)%5
            self.jq_speed+=8
            self.next_frame+=120
        t=x+self.jq_speed if self.angle==0 else t
        t=x-self.jq_speed if self.angle==180 else t
        r=y+self.jq_speed if self.angle==270 else r
        r=y-self.jq_speed if self.angle==90 else r
        self.game_hyjq.move(t,r)
        self.game_hyjq.change_image(self.frame)
        self.game_hyjq.retate(self.angle)
        self.hyjq_group.draw(self.screen)
        if self.frame==0:
            self.jq_speed=0
            self.next_frame=pygame.time.get_ticks()

    def fq_gj(self,x,y):
        t=x
        r=y
        if self.frame_2<5:
            if pygame.time.get_ticks()>self.next_frame_2:
                self.frame_2=(self.frame_2+1)%6
                print("-------------------------------------------------------"+str(self.frame_2)+"--------------------------------------------------------------------------")
                self.next_frame_2+=2500

        if self.frame_2<5:
            self.fq_speed=0
            self.next_frame_4=pygame.time.get_ticks()
            self.next_frame_5 = self.next_frame_4
        t=x+self.fq_speed if self.angle==0 else t
        t=x-self.fq_speed if self.angle==180 else t
        r=y+self.fq_speed if self.angle==270 else r
        r=y-self.fq_speed if self.angle==90 else r
        if self.frame_2>=5:
            if pygame.time.get_ticks()>self.next_frame_4:
                self.fq_speed+=7
                self.next_frame_4+=500
                if self.next_frame_4-self.next_frame_5>=8000:
                    self.next_frame_2 = pygame.time.get_ticks()
                    self.frame_2=0
            self.game_fq.move(t,r)
        self.game_fq.move(t,r)
        self.game_fq.change_image(self.frame_2)
        self.fq_group.draw(self.screen)

        # if self.frame_2<5:
        #     self.fq_speed=0
            # self.next_frame_2=pygame.time.get_ticks()
            # self.next_frame_4=pygame.time.get_ticks()

    def js_fy(self):
        if pygame.time.get_ticks()>self.next_frame_3:
            self.frame_3=(self.frame_3+1)%2
            self.next_frame_3+=300
        self.game_js.move(600,400)
        self.game_js.change_image(self.frame_3)
        self.js_group.draw(self.screen)