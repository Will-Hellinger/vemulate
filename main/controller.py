import pygame
import time


class Controller:
    def __init__(self):
        self.screen_resolution: tuple = (127, 63) # This is 128 x 64
        
        pygame.init()
        self.screen = pygame.display.set_mode([self.screen_resolution[0], self.screen_resolution[1]])
        pygame.display.set_caption("Controller")
    