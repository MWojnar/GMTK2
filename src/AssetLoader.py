import pygame
from Sprite import Sprite

class AssetLoader(object):
    def __init__(self, world):
        self.spaceguyStand = Sprite(world, pygame.image.load("spr_spaceguy_stand.png"), 1)
        self.spaceguyJump = Sprite(world, pygame.image.load("spr_spaceguy_jump.png"), 1)
        self.spaceguyFloat = Sprite(world, pygame.image.load("spr_spaceguy_float.png"), 1)
        self.spaceguyCrouch = Sprite(world, pygame.image.load("spr_spaceguy_crouch.png"), 1)
        self.spaceguyDie = Sprite(world, pygame.image.load("spr_spaceguy_die_8frames.png"), 8)
        
        self.smallSpikes = Sprite(world, pygame.image.load("spr_small_spikes.png"), 1)
        self.mediumSpikes = Sprite(world, pygame.image.load("spr_medium_spikes.png"), 1)
        self.bigSpikes = Sprite(world, pygame.image.load("spr_big_spikes.png"), 1)
        
        self.pullOrb = Sprite(world, pygame.image.load("spr_attract_4frames.png"), 4)
        self.pullTether = Sprite(world, pygame.image.load("spr_attract_tether_3frames.png"), 3)
        
        self.bgEarth = Sprite(world, pygame.image.load("bg_earth.png"), 1)
        
        self.satellitePlatform = Sprite(world, pygame.image.load("ts_satellite_platform.png"), 1)
        
        self.arrowSegment = Sprite(world, pygame.image.load("spr_arrow_segment.png"), 1)
        self.arrowTip = Sprite(world, pygame.image.load("spr_arrow_tip.png"), 1)