import pygame
from pygame.locals import *
from physic import Physics
from blocks import BlockType, Block
class Player(Physics):
    def __init__(self, name , x ,y, speed , crouch_speed,height , width ):
        super().__init__(0.4,20)
        self.name = name
        self.hp = 100
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.crouched = False
        self.speed = speed
        self.crouch_speed = crouch_speed
        self.onGround = False
        self.jump = False
    
    def move(self, keys , world):
        oldy = self.y
        oldx = self.x
        speed = self.speed if not self.crouched else self.crouch_speed
        # Clear the screen
        if keys[K_SPACE or K_w]:
            if(self.onGround):
                jump = True
                self.velocity = -10 
                self.onGround = False
            
        if keys[K_a]:
            self.x -= 1*speed
            if(self.check_collision(self,world )):
                self.x = oldx
                self.y = oldy     
                
        if keys[K_d]:
            self.x += 1*speed
            if(self.check_collision(self,world )):
                self.x = oldx
                self.y = oldy 
        if keys[K_s]:
            self.crouch(True)
        else:
            self.crouch(False)
        self.apply_gravity(self)
        if(self.check_collision(self,world )):
            self.y = oldy 
            self.onGround=True 
            self.velocity = 0
    
    def crouch(self,is_croching):
        
        self.crouched = is_croching
                
    def get_collison_point(self):
        x_offset = 5
        y_offset = 5
        point1 = (self.x, self.y)
        point2 = (self.x+self.width-x_offset, self.y)
        point3 = (self.x, self.y-self.height+y_offset)
        point5 = (self.x, self.y-int(self.height/2))
        point4 = (self.x+self.width-x_offset, self.y-self.height+y_offset)
        point6 = (self.x+self.width-x_offset, self.y-int(self.height/2))
        return [point1, point2, point3, point4, point5, point6]            

    def get_pos(self):
        return (self.x, self.y)

    def draw(self, screen,x, y , textures):
        if(self.crouched):
            texture =  textures[BlockType.PLAYERCROUCH]
        else:
            texture =  textures[BlockType.PLAYER]
        resize = pygame.transform.scale(texture, (self.width, self.height))
        screen.blit(resize, (int(x/2), int(y/2)-self.height))