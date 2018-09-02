from World import World
import pygame

pygame.mixer.pre_init(44100, -16, 20, 2048)
pygame.mixer.init()
pygame.init()
pygame.display.set_caption("test")
windowSize = (960, 540)
screen = pygame.display.set_mode(windowSize)
world = World(screen)
world.run()