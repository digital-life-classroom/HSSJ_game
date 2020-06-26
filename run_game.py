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
    game_sprite=GameSprite('image/jack_sprite.png',16)
    game_sprite.move(600,400)
    while True:
        gf.check_event(background)
        # gf.update_screen(screen,jack)
        pygame.display.flip()
run_game()