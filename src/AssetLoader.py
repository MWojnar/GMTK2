import pygame
from Sprite import Sprite

class AssetLoader(object):
    def __init__(self, world):
        self.spaceguyStand = Sprite(world, pygame.image.load("spr_spaceguy_stand.png"), 1)
        self.spaceguyJump = Sprite(world, pygame.image.load("spr_spaceguy_jump.png"), 1)
        self.spaceguyFloat = Sprite(world, pygame.image.load("spr_spaceguy_float.png"), 1)
        self.spaceguyCrouch = Sprite(world, pygame.image.load("spr_spaceguy_crouch.png"), 1)
        
        self.mediumSpikes = Sprite(world, pygame.image.load("spr_medium_spikes1.png"), 1)
        self.bigSpikes = Sprite(world, pygame.image.load("spr_big_spikes1.png"), 1)
        
        self.pullOrb = Sprite(world, pygame.image.load("spr_attract_4frames.png"), 4)
        
        self.bgEarth = Sprite(world, pygame.image.load("bg_earth.png"), 1)
        
        self.satellitePlatform = Sprite(world, pygame.image.load("ts_satellite_platform.png"), 1)