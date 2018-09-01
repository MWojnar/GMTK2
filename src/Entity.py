class Entity(object):
    sprite = None
    animationSpeedTimer = 0
    frame = 0
    world = None
    x = 0
    y = 0
    depth = 0

    def __init__(self, world=None, sprite=None, x=0, y=0, depth=0):
        self.world = world
        self.sprite = sprite
        self.x = x
        self.y = y
        self.depth = depth
        
    def update(self):
        self.incrementFrame()
    
    def draw(self, surface):
        self.sprite.draw(surface, self.x, self.y, self.frame)
        
    def incrementFrame(self):
        if self.sprite != None and self.sprite.animationSpeed != 0:
            self.animationSpeedTimer += self.sprite.animationSpeed / self.world.FPS
            if self.animationSpeedTimer >= 1:
                self.frame += 1
                self.animationSpeedTimer = 0
            if self.frame >= self.sprite.frameCount:
                self.frame = 0
                self.animationEnd()
    
    def animationEnd(self):
        pass