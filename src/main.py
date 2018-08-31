'''
Created on Aug 31, 2018

@author: Michael
'''

import World
import pygame

pygame.init()
pygame.display.set_caption("test")
screen = pygame.display.set_mode((500, 500))
world = World.World(screen)
world.run()