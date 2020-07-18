import pygame,sys
from settings import Setting
from jack import Jack
import game_function as gf
from background import Background
from game_sprite import GameSprite

def run_game():
    #初始化游戏
    pygame.init()
    #创建一个屏幕对象
    ai_setting=Setting()
    screen=pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    # jack=Jack(screen)
    background=Background(screen)
    #设置窗口名称
    pygame.display.set_caption("唤兽世界")
    background.blitme()
    sprite_group=pygame.sprite.OrderedUpdates()         #按添加顺序绘制sprite类
    game_sprite=GameSprite('image/jack_sprite.png',16)
    game_sprite.move(600,400)
    sprite_group.add(game_sprite)
    sprite_group.draw(screen)
    next_frame=pygame.time.get_ticks()
    frame=0
    while True:
        if pygame.time.get_ticks()>next_frame:
            frame=(frame+1)%4
            next_frame+=60
        if gf.key_pressed(pygame.K_RIGHT):
            game_sprite.change_image(frame)
            background.move(-1,0)
            sprite_group.draw(screen)
        elif gf.key_pressed(pygame.K_LEFT):
            game_sprite.change_image(frame)
            background.move(1,0)
            sprite_group.draw(screen)
        elif gf.key_pressed(pygame.K_UP):
            game_sprite.change_image(frame)
            background.move(0,1)
            sprite_group.draw(screen)
        elif gf.key_pressed(pygame.K_DOWN):
            game_sprite.change_image(frame)
            background.move(0,-1)
            sprite_group.draw(screen)
        gf.check_event(background)
        # gf.update_screen(screen,jack)
        pygame.display.flip()
        
run_game()