import pygame,sys

def check_event(jack):
        #监视键盘与鼠标事件
    for event in pygame.event.get():
        #如果发生退出事件
        if event.type==pygame.QUIT:
            #系统退出
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                jack.rect.centerx+=1
            elif event.key==pygame.K_LEFT:
                jack.rect.centerx-=1
            elif event.key==pygame.K_UP:
                jack.rect.centery-=1
            elif event.key==pygame.K_DOWN:
                jack.rect.centery+=1

def uodate_screen(screen,jack):
    screen.fill((112,233,143))
    jack.blitme()
    pygame.display.flip()