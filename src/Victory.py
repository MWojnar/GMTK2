from Entity import Entity

class Victory(Entity):
    def __init__(self, world=None, x=0, y=0, sprite=None, depth=0):
        super().__init__(world, x, y, depth)
        if sprite == None:
            self.sprite = self.world.assetLoader.victory
        else:
            self.sprite = sprite
        self.lastButtonState = False
            
    def update(self):
        super().update()
        if not self.world.buttonState[0] and self.lastButtonState:
            self.world.loadMenu()
        self.lastButtonState = self.world.buttonState[0]