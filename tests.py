import settings_file
import pygame


# narysowanie staki na kafelkach
def draw_grid():
    for line in range(0, 16):
        pygame.draw.line(settings_file.screen, (255, 255, 255), (0, line * settings_file.TILE_SIZE),
                         (settings_file.SCREEN_WIDTH, line * settings_file.TILE_SIZE))
        pygame.draw.line(settings_file.screen, (255, 255, 255), (line * settings_file.TILE_SIZE, 0),
                         (line * settings_file.TILE_SIZE, settings_file.SCREEN_HEIGHT))
