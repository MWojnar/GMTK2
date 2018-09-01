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
        
        
    def update(self):
        super().update()
        buttonState = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        truePos = (pos[0] + self.world.camPos[0], pos[1] + self.world.camPos[1])
        dist = Utility.getDistance((self.x, self.y), truePos)
        if self.isStable:
            self.rotation = math.degrees(math.atan2(truePos[0] - self.x, truePos[1] - self.y))
            self.rotation = Utility.getRelativeRotation(self.stableRotation, self.rotation)
            if self.rotation > self.stableRotation + self.angleLimit:
                self.rotation = self.stableRotation + self.angleLimit
            if self.rotation < self.stableRotation - self.angleLimit:
                self.rotation = self.stableRotation - self.angleLimit
            if buttonState[0]:
                self.sprite = self.world.assetLoader.spaceguyCrouch
            else:
                self.sprite = self.world.assetLoader.spaceguyStand
        
    def draw(self, surface):
        self.sprite.draw(surface, self.x, self.y, self.frame, self.rotation)