""" Main file of asteroids."""
import pygame
import sys
from pygame.locals import *
from Ship import Ship
from Asteroid import Asteroid

if __name__ == '__main__':
    FPS = 60
    WINDOW_RES = (640, 480)
    BG_COLOR = (0, 0, 0) # RGB for black

    pygame.init()
    FramePerSec = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode(WINDOW_RES)

    # fixed sprites
    player_ship = Ship(*WINDOW_RES)
    player_ship.update()

    # Test asteroid
    test_asteroid = Asteroid(200, 200, 30)

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
        DISPLAYSURF.fill(BG_COLOR)
        player_ship.draw(DISPLAYSURF)
        test_asteroid.draw(DISPLAYSURF)

        pygame.display.update()
        FramePerSec.tick(FPS)