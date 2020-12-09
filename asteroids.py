""" Main file of asteroids."""
import pygame
import sys
from pygame.locals import *
from Ship import Ship

if __name__ == '__main__':
    pygame.init()
    FPS = 60
    FramePerSec = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((640, 480))

    # fixed sprites
    player_ship = Ship(640, 480)
    player_ship.update()

    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Update sprites
        player_ship.update_keys()

        # Draw sprites
        player_ship.update_sprite()
        DISPLAYSURF.fill((0, 0, 0))
        player_ship.draw(DISPLAYSURF)

        pygame.display.update()
        FramePerSec.tick(FPS)