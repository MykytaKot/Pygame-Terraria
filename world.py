import numpy as np
from perlin_noise import PerlinNoise
import random
from blocks import Block, BlockType
import pygame

class World:
    def __init__(self, height , width , blocksize ):
        self.height = height
        self.width = width
        self.blocksize  = blocksize 
        self.world = []

    def generate_world(self):
    
        noise_generator = PerlinNoise(octaves=50, seed=random.randint(0, 1000))
        noise_generator2 = PerlinNoise(octaves=20, seed=random.randint(0, 1000))
        noise_generator3 = PerlinNoise(octaves=5, seed=random.randint(0, 1000))
        noise_generator4 = PerlinNoise(octaves=4, seed=random.randint(0, 1000))
        # Create an empty 2D NumPy array to store the Perlin noise values
        noise_generator5 = PerlinNoise(octaves=80, seed=random.randint(0, 1000))
        noise_generator6 = PerlinNoise(octaves=80, seed=random.randint(0, 1000))
        world = np.empty((self.height, self.width), dtype=object)

        # Example generation using random colors (replace with your logic)
        for y in range(self.height):
            for x in range(self.width):
                perlin = noise_generator([x / self.width, y / self.height])
                
                if(y < 230):
                    
                    if(perlin> 0.3):
                        world[y, x] = Block(x * self.blocksize , y * self.blocksize , self.blocksize , BlockType.AIR)
                    else:
                        world[y, x] = Block(x * self.blocksize , y * self.blocksize , self.blocksize , BlockType.SKY)
                elif(y >= 230 and y < 280):
                        world[y, x] = Block(x * self.blocksize , y * self.blocksize , self.blocksize , BlockType.SKY)
                else:
                    perlin45 = noise_generator4([x / self.width, y / self.height])
                    perlin5 = noise_generator5([x / self.width, y / self.height])
                    perlin = noise_generator([x / self.width, y / self.height])
                    perlin2 = noise_generator2([x / self.width, y / self.height])
                    perlin3 = noise_generator3([x / self.width, y / self.height])
                    if(perlin2*7+perlin*5+perlin3*8 + perlin45*7 +perlin5*7 < 0.8):
                        world[y, x] = Block(x * self.blocksize , y * self.blocksize , self.blocksize , BlockType.STONE)
                        world[y, x].set_collision(True)    
                    else:
                        world[y, x] = Block(x * self.blocksize , y * self.blocksize , self.blocksize , BlockType.STONEDARK)
            if(y % 10 == 0):
                print("generating" + str(y) + " of " + str(self.height) + " rows")
        x , y = 0, 0
        
        print("second stage")
        for x in range(self.width):
            perlin45 = noise_generator4([x / self.width, y / self.height])
            perlin5 = noise_generator5([x / self.width, y / self.height])
            perlin = noise_generator([x / self.width, y / self.height])
            perlin2 = noise_generator2([x / self.width, y / self.height])
            perlin3 = noise_generator3([x / self.width, y / self.height])
            
            stone = random.randint(0, 4)
            grass = 1
            
            height =  min(max(int(abs(perlin45*1.5+perlin5*0.9+perlin*0.4+perlin2*1.2+perlin3*0.8)*60) ,6),50)

            for y in range(280,231,-1):
                perlin = noise_generator([x / self.width, y / self.height])
                perlin2 = noise_generator2([x / self.width, y / self.height])
                perlin3 = noise_generator3([x / self.width, y / self.height])
                perlin45 = noise_generator4([x / self.width, y / self.height])
                perlin5 = noise_generator5([x / self.width, y / self.height])
            
                dirt =  height - grass - stone
                if(height != 0):
                    if(stone != 0):
                        if(perlin2*7+perlin*5+perlin3*8 + perlin45*7 +perlin5*7 < 0.8):
                            world[y, x] = Block(x * self.blocksize , y * self.blocksize , self.blocksize , BlockType.STONE)
                            world[y, x].set_collision(True) 
                        else:
                            world[y, x] = Block(x * self.blocksize , y * self.blocksize , self.blocksize , BlockType.STONEDARK)
                        stone -= 1
                    elif(dirt != 0):
                        if(perlin2*7+perlin*5+perlin3*8 + perlin45*7 +perlin5*7 < 0.8):
                            world[y, x] = Block(x * self.blocksize , y * self.blocksize , self.blocksize , BlockType.DIRT)
                            world[y, x].set_collision(True) 
                        else:
                            world[y, x] = Block(x * self.blocksize , y * self.blocksize , self.blocksize , BlockType.DIRTDARK)
                        dirt -= 1
                    else:
                        world[y, x] = Block(x * self.blocksize , y * self.blocksize , self.blocksize , BlockType.GRASS)
                        world[y, x].set_collision(True) 
                        grass -= 1
                    height -= 1    
                else:
                    continue     

        print("third stage")
        self.world = world
        x , y = 0, 0
        for x in range(20 ,self.width-20):
            for y in range(280,231,-1):
                if(world[y, x].get_type() == BlockType.GRASS):
                    if(random.randint(0, 100) < 60):
                        is_free = True
                        for i in range(5):
                            for u in range(5):
                                if(world[y-i-1, x+u-2].is_colision()):
                                    is_free = False

                        if(is_free):
                            self.put_tree(x,y-1)
        x , y = 0, 0        
        print("fourth stage")
        for x in range(self.width):
            for y in range(300,self.height):    
                perlin5 = noise_generator5([x / self.width, y / self.height])
                perlin = noise_generator6([x / self.width, y / self.height])
                if(self.world[y, x].get_type() == BlockType.STONE):
                    if(abs(perlin5)*10 < 0.1):
                        self.world[y, x] = Block(x * self.blocksize , y * self.blocksize , self.blocksize , BlockType.COAL)
                        self.world[y, x].set_collision(True)
                    if(abs(perlin)*10 < 0.05):
                        self.world[y, x] = Block(x * self.blocksize , y * self.blocksize , self.blocksize , BlockType.IRON)
                        self.world[y, x].set_collision(True)
                    if(abs(perlin)*10 < 0.01 and y >400):
                        self.world[y, x] = Block(x * self.blocksize , y * self.blocksize , self.blocksize , BlockType.GOLD)
                        self.world[y, x].set_collision(True)
                    if(abs(perlin)*10 < 0.005 and y >450):
                        self.world[y, x] = Block(x * self.blocksize , y * self.blocksize , self.blocksize , BlockType.DIAMOND)
                        self.world[y, x].set_collision(True)

        print("world generated")
        

    def get_blocksize(self):
        return self.blocksize
    def get_block(self, x , y):
        return self.world[y, x]
    
    def put_tree(self,x,y):
        for o in range(3):
            for u in range(5):
                prevblock = self.get_block(x+(u-2), y-2-o)
                if(prevblock.is_transperent()):
                    prevblock = prevblock.get_background()
                else:
                    prevblock = prevblock.get_type()
                block = Block((x+(u-2)) * self.blocksize , (y-2-o) * self.blocksize , self.blocksize , BlockType.LEAVES)
                block.set_transparent(True)
                block.set_background(prevblock)
                self.set_block(x+(u-2), y-2-o,block,False)

        for i in range(5):
            self.set_block(x, y-i, Block(x * self.blocksize , y * self.blocksize , self.blocksize , BlockType.OAK),True)
        for r in range(3):
            prevblock = self.get_block(x+(r-1), y-5)
            if(prevblock.is_transperent()):
                prevblock = prevblock.get_background()
            else:
                prevblock = prevblock.get_type()
            block = Block(x+(r-1) * self.blocksize , y * self.blocksize , self.blocksize , BlockType.LEAVES)
            block.set_transparent(True)
            block.set_background(prevblock)
            self.set_block(x+(r-1), y-5,block,False)

    def set_block(self, x , y , block , collision):
        self.world[y, x] = block
        self.world[y, x].set_collision(collision)

    def render_world(self, surface , playerx, playery , textures ):
    
        world_height, world_width = self.world.shape

        # Render visible blocks only (optimize for larger worlds)
        half_width = int((surface.get_width() / self.blocksize) /2)+10
        half_height = int((surface.get_height() / self.blocksize) /2)+10

        placeinworldx =  int(playerx/self.blocksize)
        placeinworldy =  int(playery/self.blocksize)
        
        for y in range(placeinworldy - half_height, placeinworldy + half_height):
            for x in range(placeinworldx - half_width, placeinworldx + half_width):
                if 0 <= y < world_height and 0 <= x < world_width:
                    block = self.world[y, x]
                    posx = x * self.blocksize - playerx + surface.get_width()/2
                    posy = y * self.blocksize - playery + surface.get_height()/2
                    # Draw the block at its calculated position
                    block.draw(surface, posx, posy,textures)
        

    