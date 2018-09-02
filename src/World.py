import pygame
from Player import Player
from AssetLoader import AssetLoader
from PullOrb import PullOrb
from Platform import Platform
from Background import Background

class World(object):
    clock = pygame.time.Clock()
    FPS = 60
    entityList = []
    running = True
    mainSurface = None
    camPos = [0, 0]
    

    def __init__(self, mainSurface):
        self.assetLoader = AssetLoader(self)
        self.mainSurface = mainSurface
        self.background = Background()
        player = Player(self, 200, 300)
        self.addEntity(player)
        pullOrb = PullOrb(self, 250, 150, depth=-1, player=player)
        self.addEntity(pullOrb)
        platform = Platform(self, 200, 325, depth=-1, player=player)
        platform.frame = 1
        self.addEntity(platform)
        platform = Platform(self, 300, 225, depth=-1, player=player)
        platform.frame = 6
        self.addEntity(platform)
        platform = Platform(self, 300, 225 - 16, depth=-1, player=player)
        platform.frame = 6
        self.addEntity(platform)
        platform = Platform(self, 300, 225 - 32, depth=-1, player=player)
        platform.frame = 6
        self.addEntity(platform)
        platform = Platform(self, 300, 225 - 48, depth=-1, player=player)
        platform.frame = 6
        self.addEntity(platform)

    def run(self):
        while self.running:
            self.update()
            self.render()
            
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        self.clock.tick(self.FPS)
        self.buttonState = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        self.mousePos = (pos[0] + self.camPos[0], pos[1] + self.camPos[1])
        for entity in self.entityList:
            entity.update()
    
    def render(self):
        self.mainSurface.fill((255, 255, 255))
        self.background.draw(self.mainSurface, self.assetLoader.bgSpace)
        for entity in self.entityList:
            entity.draw(self.mainSurface)
        pygame.display.flip()
        
            
    def addEntity(self, entity):
        found = False
        for i in range(len(self.entityList)):
            if entity.depth <= self.entityList[i].depth:
                self.entityList.insert(i, entity)
                found = True
                break
        if not found:
            self.entityList.append(entity)
            
    def removeEntity(self, entity):
        try:
            self.entityList.remove(entity)
        except:
            print("Error, trying to remove entity that does not exist!")