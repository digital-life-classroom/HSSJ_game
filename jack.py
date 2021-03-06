import pygame
from game_sprite import GameSprite
from ai_xin import Ai_xin
from attack import Attack
class Jack():
    def __init__(self,screen,gf):
        self.screen=screen
        # self.rect=self.image.get_rect()           #把图片设置为矩形，把图片放入碰撞矩形
        # self.screen_rect=screen.get_rect()
        # self.rect.centerx=self.screen_rect.centerx
        # self.rect.centery=self.screen_rect.centery
        self.gf=gf
        self.jack_group=pygame.sprite.OrderedUpdates()         #按添加顺序绘制sprite类
        self.game_jack=GameSprite('image/jack_sprite.png',16)
        self.game_jack.move(600,400)
        self.jack_group.add(self.game_jack)
        self.frame=0
        self.next_frame=pygame.time.get_ticks()
        self.speed=0.9
        self.direction=4
        self.wd=False
    def blitme(self):
        # self.screen.blit(self.image,self.rect)
        self.jack_group.draw(self.screen)

    def jack_move(self,background,spirits,gems,nests):
        aixin=Ai_xin(self.screen)
        if pygame.time.get_ticks()>self.next_frame:
            self.frame=(self.frame+1)%4
            self.next_frame+=200

        if self.gf.key_pressed(pygame.K_RIGHT):
            self.game_jack.change_image(self.frame+8)
            background.move(-self.speed,0)
            self.jack_group.draw(self.screen)
            spirits.update(True,-self.speed,0)
            gems.update(True,-self.speed,0)
            nests.update(True,-self.speed,0)
            self.direction=1

        elif self.gf.key_pressed(pygame.K_LEFT):
            self.game_jack.change_image(self.frame+4)
            background.move(self.speed,0)
            self.jack_group.draw(self.screen)
            spirits.update(True,self.speed,0)
            gems.update(True,self.speed,0)
            nests.update(True,self.speed,0)
            self.direction=2

        elif self.gf.key_pressed(pygame.K_UP):
            self.game_jack.change_image(self.frame+12)
            background.move(0,self.speed)
            self.jack_group.draw(self.screen)
            spirits.update(True,0,self.speed)
            gems.update(True,0,self.speed)
            nests.update(True,0,self.speed)
            self.direction=3

        elif self.gf.key_pressed(pygame.K_DOWN):
            self.game_jack.change_image(self.frame)
            background.move(0,-self.speed)
            self.jack_group.draw(self.screen)
            spirits.update(True,0,-self.speed)
            gems.update(True,0,-self.speed)
            nests.update(True,0,-self.speed)
            self.direction=4

        else:
            background.move(0,0)
            self.jack_group.draw(self.screen)

    def jack_attack(self,attack):
        if self.gf.key_pressed(pygame.K_z):

            if self.direction==1:
                attack.angle=0
                attack.hyjq_gj(630,400)

            elif self.direction==2:
                attack.angle=180
                attack.hyjq_gj(580,400)

            elif self.direction==3:
                attack.angle=90
                attack.hyjq_gj(600,370)

            elif self.direction==4:
                attack.angle=270
                attack.hyjq_gj(600,430)

        if self.gf.key_pressed(pygame.K_x):

            if self.direction==1:
                attack.angle=0
                attack.fq_gj(630,400)

            elif self.direction==2:
                attack.angle=180
                attack.fq_gj(580,400)

            elif self.direction==3:
                attack.angle=90
                attack.fq_gj(600,370)

            elif self.direction==4:
                attack.angle=270
                attack.fq_gj(600,430)

        else:
            if self.direction==1:
                attack.angle=0
                attack.fq_gj_fs()

            elif self.direction==2:
                attack.angle=180
                attack.fq_gj_fs()

            elif self.direction==3:
                attack.angle=90
                attack.fq_gj_fs()

            elif self.direction==4:
                attack.angle=270
                attack.fq_gj_fs()

        if self.gf.key_pressed(pygame.K_c):

            attack.js_fy()
            self.wd=True
        else:
            self.wd=False