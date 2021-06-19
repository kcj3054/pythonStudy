import sys
import pygame
import random
from pygame.locals import QUIT


pygame.init()
VIEW = pygame.display.set_mode((400, 200))
FPSCLOCK = pygame.time.Clock()


def  main():

    while True:

        VIEW.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type ==QUIT:
                pygame.QUIT
                sys.exit()

        pygame.draw.line(VIEW, (255, 0, 0), (10, 80)
                         , (200, 80))
        pygame.draw.line(VIEW, (255, 0, 0), (10, 150)
                         , (200, 150), 15)
        pygame.draw.line(VIEW, (0, 255, 0), (250, 30)
                         , (250, 200), 15)

        startPos = (300, 30)
        endPos =   (380, 200)
        pygame.draw.line(VIEW, (0, 255, 0), startPos, endPos, 10)
        pygame.display.update()
        FPSCLOCK.tick(3)


if __name__ == "__main__":
    main()