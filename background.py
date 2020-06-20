import pygame

class Background():
    def __init__(self,screen):
        self.posX=0
        self.posY=0
        self.theInmage=pygame.image.load('image/background.png')
        self.imageWidth=self.theInmage.get_width()
        self.imageHeight=self.theInmage.get_height()
        self.screen=screen
    def blitme(self):
        self.screen.blit(self.theInmage,(0,0))
    def move(self,x,y):
        self.posX+=x
        self.posY+=y
        self.screen.blit(self.theInmage,(0-(-self.posX)%self.imageWidth,0-(-self.posY)%self.imageHeight))
        self.screen.blit(self.theInmage,(self.imageWidth-(-self.posX)%self.imageWidth,0-(-self.posY)%self.imageHeight))
        self.screen.blit(self.theInmage,(0-(-self.posX)%self.imageWidth,self.imageHeight-(-self.posY)%self.imageHeight))
        self.screen.blit(self.theInmage,(self.imageWidth-(-self.posX)%self.imageWidth,self.imageHeight-(-self.posY)%self.imageHeight))
