import pygame,sys
from settings import Setting
from jack import Jack
import game_function as gf
def run_game():
    #初始化游戏
    pygame.init()
    #创建一个屏幕对象
    ai_setting=Setting()
    screen=pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    jack=Jack(screen)
    #设置窗口名称
    pygame.display.set_caption("唤兽世界")
    
    while True:
        gf.check_event(jack)
        gf.update_screen(screen,jack,ai_setting)
run_game()