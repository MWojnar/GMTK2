from Entity import Entity
from PullOrbTether import PullOrbTether
import Utility
import pygame

class PullOrb(Entity):
    def __init__(self, world=None, x=0, y=0, sprite=None, depth=-2, player=None):
        super().__init__(world, x, y, depth=depth)
        if sprite == None:
            self.sprite = world.assetLoader.pullOrb
        else:
            self.sprite = sprite
        self.player = player
        self.range = 256
        self.circleMaskRadius = 32
        self.pullOrbTether = PullOrbTether(world, pullOrb=self, player=player, depth=depth-1)
        world.addEntity(self.pullOrbTether)
        
    def update(self):
        super().update()
        if self.withinRange() and self.mouseOver() and self.world.buttonState[0] and not self.player.isStable:
            self.player.pull((self.x, self.y))
            self.pullOrbTether.visible = True
            if not pygame.mixer.Channel(7).get_sound() == self.world.assetLoader.sndPullOrb:
                pygame.mixer.Channel(7).play(self.world.assetLoader.sndPullOrb)
                
        else:
            self.pullOrbTether.visible = False
            
    def withinRange(self):
        dist = Utility.getDistance((self.x, self.y), (self.player.x, self.player.y))
        return dist < self.range
    
    def mouseOver(self):
        dist = Utility.getDistance((self.x, self.y), self.world.mousePos)
        return dist < self.sprite.width