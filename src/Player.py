'''
Created on Aug 31, 2018

@author: Seanzee
'''
import pygame
import math
import Utility
from Entity import Entity

class Player(Entity):
    def __init__(self, world=None, x=0, y=0, sprite=None, depth=0):
        # Can't set the sprite as a default value, as I need before
        # I can access assetLoader
        super().__init__(world, x, y, depth=depth)
        if sprite == None:
            self.sprite = world.assetLoader.spaceguyStand
        else:
            self.sprite = sprite
        self.animationSpeedTimer = 0
        self. frame = 0
        self.world = world
        self.x = x
        self.y = y
        self.depth = depth
        self.isStable = True
        self.stableRotation = 0
        self.angleLimit = 60
        self.maxPower = 10
        self.power = 1
        self.crouching = False
        self.hSpeed = 0
        self.vSpeed = 0
        self.jumpTimer = 0
        self.jumpTimerMax = 10
        
    def update(self):
        super().update()
        dist = Utility.getDistance((self.x, self.y), self.world.mousePos)
        self.power = dist // 25 + 1
        if self.power < 1:
            self.power = 1
        if self.power > self.maxPower:
            self.power = self.maxPower
        if self.isStable:
            self.rotation = math.degrees(math.atan2(self.world.mousePos[0] - self.x, self.world.mousePos[1] - self.y))
            self.rotation = Utility.getRelativeRotation(self.stableRotation, self.rotation)
            if self.rotation > self.stableRotation + self.angleLimit:
                self.rotation = self.stableRotation + self.angleLimit
            if self.rotation < self.stableRotation - self.angleLimit:
                self.rotation = self.stableRotation - self.angleLimit
            if self.world.buttonState[0]:
                self.sprite = self.world.assetLoader.spaceguyCrouch
                self.crouching = True
            else:
                if self.crouching:
                    self.crouching = False
                    self.isStable = False
                    self.sprite = self.world.assetLoader.spaceguyJump
                    self.hSpeed = Utility.lengthDirXDegrees(self.power / 2, self.rotation + 90)
                    self.vSpeed = Utility.lengthDirYDegrees(self.power / 2, self.rotation + 90)
                    self.jumpTimer = self.jumpTimerMax
                else:
                    self.sprite = self.world.assetLoader.spaceguyStand
        else:
            self.jumpTimer -= 1
            if self.jumpTimer < 0:
                self.jumpTimer = 0
                self.sprite = self.world.assetLoader.spaceguyFloat
        self.move()
        
    def move(self):
        self.x += self.hSpeed
        self.y += self.vSpeed
        
    def draw(self, surface):
        self.sprite.draw(surface, self.x, self.y, self.frame, self.rotation)
        if self.isStable and self.world.buttonState[0]:
            self.drawArrow(surface)
            
    def drawArrow(self, surface):
        arrowSeg = self.world.assetLoader.arrowSegment
        arrowTip = self.world.assetLoader.arrowTip
        segLen = arrowSeg.width / 2 - 1
        for i in range(int(self.power)):
            x = self.x + Utility.lengthDirXDegrees(i * segLen + segLen / 2 + self.sprite.height / 4, self.rotation + 90)
            y = self.y + Utility.lengthDirYDegrees(i * segLen + segLen / 2 + self.sprite.height / 4, self.rotation + 90)
            arrowSeg.draw(surface, x, y, 0, self.rotation + 90)
        x = self.x + Utility.lengthDirXDegrees(self.power * segLen + segLen / 2 + self.sprite.height / 4, self.rotation + 90)
        y = self.y + Utility.lengthDirYDegrees(self.power * segLen + segLen / 2 + self.sprite.height / 4, self.rotation + 90)
        arrowTip.draw(surface, x, y, 0, self.rotation)