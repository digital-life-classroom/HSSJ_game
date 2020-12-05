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
from attack import Attack
from gem import Gem

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

    xl=6
    for i in range(5):
        spirit=Spirit(screen)
        spirits.add(spirit)

    attack=Attack(screen)

    gems=Group()
    gem=Gem(screen)

    end=True
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

                    pygame.mixer.music.load("music/music.wav")
                    pygame.mixer.music.play(-1,0)

                    ai_xin=Ai_xin(screen)

                    jack.blitme()

                    next_frame=pygame.time.get_ticks()
                    next_frame_2=pygame.time.get_ticks()
                    next_frame_3=pygame.time.get_ticks()
                    next_frame_4=pygame.time.get_ticks()
        if begingame==True and xl>0:
            jack.jack_move(background,spirits,gems)
            jack.jack_attack(attack)

            jifen.blit_me(screen)

            ai_xin.js_xl(xl)

            if pygame.time.get_ticks()>next_frame:
                spirit=Spirit(screen)
                spirits.add(spirit)
                next_frame+=20000
            spirits.update()

            if pygame.time.get_ticks()>next_frame_3:
                gem=Gem(screen)
                gems.add(gem)
                next_frame_3+=1000
            gems.update()

            for the_spirit in spirits:
                if pygame.sprite.spritecollideany(jack.game_jack,the_spirit.spirit_group):
                    if not jack.wd:
                        if pygame.time.get_ticks()>next_frame_2:
                            next_frame_2=pygame.time.get_ticks()
                            xl_2=xl
                            xl-=1
                            if xl_2>xl:
                                jack_ss=pygame.mixer.Sound("music/jack_ss.wav")
                                jack_ss.set_volume(1)                                             #调节音量
                                jack_ss.play(0)
                            ai_xin.js_xl(xl)   #pygame.sprite.groupcollide(jack.jack_group,spirit.spirit_group,True,True) //碰撞消失
                            next_frame_2+=3000
                if pygame.sprite.groupcollide(attack.hyjq_group,the_spirit.spirit_group,True,True):
                    jifen.plus()
                if pygame.time.get_ticks()>next_frame_4:
                    attack=Attack(screen)
                    next_frame_4+=10000
            # if pygame.sprite.groupcollide(jack.jack_group,gems,True,False):
            #     xl+=1
            # elif pygame.sprite.groupcollide(jack.jack_group,gems,True,False):
            #     xl+=2
        # gf.check_event()

        # gf.update_screen(screen,jack)

        elif xl==0:
            if end==True:
                pygame.mixer.music.load("music/end_music.wav")
                pygame.mixer.music.play(-1,0)
            end=False

            # pygame.mixer.music.stop()
            kai_shi.jieshu(screen)


        pygame.display.flip()
        
run_game()