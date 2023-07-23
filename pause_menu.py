from settings_file import *
import pygame
from button import *


def pause_menu_screen():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                paused = False
                return paused


        screen.fill([100, 100, 100])
        pause_text = pygame.image.load("assets/pause_text.png").convert_alpha()
        screen_menu.blit(pause_text, (800, 100))
        pygame.display.flip()

