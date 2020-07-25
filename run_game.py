import pygame,sys
import random
from settings import Setting
from jack import Jack
import game_function as gf
from background import Background
from game_sprite import GameSprite
from jifen import JiFen
from kaishi import Kaishi

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
    
    next_frame=pygame.time.get_ticks()
    frame=0


    jifen=JiFen()
    
    kai_shi=Kaishi()
    kai_shi.kaishi(screen)

    begingame=False
    pygame.mixer.music.load("music/begin_music.wav")
    pygame.mixer.music.play(-1,0)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                #系统退出
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    begingame=True
                    background.blitme()

                    jack_group=pygame.sprite.OrderedUpdates()         #按添加顺序绘制sprite类
                    game_jack=GameSprite('image/jack_sprite.png',16)
                    game_jack.move(600,400)
                    jack_group.add(game_jack)
                    jack_group.draw(screen)
                    jifen.blit_me(screen)
                    spirit_group=pygame.sprite.OrderedUpdates()

                    game_spirit=GameSprite('image/spirit_sprite.png',16)
                    game_spirit.move(730,200)
                    spirit_group.add(game_spirit)
                    spirit_group.draw(screen)
                    jifen.blit_me(screen)

                    for i in range(3):
                        a=random.randint(0,1201)
                        b=random.randint(0,801)
                        game_spirit.move(a,b)
                        spirit_group.add(game_spirit)
                        spirit_group.draw(screen)
                        game_spirit.change_image(4)

                    pygame.mixer.music.load("music/music.wav")
                    pygame.mixer.music.play(-1,0)
        if begingame==True:          
            if pygame.time.get_ticks()>next_frame:
                frame=(frame+1)%4
                next_frame+=120
            if gf.key_pressed(pygame.K_RIGHT):
                game_jack.change_image(frame+8)
                background.move(-1,0)
                jack_group.draw(screen)
            elif gf.key_pressed(pygame.K_LEFT):
                game_jack.change_image(frame+4)
                background.move(1,0)
                jack_group.draw(screen)
            elif gf.key_pressed(pygame.K_UP):
                game_jack.change_image(frame+12)
                background.move(0,1)
                jack_group.draw(screen)
            elif gf.key_pressed(pygame.K_DOWN):
                game_jack.change_image(frame)
                background.move(0,-1)
                jack_group.draw(screen)
            
            jifen.blit_me(screen)
        # gf.check_event()

        #gf.update_screen(screen,jack)

        pygame.display.flip()
        
run_game()