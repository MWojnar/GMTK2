'''
Created on Aug 31, 2018

@author: micha
'''

class Sprite(object):


    def __init__(self, spriteSheet, frameCount=1, animationSpeed=15):
        self.frameCount = frameCount
        self.animationSpeed = animationSpeed
        size = spriteSheet.get_size()
        frameHeight = size[1]
        frameWidth = size[0] / frameCount
        self.frameCount = 1
        self.animationSpeed = 15
        self.frameList = []

        for frame in range(frameCount):
            x = frameWidth * frame
            self.frameList.append(spriteSheet.subsurface(x, 0, frameWidth, frameHeight))

    def draw(self, surface, x, y, frame):
        surface.blit(self.frameList[frame], (x, y))