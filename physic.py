
class Physics:
    def __init__(self, gravity , speed_limit):
        self.gravity = gravity
        self.velocity = 0
        self.speed_limit = speed_limit
    def apply_gravity(self, player):
        player.y += self.velocity
        if(self.velocity > self.speed_limit):
            self.velocity = self.speed_limit
        else:
            self.velocity += self.gravity
    def check_collision(self , player , world):
        points = player.get_collison_point()
        blocksize = world.get_blocksize()
        for point in points:
            placeinworldx =  int(point[0]/blocksize)
            placeinworldy =  int(point[1]/blocksize)
            
            block = world.get_block(placeinworldx, placeinworldy)
            if( block.is_colision()):
                return True
        return False