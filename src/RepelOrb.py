from Entity import Entity
from RepelOrbTether import RepelOrbTether
import Utility
import pygame

class RepelOrb(Entity):
    def __init__(self, world=None, x=0, y=0, sprite=None, depth=-2, player=None):
        super().__init__(world, x, y, depth=depth)
        if sprite == None:
            self.sprite = world.assetLoader.repelOrb
        else:
            self.sprite = sprite
        self.player = player
        self.range = 256
        self.circleMaskRadius = 32
        self.repelOrbTether = RepelOrbTether(world, repelOrb=self, player=player, depth=depth-1)
        world.addEntity(self.repelOrbTether)
        
    def update(self):
        super().update()
        if self.withinRange() and self.mouseOver() and self.world.buttonState[0] and not self.player.isStable:
            self.player.push((self.x, self.y))
            self.repelOrbTether.visible = True
            
            if not pygame.mixer.Channel(7).get_sound() == self.world.assetLoader.sndRepelOrb:
                pygame.mixer.Channel(7).play(self.world.assetLoader.sndRepelOrb)
                

        else:
            self.repelOrbTether.visible = False
            
    def withinRange(self):
        dist = Utility.getDistance((self.x, self.y), (self.player.x, self.player.y))
        return dist < self.range
    
    def mouseOver(self):
        dist = Utility.getDistance((self.x, self.y), self.world.mousePos)
        return dist < self.sprite.width