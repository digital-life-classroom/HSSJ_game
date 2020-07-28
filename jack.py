import pygame
from game_sprite import GameSprite

class Jack():
    def __init__(self,screen,gf):
        self.screen=screen
        self.image=pygame.image.load('image/jack-forward.png')
        self.rect=self.image.get_rect()  #把图片设置为矩形，把图片放入碰撞矩形
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.centery=self.screen_rect.centery
        self.gf=gf
        self.jack_group=pygame.sprite.OrderedUpdates()         #按添加顺序绘制sprite类
        self.game_jack=GameSprite('image/jack_sprite.png',16)
        self.game_jack.move(600,400)
        self.jack_group.add(self.game_jack)
        self.jack_group.draw(screen)
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def jack_move(self,next_frame,frame,background):
        if pygame.time.get_ticks()>next_frame:
            frame=(frame+1)%4
            next_frame+=120
        if self.gf.key_pressed(pygame.K_RIGHT):
            self.game_jack.change_image(frame+8)
            background.move(-1,0)
            self.jack_group.draw(self.screen)
        elif self.gf.key_pressed(pygame.K_LEFT):
            self.game_jack.change_image(frame+4)
            background.move(1,0)
            self.jack_group.draw(self.screen)
        elif self.gf.key_pressed(pygame.K_UP):
            self.game_jack.change_image(frame+12)
            background.move(0,1)
            self.jack_group.draw(self.screen)
        elif self.gf.key_pressed(pygame.K_DOWN):
            self.game_jack.change_image(frame)
            background.move(0,-1)
            self.jack_group.draw(self.screen)
        