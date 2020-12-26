import pygame
import random
from pygame.sprite import Sprite
from game_sprite import GameSprite

class Spirit(Sprite):
    def __init__(self,screen,x,y):
        super(Spirit,self).__init__()
        # self.image=pygame.image.load("image/spirit.png")
        # self.rect=self.image.get_rect()
        self.screen=screen
        self.pos_x=x
        self.pos_y=y
        self.spirit_group=pygame.sprite.OrderedUpdates()         #按添加顺序绘制sprite类
        self.game_spirit=GameSprite('image/spirit_sprite.png',16)
        self.game_spirit.move(self.pos_x,self.pos_y)
        self.spirit_group.add(self.game_spirit)
        self.frame=0
        self.next_frame=pygame.time.get_ticks()
        self.random_direction = 1
        self.speed=0.3
    def update(self,bg_move=False,x=0,y=0,time=0,next_time=0):
        if(bg_move):
            self.pos_x += x
            self.pos_y += y
            self.game_spirit.move(self.pos_x,self.pos_y)
            self.spirit_group.draw(self.screen)

        else:
            if pygame.time.get_ticks()>self.next_frame:
                self.frame=(self.frame+1)%4
                self.next_frame+=300
                self.random_direction=random.randint(1,40)
            
            # if time < next_time:
            #     self.random_direction >=1 and self.random_direction <=10
            #     self.game_spirit.change_image(self.frame+8)
            #     self.pos_x += self.speed
            #     self.game_spirit.move(self.pos_x,self.pos_y)
            #     self.spirit_group.draw(self.screen)

            if self.random_direction >=1 and self.random_direction <=10:
                self.game_spirit.change_image(self.frame+8)
                self.pos_x += self.speed
                self.game_spirit.move(self.pos_x,self.pos_y)
                self.spirit_group.draw(self.screen)
                # self.rect.centerx += 1

            elif self.random_direction >=11 and self.random_direction <=20:
                self.game_spirit.change_image(self.frame+4)
                # self.rect.centerx -= 1
                self.pos_x -= self.speed
                self.game_spirit.move(self.pos_x,self.pos_y)
                self.spirit_group.draw(self.screen)

            elif self.random_direction >=21 and self.random_direction <=30:
                self.game_spirit.change_image(self.frame)
                # self.rect.centery += 1
                self.pos_y += self.speed
                self.game_spirit.move(self.pos_x,self.pos_y)
                self.spirit_group.draw(self.screen)

            elif self.random_direction >=31 and self.random_direction <=40:
                self.game_spirit.change_image(self.frame+12)
                # self. rect.centery -= 1
                self.pos_y -= self.speed
                self.game_spirit.move(self.pos_x,self.pos_y)
                self.spirit_group.draw(self.screen)
