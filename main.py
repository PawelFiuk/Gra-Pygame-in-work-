import player_file
import world_file
from settings_file import *
import menu_file

# Inicjalizacja gry
pygame.init()

menu_init = menu_file.Menu()
menu_init.draw()

'''
# def draw_grid():
#    for line in range(0, 16):
#        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
#        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))
# Główna linia gry

world = world_file.World(world_data)

player = player_file.Player(100, SCREEN_HEIGHT-600)

running_game = True
while running_game:
    CLOCK.tick(200)
    world.draw()
    player.update()
    player.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False
        elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running_game = False

    pygame.display.flip()

pygame.quit()
 '''