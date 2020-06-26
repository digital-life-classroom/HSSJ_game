import pygame
class GameSprite(pygame.sprite.Sprite):
    def __init__ (self,filename,frames=1):
        pygame.sprite.Sprite.__init__(self)        #基类的init用法
        self.images=[]
        img=pygame.image.load(filename)
        self.original_width=img.get_width()//frames
        self.original_height=img.get_height()
        frame_surface=pygame.Surface([self.original_width,self.original_height])
        x=0
        for frame_no in range(frames):
            frame_surface=pygame.Surface([self.original_width,self.original_height])
            frame_surface.blit(img,[x,0])
            self.images.append(frame_surface.copy())
            x-=self.original_width
        self.image=self.images[0]
        self.current_index=0
        self.rect=self.image.get_rect()
    def move(self,pos_X,pos_Y):
        self.rect.center=[pos_X,pos_Y]
    def change_image(self,index):
        self.current_index=index
        self.image=self.images[index]
        oldcenter=self.rect.center
        self.rect=self.image.get_rect()
        original_rect=self.images[self.current_index].get_rect()
        self.original_width=original_rect.width
        self.original_height=original_rect.height
        self.rect.center=oldcenter
        