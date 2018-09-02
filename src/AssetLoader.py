import pygame
from Sprite import Sprite

class AssetLoader(object):
    def __init__(self, world):
        # Player sprites
        self.spaceguyStand = Sprite(world, pygame.image.load("images\\spr_spaceguy_stand.png"), 1)
        self.spaceguyJump = Sprite(world, pygame.image.load("images\\spr_spaceguy_jump.png"), 1)
        self.spaceguyFloat = Sprite(world, pygame.image.load("images\\spr_spaceguy_float.png"), 1)
        self.spaceguyCrouch = Sprite(world, pygame.image.load("images\\spr_spaceguy_crouch.png"), 1)
        self.spaceguyDie = Sprite(world, pygame.image.load("images\\spr_spaceguy_die_8frames.png"), 8)
        self.spaceguyDieHead = Sprite(world, pygame.image.load("images\\spr_spaceguy_die_head.png"), 1)
        self.spaceguyRespawn = Sprite(world, pygame.image.load("images\\spr_spaceguy_spawn_10frames.png"), 10)
        
        # Spike sprites
        self.smallSpikes = Sprite(world, pygame.image.load("images\\spr_small_spikes.png"), 1)
        self.mediumSpikes = Sprite(world, pygame.image.load("images\\spr_medium_spikes.png"), 1)
        self.bigSpikes = Sprite(world, pygame.image.load("images\\spr_big_spikes.png"), 1)
        
        # Pull Orb, Tether, Range sprites
        self.pullOrb = Sprite(world, pygame.image.load("images\\spr_attract_4frames.png"), 4)
        self.pullTether = Sprite(world, pygame.image.load("images\\spr_attract_tether_3frames.png"), 3)
        self.pullRange = Sprite(world, pygame.image.load("images\\spr_attract_range.png"), 1)
        
        # Background sprites
        self.bgEarth = Sprite(world, pygame.image.load("images\\bg_earth.png"), 1)  # FIXME: Implement
        self.bgSpace = pygame.image.load("images\\bg_space.png")
        
        # Platform sprites
        self.satellitePlatform = Sprite(world, pygame.image.load("images\\ts_satellite_platform.png"), 10, 0)
        
        # Bouncy sprites
        self.bouncy = Sprite(world, pygame.image.load("images\\spr_bouncy_5frames.png"), 5)
        
        # Checkpoint sprites
        self.checkpoint = Sprite(world, pygame.image.load("images\\spr_checkpoint_not_got.png"), 1)
        self.checkpointGet = Sprite(world, pygame.image.load("images\\spr_checkpoint_get_10frames.png"), 10)
        self.checkpointGot = Sprite(world, pygame.image.load("images\\spr_checkpoint_6frames.png"), 6)
        
        # Rocket sprites
        self.endRocket = Sprite(world, pygame.image.load("images\\spr_end_rocket.png"), 1)
        self.endRocketTakeoff = Sprite(world, pygame.image.load("images\\spr_end_rocket_exit_3frames.png"), 3)
        
        # Arrow sprites
        self.arrowSegment = Sprite(world, pygame.image.load("images\\spr_arrow_segment.png"), 1)
        self.arrowTip = Sprite(world, pygame.image.load("images\\spr_arrow_tip.png"), 1)
        
        # UI sprites
        self.mouse = pygame.image.load("images\\spr_mouse.png") # FIXME: Implement
        self.mouseCanClick = pygame.image.load("images\\spr_mouse_canclick.png") # FIXME: Implement
        
        self.start = pygame.image.load("images\\spr_start.png") # FIXME: Implement
        self.startSelected = pygame.image.load("images\\spr_start_selected.png") # FIXME: Implement
        
        self.quit = pygame.image.load("images\\spr_quit.png") # FIXME: Implement
        self.quitSelected = pygame.image.load("images\\spr_quit_selected.png") # FIXME: Implement
        
        self.title = pygame.image.load("images\\spr_title.png") # FIXME: Implement
        
        self.victory = pygame.image.load("images\\spr_victory.png") # FIXME: Implement
        
        # Main theme song
        self.sndMainTheme = pygame.mixer.music.load("sounds\\SpaceSong_Loop.mp3")
        
        # Sounds
        # Entity sounds
        self.sndDie = pygame.mixer.Sound("sounds\\snd_die.wav")
        self.sndJump = pygame.mixer.Sound("sounds\\snd_jump.wav")
        self.sndLand = pygame.mixer.Sound("sounds\\snd_land.wav")
        
        self.sndPullOrb = pygame.mixer.Sound("sounds\\snd_attract.wav")
        self.sndBouncy = pygame.mixer.Sound("sounds\\snd_bouncy.wav") # FIXME: Implement
        self.sndRepelOrb = pygame.mixer.Sound("sounds\\snd_repel.wav") # FIXME: Implement
        self.sndRocket = pygame.mixer.Sound("sounds\\snd_rocket.wav")
        
        # Menu sounds
        self.sndSelect = pygame.mixer.Sound("sounds\\snd_select.wav") # FIXME: Implement