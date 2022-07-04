import player_file
import world_file
from settings_file import *
import menu_file
import button

# Inicjalizacja gry
pygame.init()

menu_init = menu_file.Menu()
button_start = button.Button(100, 500, start_button_img, 1)
menu_init.draw()
button_start.draw()

'''
# Główna linia gry

world = world_file.World(world_data)

player = player_file.Player(100, SCREEN_HEIGHT-600)

running_game = True
while running_game:
    CLOCK.tick(120)
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
