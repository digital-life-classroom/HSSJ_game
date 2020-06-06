import pygame,sys
from settings import Setting
from jack import Jack
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
        #监视键盘与鼠标事件
        for event in pygame.event.get():
            #如果发生退出事件
            if event.type==pygame.QUIT:
                #系统退出
                sys.exit()
        pygame.display.flip()

run_game()
settings=Settings()