import pygame,sys

def check_event(background):
        #监视键盘与鼠标事件
    for event in pygame.event.get():
        #如果发生退出事件
        if event.type==pygame.QUIT:
            #系统退出
            sys.exit()
    if key_pressed(pygame.K_RIGHT):
        background.move(-1,0)
    elif key_pressed(pygame.K_LEFT):
        background.move(1,0)
    elif key_pressed(pygame.K_UP):
        background.move(0,1)
    elif key_pressed(pygame.K_DOWN):
        background.move(0,-1)

def key_pressed(key_check):
    keys=pygame.key.get_pressed()
    if keys[key_check]==1:
        return True
    else:
        return False

def update_screen(screen,jack):
    jack.blitme()
    pygame.display.flip()