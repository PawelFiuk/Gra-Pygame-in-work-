import player_file
import world_file
from settings_file import *
import new_menu_file
import button
import enemy

# Inicjalizacja gry
pygame.init()


running_game = False
running_menu = True

# Główna linia gry

while running_menu:
    menu_init = new_menu_file.Menu()
    menu_init.draw()
    if running_menu == False :
        running_game = True

running_game = True
world = world_file.World(world_data)

player = player_file.Player(100, SCREEN_HEIGHT-600)

enemy_1 = enemy.EnemyBlueGhost(700, SCREEN_HEIGHT-600)

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

