import pygame
from pygame.locals import *
class Taskbar:
    def __init__(self, size , iconsize):
        self.size = size
        self.iconsize = iconsize
        self.blocks = []
        self.current_slot = 0
    def add_block(self, block):
        self.blocks.append(block)
    def draw(self, surface , x, y , textures):
        lenx = (self.iconsize +6)*self.size
        leny = self.iconsize+4
        pygame.gfxdraw.box(surface,(x, y, lenx, leny), (60,60,60))
        for i in range(self.size):
            if(i < len(self.blocks)):
                type = self.blocks[i]
                image = textures[type]
                iconimage = pygame.transform.scale(image, (self.iconsize, self.iconsize))
                surface.blit(iconimage, (x + i*(self.iconsize+2)+2, y + 2))
                iconx= x + i*(self.iconsize+2)+2
                icony= y + 2
                if(i == self.current_slot):
                    pygame.gfxdraw.rectangle(surface,(iconx-1, icony-1, self.iconsize, self.iconsize), (255,255,255))
               
            else:
                iconx= x + i*(self.iconsize+2)+2
                icony= y + 2
                if(i == self.current_slot):
                    pygame.gfxdraw.rectangle(surface,(iconx-1, icony-1, self.iconsize+4, self.iconsize+4), (255,255,255))

    def get_current_block(self):
        return self.blocks[self.current_slot]
    def next_block(self):
        self.current_slot += 1
        if self.current_slot >= len(self.blocks):
            self.current_slot = 0
    def previous_block(self):
        self.current_slot -= 1
        if self.current_slot < 0:
            self.current_slot = len(self.blocks) - 1