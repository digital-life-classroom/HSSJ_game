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

    next_frame=0

    xl=6
    for i in range(5):
        spirit=Spirit(screen)
        spirits.add(spirit)

    attack=Attack(screen)

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

                    next_frame=pygame.time.get_ticks()
                    next_frame_2=pygame.time.get_ticks()
        if begingame==True and xl>0:
            jack.jack_move(background,spirits)
            jack.jack_attack(attack)

            jifen.blit_me(screen)

            ai_xin.js_xl(xl)

            if pygame.time.get_ticks()>next_frame:
                spirit=Spirit(screen)
                spirits.add(spirit)
                next_frame+=20000
            spirits.update()

            for the_spirit in spirits:
                if pygame.sprite.spritecollideany(jack.game_jack,the_spirit.spirit_group):
                    if not jack.wd:
                        if pygame.time.get_ticks()>next_frame_2:
                            next_frame_2=pygame.time.get_ticks()
                            xl-=1
                            ai_xin.js_xl(xl)   #pygame.spite.groupcollide(jack.jack_group,spirit.spirit_group,True,True) //碰撞消失
                            #音乐
                            next_frame_2+=3000

        # gf.check_event()

        # gf.update_screen(screen,jack)

        else:
            #音乐，图片
            # pygame.mixer.music.stop()
            kai_shi.jieshu(screen)


        pygame.display.flip()
        
run_game()