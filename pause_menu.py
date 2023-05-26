from settings_file import *
import pygame


def pause_menu():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                paused = False

        screen.fill([255, 0, 0])

