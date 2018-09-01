import pygame
import math

class Sprite(object):
    def __init__(self, world, spriteSheet, frameCount=1, animationSpeed=15):
        self.world = world
        self.frameCount = frameCount
        self.animationSpeed = animationSpeed
        size = spriteSheet.get_size()
        self.height = size[1]
        self.width = size[0] / frameCount
        self.frameCount = 1
        self.animationSpeed = 15
        self.frameList = []

        for frame in range(frameCount):
            x = self.width * frame
            self.frameList.append(spriteSheet.subsurface(x, 0, self.width, self.height))

    def draw(self, surface, x, y, frame, angle=0):
        if angle == 0:
            surface.blit(self.frameList[frame], (x - self.width / 2 - self.world.camPos[0], y - self.height / 2 - self.world.camPos[1]))
        else:
            tempSurface = pygame.transform.rotate(self.frameList[frame], angle)
            tempSize = tempSurface.get_size()
            surface.blit(tempSurface, (x - tempSize[0] / 2 - self.world.camPos[0], y - tempSize[1] / 2 - self.world.camPos[1]))