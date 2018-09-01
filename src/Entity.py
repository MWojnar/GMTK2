class Entity(object):
    def __init__(self, world=None, x=0, y=0, sprite=None, depth=0):
        self.frame = 0
        self.animationSpeedTimer = 0
        self.world = world
        self.sprite = sprite
        self.x = x
        self.y = y
        self.depth = depth
        self.rotation = 0
        self.animating = True
        
    def update(self):
        if self.animating:
            self.incrementFrame()
    
    def draw(self, surface):
        self.sprite.draw(surface, self.x, self.y, self.frame, self.rotation)
        
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