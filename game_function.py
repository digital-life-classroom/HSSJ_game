import pygame,sys
class Game_function():
    def __init__(self,screen):
        self.screen=screen
    def check_event(self):
            #监视键盘与鼠标事件
        for event in pygame.event.get():
            #如果发生退出事件
            if event.type==pygame.QUIT:
                #系统退出
                sys.exit()

    def key_pressed(self,key_check):
        keys=pygame.key.get_pressed()
        if keys[key_check]==1:
            return True
        else:
            return False

    # def update_screen(self,screen,jack):
    #     jack.blitme()
    #     pygame.display.flip()