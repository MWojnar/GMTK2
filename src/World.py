import pygame
from Player import Player
from Sprite import Sprite

class World(object):
    clock = pygame.time.Clock()
    FPS = 60
    entityList = []
    running = True
    mainSurface = None
    camPos = [0, 0]

    def __init__(self, mainSurface):
        self.mainSurface = mainSurface
        player = Player(self, 100, 100)
        self.addEntity(player)

    def run(self):
        while self.running:
            self.update()
            self.render()
            
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        self.clock.tick(self.FPS)
        for entity in self.entityList:
            entity.update()
    
    def render(self):
        self.mainSurface.fill((255, 255, 255))
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