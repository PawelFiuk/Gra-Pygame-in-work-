import player_file
import world_file
from settings_file import *
import menu_file
import button
import enemy

# Inicjalizacja gry
pygame.init()

'''
running_game = False
menu_init = menu_file.Menu()
button_start = button.Button(0, 500, start_button_img, 0.8)
button_quit = button.Button(60, 700, exit_button_img, 0.025)
menu_init.draw()
'''

# Główna linia gry

world = world_file.World(world_data)

player = player_file.Player(100, SCREEN_HEIGHT-600)

enemy_1 = enemy.EnemyBlueGhost(700, SCREEN_HEIGHT-600)

running_game = True
while running_game:
    CLOCK.tick(200)
    world.draw()
    player.update()
    player.draw()
    enemy_1.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False
        elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running_game = False

    pygame.display.flip()

pygame.quit()

