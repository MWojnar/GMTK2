from Entity import Entity

class Rocket(Entity):
        def __init__(self, world=None, x=0, y=0, sprite=None, depth=0):
            super().__init__(world, x, y, depth=depth)
            if sprite == None:
                self.sprite = world.assetLoader.endRocket
            else:
                self.sprite = sprite
            self.animationSpeedTimer = 0
            self.frame = 0