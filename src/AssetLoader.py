import pygame
from Sprite import Sprite

class AssetLoader(object):
    def __init__(self, world):
        self.spaceguyStand = Sprite(world, pygame.image.load("images\\spr_spaceguy_stand.png"), 1)
        self.spaceguyJump = Sprite(world, pygame.image.load("images\\spr_spaceguy_jump.png"), 1)
        self.spaceguyFloat = Sprite(world, pygame.image.load("images\\spr_spaceguy_float.png"), 1)
        self.spaceguyCrouch = Sprite(world, pygame.image.load("images\\spr_spaceguy_crouch.png"), 1)
        self.spaceguyDie = Sprite(world, pygame.image.load("images\\spr_spaceguy_die_8frames.png"), 8)
        self.spaceguyDieHead = Sprite(world, pygame.image.load("images\\spr_spaceguy_die_head.png"), 1)
        
        self.smallSpikes = Sprite(world, pygame.image.load("images\\spr_small_spikes.png"), 1)
        self.mediumSpikes = Sprite(world, pygame.image.load("images\\spr_medium_spikes.png"), 1)
        self.bigSpikes = Sprite(world, pygame.image.load("images\\spr_big_spikes.png"), 1)
        
        self.pullOrb = Sprite(world, pygame.image.load("images\\spr_attract_4frames.png"), 4)
        self.pullTether = Sprite(world, pygame.image.load("images\\spr_attract_tether_3frames.png"), 3)
        self.pullRange = Sprite(world, pygame.image.load("images\\spr_attract_range.png"), 1)
        
        self.bgEarth = Sprite(world, pygame.image.load("images\\bg_earth.png"), 1)
        self.bgSpace = pygame.image.load("images\\bg_space.png")
        
        self.satellitePlatform = Sprite(world, pygame.image.load("images\\ts_satellite_platform.png"), 10, 0)
        
        self.bouncy = Sprite(world, pygame.image.load("images\\spr_bouncy_5frames.png"), 5)
        
        self.checkpoint = Sprite(world, pygame.image.load("images\\spr_checkpoint_not_got.png"), 1)
        self.checkpointGet = Sprite(world, pygame.image.load("images\\spr_checkpoint_get_10frames.png"), 10)
        self.checkpointGot = Sprite(world, pygame.image.load("images\\spr_checkpoint_6frames.png"), 1)
        
        self.endRocket = Sprite(world, pygame.image.load("images\\spr_end_rocket.png"), 1)
        self.endRocketTakeoff = Sprite(world, pygame.image.load("images\\spr_end_rocket_exit_3frames.png"), 3)
        
        self.arrowSegment = Sprite(world, pygame.image.load("images\\spr_arrow_segment.png"), 1)
        self.arrowTip = Sprite(world, pygame.image.load("images\\spr_arrow_tip.png"), 1)