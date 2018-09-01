'''
Created on Aug 31, 2018

@author: Seanzee
'''
import pygame
from Entity import Entity
from Sprite import Sprite

class Player(Entity):
    def __init__(self, world=None, x=0, y=0, sprite=None, depth=0):
        self.sprite = Sprite(world, pygame.image.load("spr_spaceguy.png"), 1)
        self.frame = 0
        self.world = None
        self.animationSpeedTimer = 0
        self.world = world
        self.x = x
        self.y = y
        self.depth = depth