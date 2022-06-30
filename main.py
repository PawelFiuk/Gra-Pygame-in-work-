import player_file
import world_file
from settings_file import *

# Inicjalizacja okna, określenie jego parametrów
pygame.init()
# def draw_grid():
#    for line in range(0, 16):
#        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
#        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))
# Główna linia gry

world = world_file.World(world_data)

player = player_file.Player(100, SCREEN_HEIGHT-600)

running = True
while running:
    CLOCK.tick(200)
    world.draw()
    player.update()
    player.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False

    pygame.display.flip()

pygame.quit()
