from math import *

import pygame
from pygame import *

pygame.init()
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption(f"{title}")
clock = pygame.time.Clock()
running = True

def startProgram():

    while running:

        for event in pygame.event.get():
            print(f"{event}")
            if event.type == pygame.QUIT:
                running = False


    pygame.quit()

if __name__ == '__main__':
    startProgram()