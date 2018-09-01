'''
Created on Aug 31, 2018

@author: Seanzee
'''
import pygame
import math
from Entity import Entity
from Sprite import Sprite

class Player(Entity):
    def __init__(self, world=None, x=0, y=0, sprite=None, depth=0):
        self.sprite = Sprite(world, pygame.image.load("spr_spaceguy.png"), 1)
        self.frame = 0
        self.animationSpeedTimer = 0
        self.world = world
        self.x = x
        self.y = y
        self.depth = depth
        self.rotation = 0
        
    def update(self):
        super().update()
        buttonState = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        truePos = (pos[0] + self.world.camPos[0], pos[1] + self.world.camPos[1])
        if buttonState[0]:
            self.rotation = math.degrees(math.atan2(truePos[0] - self.x, truePos[1] - self.y))
        
    def draw(self, surface):
        self.sprite.draw(surface, self.x, self.y, self.frame, self.rotation)