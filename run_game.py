import pygame,sys
import random
from settings import Setting
from jack import Jack
# import game_function as gf
from game_function import Game_function
from background import Background
from game_sprite import GameSprite
from jifen import JiFen
from kaishi import Kaishi
from spirit import Spirit
from pygame.sprite import Group
from ai_xin import Ai_xin

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

    gf=Game_function(screen)

    jifen=JiFen()
    
    kai_shi=Kaishi()
    kai_shi.kaishi(screen)

    begingame=False
    pygame.mixer.music.load("music/begin_music.wav")
    pygame.mixer.music.play(-1,0)

    spirits=Group()
    for i in range(6):
        spirit=Spirit()
        spirits.add(spirit)
        a=random.randint(0,1201)
        b=random.randint(0,801)
        spirit.rect.centerx=a
        spirit.rect.centery=b

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                #系统退出
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    begingame=True
                    background.blitme()

                    jack=Jack(screen,gf)

                    jifen.blit_me(screen)
                    
                    spirit_group=pygame.sprite.OrderedUpdates()

                    game_spirit=GameSprite('image/spirit_sprite.png',16)
                    # game_spirit.move(730,200)
                    # spirit_group.add(game_spirit)
                    # spirit_group.draw(screen)
                    # jifen.blit_me(screen)

                    # for i in range(3):
                        # a=random.randint(0,1201)
                        # b=random.randint(0,801)
                    #     game_spirit.move(a,b)
                    #     spirit_group.add(game_spirit)
                    #     spirit_group.draw(screen)
                    #     game_spirit.change_image(4)

                    pygame.mixer.music.load("music/music.wav")
                    pygame.mixer.music.play(-1,0)

                    ai_xin=Ai_xin(screen)

                    jack.blitme()
        if begingame==True:
            jack.jack_move(background)

            spirits.update()
            spirits.draw(screen)

            jifen.blit_me(screen)

            ai_xin.blit_ai_xin()
        # gf.check_event()

        # gf.update_screen(screen,jack)

        pygame.display.flip()
        
run_game()
#1062,1065,1071,1072,1086