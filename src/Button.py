from Entity import Entity

def emptyFunc():
    pass

class Button(Entity):
    def __init__(self, world=None, x=0, y=0, defaultSprite=None, hoverSprite=None, clickEvent=emptyFunc):
        super().__init__(world, x, y)
        self.sprite = defaultSprite
        self.defaultSprite = defaultSprite
        self.hoverSprite = hoverSprite
        self.lastButtonState = False
        self.clickEvent = clickEvent
        
    def update(self):
        super().update()
        if self.pointInImage(self.world.mousePos):
            self.sprite = self.hoverSprite
            if not self.world.buttonState[0] and self.lastButtonState:
                self.clickEvent()
        else:
            self.sprite = self.defaultSprite
        self.lastButtonState = self.world.buttonState[0]
        
    def pointInImage(self, pos):
        return (pos[0] > self.x - self.sprite.width / 2 and pos[0] < self.x + self.sprite.width / 2 and
            pos[1] > self.y - self.sprite.height / 2 and pos[1] < self.y + self.sprite.height / 2)