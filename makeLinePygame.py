import sys
import pygame
import random
from pygame.locals import QUIT


pygame.init()
VIEW = pygame.display.set_mode((400, 220))
FPSCLOCK = pygame.time.Clock()


def main():

    while True:

        VIEW.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pointList = []

        for _ in range(10):
            xpos = random.randint(0, 400)
            ypos = random.randint(0, 300)
            pointList.append((xpos, ypos))

        pygame.draw.lines(VIEW, (255, 255, 255), True, pointList, 5) # 화면, color, closed(이어지는 여러 개의 선을 다 그리고 하나의 구역으로 설정할지 결정), pointList(그릴 위치), width
        
        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()