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
from monster_nest import Monster_nest
import refresh as re

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
    
    kai_shi=Kaishi(screen)
    kai_shi.kaishi()

    begingame=False
    pygame.mixer.music.load("music/begin_music.wav")
    pygame.mixer.music.play(-1,0)

    spirits=Group()

    xl=6
    for i in range(5):
        x=random.randint(0,1201)
        y=random.randint(0,801)
        spirit=Spirit(screen,x,y)
        spirits.add(spirit)

    attack=Attack(screen)
    gems=Group()
    gem=Gem(screen)

    end=True
    win=True

    nests=Group()
    nest=Monster_nest(screen)
    nests.add(nest)
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

                    frame_spirit=pygame.time.get_ticks()
                    frame_treehole=pygame.time.get_ticks()
                    frame_treehole_spirit=pygame.time.get_ticks()
                    frame_koxie=pygame.time.get_ticks()
                    frame_gem=pygame.time.get_ticks()
                    frame_hyjq=pygame.time.get_ticks()
                    frame_fq=pygame.time.get_ticks()
        if begingame==True and xl>0 and jifen.jifen<5:
            jack.jack_move(background,spirits,gems,nests)
            jack.jack_attack(attack)

            jifen.blit_me(screen)

            ai_xin.js_xl(xl)

            frame_spirit=re.spirit_refresh(screen,spirits,frame_spirit)
            frame_gem=re.gem_refresh(screen,gems,frame_gem)
            nests.update()
            frame_treehole_spirit=re.treehole_spirit_refresh(screen,spirits,frame_treehole_spirit,nest.spirit_treehole_x,nest.spirit_treehole_y)

            for the_spirit in spirits:
                if pygame.sprite.spritecollideany(jack.game_jack,the_spirit.spirit_group):
                    if not jack.wd:
                        if pygame.time.get_ticks()>frame_koxie:
                            frame_koxie=pygame.time.get_ticks()
                            xl_2=xl
                            xl-=1
                            if xl_2>xl:
                                jack_ss=pygame.mixer.Sound("music/jack_ss.wav")
                                jack_ss.set_volume(1)                                             #调节音量
                                jack_ss.play(0)
                            ai_xin.js_xl(xl)   #pygame.sprite.groupcollide(jack.jack_group,spirit.spirit_group,True,True) //碰撞消失
                            frame_koxie+=3000

                if pygame.sprite.groupcollide(attack.hyjq_group,the_spirit.spirit_group,True,True):
                    jifen.plus()
                if pygame.time.get_ticks()>frame_hyjq:
                    attack.hyjq_group.add(attack.game_hyjq)
                    frame_hyjq+=10000

                if pygame.sprite.groupcollide(attack.fq_group,the_spirit.spirit_group,False,True):
                    jifen.plus()
                if pygame.time.get_ticks()>frame_fq:
                    attack.fq_group.add(attack.game_fq)
                    frame_fq+=10000
            for gem in gems:
                f=True if xl<=5 else False 
                if pygame.sprite.groupcollide(jack.jack_group,gem.gem_group_xlbs1,False,f) and xl<=5:
                    xl+=1
                elif pygame.sprite.groupcollide(jack.jack_group,gem.gem_group_xlbs2,False,f) and xl<=5:
                    xl=xl+1 if xl==5 else xl+2
        # gf.check_event()

        # gf.update_screen(screen,jack)

        elif xl==0:
            if end==True:
                pygame.mixer.music.load("music/end_music.wav")
                pygame.mixer.music.play(-1,0)
            end=False

            # pygame.mixer.music.stop()
            kai_shi.jieshu()
        elif jifen.jifen>=5:
            if win==True:
                pygame.mixer.music.load("music/win_music.wav")
                pygame.mixer.music.play(-1,0)
            win=False

            kai_shi.shengli()


        pygame.display.flip()
        
run_game()