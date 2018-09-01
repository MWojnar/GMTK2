from World import World
import pygame

pygame.init()
pygame.display.set_caption("test")
windowSize = (960, 540)
screen = pygame.display.set_mode(windowSize)
world = World(screen)
world.run()