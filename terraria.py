import pygame 
import random
import math
import numpy as np
from perlin_noise import PerlinNoise
from pygame.locals import *
import pygame.gfxdraw
from blocks import BlockType, Block
from taskbar import Taskbar
from world import World
from playerController import Player

DisplayH = 720
DisplayW = 1280

speed = 5
crouch_speed = 1

worldh = 500
worldw = 2000

blocksize = 40




current_block = None


        





    

def load_textures():
    textures = {}
    for block_type in BlockType:
        texture = pygame.image.load(f"./textures/{block_type.name.lower()}.png")
        textures[block_type] = texture
    return textures
    



def main():
   
    
    playerx = (worldw*blocksize)/2
    playery = (worldh*blocksize)/2
    

    textures = load_textures()

    world = World(worldh, worldw, blocksize)
    world.generate_world()


    player = Player("player", playerx, playery, speed, crouch_speed,60,40)
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((DisplayW, DisplayH))
    pygame.display.set_caption("Pyraria")
    taskbar = Taskbar(15, 40)
    clock = pygame.time.Clock()
    taskbar.add_block(BlockType.STONE)
    taskbar.add_block(BlockType.DIRT)
    taskbar.add_block(BlockType.GRASS)
    taskbar.add_block(BlockType.AIR)
    taskbar.add_block(BlockType.DIRTDARK)
    taskbar.add_block(BlockType.STONEDARK)
    taskbar.add_block(BlockType.LEAVES)
    taskbar.add_block(BlockType.SKIBIDI)
    taskbar.add_block(BlockType.OAK)
    taskbar.add_block(BlockType.COAL)
    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEWHEEL:
                if event.y > 0:  # Scroll up
                    taskbar.next_block()
                    pass
                elif event.y < 0:  # Scroll down
                    taskbar.previous_block()
                    pass
        if pygame.mouse.get_pressed()[0]:
            if(BlockType.is_transparent(taskbar.get_current_block())):
                putting_on = world.get_block(current_block[0], current_block[1])
                if(putting_on.is_transperent()):
                    putting_on = putting_on.get_background()
                else:
                    putting_on = putting_on.get_type()

                
                
                block = Block(current_block[0] * blocksize , current_block[1] * blocksize , blocksize ,taskbar.get_current_block())

                block.set_transparent(True)
                block.set_background(putting_on)
                world.set_block(current_block[0], current_block[1],block, BlockType.is_colideable(taskbar.get_current_block()))
            else:
                block = Block(current_block[0] * blocksize , current_block[1] * blocksize , blocksize , taskbar.get_current_block())
                world.set_block(current_block[0], current_block[1],block, BlockType.is_colideable(taskbar.get_current_block()))
            

        if pygame.mouse.get_pressed()[2]:
            BlockC = world.get_block(current_block[0], current_block[1])
            if(BlockC.is_transperent()):
                Btype = BlockC.get_background()
            else:
                Btype = BlockC.get_type()
            ChangeType = BlockType.replaceblock(Btype)  
            world.set_block(current_block[0], current_block[1],Block(current_block[0] , current_block[1], blocksize, ChangeType), BlockType.is_colideable(ChangeType))
           
        keys = pygame.key.get_pressed()
        
        player.move(keys, world)
        player_pos = player.get_pos()
        mousex, mousey = pygame.mouse.get_pos()
        blockx = int((player_pos[0] + mousex - DisplayW/2) / blocksize)
        blocky = int((player_pos[1] + mousey - DisplayH/2) / blocksize)
        
        current_block =[blockx, blocky]
        player.draw(screen, DisplayW, DisplayH ,textures)
        # # Render the world with potential camera offsets (replace with your logic)
        
        
        world.render_world(screen , player_pos[0], player_pos[1], textures)
        taskbar.draw(screen, 10, 10, textures)
        player.draw(screen, DisplayW, DisplayH ,textures)
        # Update the display
        pygame.display.flip()

        # Set frame rate
        clock.tick(60)  # Target 60 FPS

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()