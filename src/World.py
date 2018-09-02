import pygame
<<<<<<< HEAD
=======
import os.path
from Player import Player
>>>>>>> d84fd5fc55f2ef21040272f86b4574c5274e8dbb
from AssetLoader import AssetLoader
from Background import Background
from LevelLoader import LevelLoader

class World(object):
    clock = pygame.time.Clock()
    FPS = 60
    entityList = []
    running = True
    mainSurface = None
    camPos = [0, 0]
    

    def __init__(self, mainSurface):
        self.roomWidth = 960
        self.roomHeight = 540
<<<<<<< HEAD
        levelTest = LevelLoader(self, "Level1.txt")
=======
>>>>>>> d84fd5fc55f2ef21040272f86b4574c5274e8dbb
        self.assetLoader = AssetLoader(self)
        self.mainSurface = mainSurface
        self.background = Background()
        self.level = 1
        self.loadCurrentLevel()
        pygame.mixer.music.play(-1)
        
    def loadCurrentLevel(self):
        self.loadLevel("Level" + str(self.level) + ".txt")
        
    def loadLevel(self, name):
        self.entityList.clear()
        levelTest = LevelLoader(self, name)
        for object in levelTest.loadLevel():
            self.addEntity(object)
            
    def nextLevel(self):
        self.level += 1
        if (os.path.isfile("Level" + str(self.level) + ".txt")):
            self.loadCurrentLevel()
        else:
            self.loadVictory()
            
    def loadMenu(self):
        self.entityList.clear()
        self.level = 1
        #To be implemented
        
    def loadVictory(self):
        self.entityList.clear()
        #To be implemented

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