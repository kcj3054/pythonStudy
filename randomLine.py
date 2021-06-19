import  sys
import pygame
import random
from pygame.locals import QUIT

pygame.init()
VIEW = pygame.display.set_mode((400, 200))
FPSCLOCK = pygame.time.Clock()


def main():

    while True:

        VIEW.fill((0, 0, 0))

        for event in  pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pointList = []

        for _ in range(10):
            xpos = random.randint(0, 400)
            ypos = random.randint(0, 300)
            pointList.append((xpos, ypos))

        # pygame.draw. #surface , color, close, point, width
        pygame.draw.lines(VIEW, (255, 255, 255), True , pointList, 5)

        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == "__main__":
    main()
