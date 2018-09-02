from World import World
import pygame

pygame.mixer.pre_init(44100, -16, 20, 2048)
pygame.mixer.init()
pygame.init()
pygame.display.set_caption("In Space No One Can Hear You Jump")
width = 960
height = 540
windowSize = (width, height)
screen = pygame.display.set_mode(windowSize)
world = World(screen, width, height)
world.run()