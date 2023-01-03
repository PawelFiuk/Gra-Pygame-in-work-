import player_file, world_file, enemy, button, new_menu_file
from settings_file import *
import bullets

# Inicjalizacja gry
pygame.init()


running_game = False
running_menu = True

# Główna linia gry
while running_menu:
    menu_init = new_menu_file.Menu()
    menu_init.draw()


    if menu_init.draw():
        world = world_file.World(world_data)
        player = player_file.Player(100, SCREEN_HEIGHT - 600)
        enemy_1 = enemy.EnemyBlueGhost(700, SCREEN_HEIGHT - 600)
        essa = bullets.Bullets.shooting()
        running_game = True
        while running_game:
            CLOCK.tick(200)
            world.draw()
            player.update()
            player.draw()
            player.health_bar()
            enemy_1.draw(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running_game = False
                    running_menu = False
                elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    running_game = False
                    running_menu = False

            pygame.display.flip()

""""
running_game = True
world = world_file.World(world_data)

player = player_file.Player(100, SCREEN_HEIGHT-600)

enemy_1 = enemy.EnemyBlueGhost(700, SCREEN_HEIGHT-600)

while running_game:
    CLOCK.tick(200)
    world.draw()
    player.update()
    player.draw()
    player.health_bar()
    enemy_1.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False
        elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running_game = False

    pygame.display.flip()
"""
