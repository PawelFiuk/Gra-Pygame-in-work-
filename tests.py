import settings_file
import pygame


def draw_grid():
   for line in range(0, 16):
       pygame.draw.line(settings_file.screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
       pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))