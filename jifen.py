import pygame
class JiFen():
    def __init__(self):
        self.jifen=0
        self.jiFen=pygame.font.SysFont("宋体",50)
        self.jiFenRender=self.jiFen.render("abc",False,(255,170,0))
        self.jiFenRect=self.jiFenRender.get_rect()
        self.jiFenRect.left=1100
        self.jiFenRect.top=10
    def blit_me(self,screen):
        screen.blit(self.jiFenRender,self.jiFenRect)
    def plus(self):
        self.jifen +=1
    def total(self):
        return self.jifen
