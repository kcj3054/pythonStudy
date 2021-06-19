import  sys
from random import randint
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE

pygame.init()
pygame.key.set_repeat(5, 5)
VIEW = pygame.display.set_mode((800, 600))
FPS = pygame.time.Clock()


def main():
    blocks = 80
    pos_y = 250
    speed = 0
    score = 0
    grt = randint(1, 6)
    sysfont = pygame.font.SysFont(None, 36)
    char_image = pygame.image.load(위치)
    maps = []

    for xpos in range(blocks):
        maps.append(Rect(xpos ))