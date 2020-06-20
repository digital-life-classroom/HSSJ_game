import pygame,sys

def check_event(jack,background):
        #监视键盘与鼠标事件
    for event in pygame.event.get():
        #如果发生退出事件
        if event.type==pygame.QUIT:
            #系统退出
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                background.move(-5,0)
            elif event.key==pygame.K_LEFT:
                background.move(5,0)
            elif event.key==pygame.K_UP:
                background.move(0,5)
            elif event.key==pygame.K_DOWN:
                background.move(0,-5)

def update_screen(screen,jack):
    jack.blitme()
    pygame.display.flip()