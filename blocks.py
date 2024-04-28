from enum import Enum
import pygame
from pygame.locals import *
class BlockType(Enum):
    GRASS = "grass.png"
    DIRT = "dirt.png"
    STONE = "stone.png"
    DIRTDARK = "dirtdark.png"
    STONEDARK = "stonedark.png"
    AIR = "air.png"
    SKY = "sky.png"
    PLAYER = "player.png"
    PLAYERCROUCH = "playercrouch.png"
    OAK= "oak.png"
    LEAVES = "leaves.png"
    SKIBIDI = "skibidi.png"
    COAL = "coal.png"
    IRON = "iron.png"
    GOLD = "gold.png"
    DIAMOND = "diamond.png"
    

    def replaceblock(Block_type):
        if(Block_type == BlockType.DIRT):
            return BlockType.DIRTDARK
        if(Block_type == BlockType.STONE):
            return BlockType.STONEDARK
        if(Block_type == BlockType.DIRTDARK):
            return BlockType.DIRTDARK
        if(Block_type == BlockType.STONEDARK):
            return BlockType.STONEDARK
        if(Block_type == BlockType.GRASS):
            return BlockType.DIRTDARK
        if(Block_type == BlockType.COAL):
            return BlockType.STONEDARK
        if(Block_type == BlockType.GOLD):
            return BlockType.STONEDARK
        if(Block_type == BlockType.IRON):
            return BlockType.STONEDARK
        if(Block_type == BlockType.DIAMOND):
            return BlockType.STONEDARK
        return BlockType.SKY

    def is_transparent(Block_type):
        if(Block_type == BlockType.LEAVES):
            return True
        if(Block_type == BlockType.SKIBIDI):
            return True
        return False
    def is_colideable(Block_type):
        if(Block_type == BlockType.LEAVES):
            return False
        if(Block_type == BlockType.SKIBIDI):
            return False
        if(Block_type == BlockType.STONEDARK):
            return False
        if(Block_type == BlockType.DIRTDARK):
            return False
        if(Block_type == BlockType.SKY):
            return False
        if(Block_type == BlockType.AIR):
            return False
        return True


class Block:
    def __init__(self, x, y, size, type ):
        self.x = x
        self.y = y
        self.size = size
        self.type = type
        self.transperent = False
        self.background = None
        self.lightlevel = 0
        self.is_colission = False
        
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_type(self):
        return self.type
    
    def get_lightlevel(self):
        return self.lightlevel
        
    def set_lightlevel(self, lightlevel):
        self.lightlevel = lightlevel
    def is_colision(self):
        return self.is_colission
    def set_collision(self, is_colission):
        self.is_colission = is_colission
    def set_transparent(self, value):
        self.transperent = value
    def is_transperent(self):
        return self.transperent
    def get_background(self):
        return self.background
    def set_background(self, background):
        self.background = background
    def draw(self , Surface , px, py , textures):
        mousex, mousey = pygame.mouse.get_pos()
        texture = textures[self.type]
        resizeimage = pygame.transform.scale(texture, (self.size, self.size))
        if(self.transperent):
            backgroundtexture = textures[self.background]
            resizeback = pygame.transform.scale(backgroundtexture, (self.size, self.size))
            Surface.blit(resizeback, (px, py))
        Surface.blit(resizeimage, (px, py))
        
        if mousex > px and mousex < px + self.size and mousey > py and mousey < py + self.size:
            pygame.gfxdraw.rectangle(Surface,(px, py, self.size, self.size), (255,255,255))
        
            
           
    def draw_minimap(self , Surface , px, py):
        pygame.gfxdraw.pixel(Surface, self.get_colors(), (px, py))
