import pygame
import os.path
from sys import exit
from Entity import Entity
from AssetLoader import AssetLoader
from Background import Background
from LevelLoader import LevelLoader
from Button import Button
from Victory import Victory

class World(object):
    clock = pygame.time.Clock()
    FPS = 60
    entityList = []
    running = True
    mainSurface = None
    camPos = [0, 0]

    def __init__(self, mainSurface, width, height):
        self.roomWidth = width
        self.roomHeight = height
        self.screenWidth = width
        self.screenHeight = height
        self.assetLoader = AssetLoader(self)
        self.mainSurface = mainSurface
        self.background = Background()
        self.level = 1
        self.loadMenu()
        self.events = []
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
        title = Entity(self, self.screenWidth / 2, self.screenHeight / 4 + 20, self.assetLoader.title)
        self.addEntity(title)
        startButton = Button(self, self.screenWidth / 2, self.screenHeight / 2 + 48, self.assetLoader.start, self.assetLoader.startSelected, self.start)
        self.addEntity(startButton)
        quitButton = Button(self, self.screenWidth / 2, self.screenHeight * 3 / 4, self.assetLoader.quit, self.assetLoader.quitSelected, exit)
        self.addEntity(quitButton)
        
    def start(self):
        self.level = 1
        self.loadCurrentLevel()
        
    def loadVictory(self):
        self.entityList.clear()
        victory = Victory(self, self.screenWidth / 2, self.screenHeight / 2, self.assetLoader.victory)
        self.addEntity(victory)
        
    def run(self):
        while self.running:
            self.update()
            self.render()
            
    def update(self):
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
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
            if entity.depth < self.entityList[i].depth:
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