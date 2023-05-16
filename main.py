import pygame

import player_file, world_file, enemy, button, new_menu_file
from settings_file import *
#import bullets

# Inicjalizacja gry
pygame.init()


running_game = False
running_menu = True

#grupy

bullet_groups = pygame.sprite.Group()


# Główna linia gry
while running_menu:
    menu_init = new_menu_file.Menu()
    menu_init.draw()

    if menu_init.draw():
        world = world_file.World(world_data)
        player = player_file.Player(100, SCREEN_HEIGHT - 600)
        enemy_1 = enemy.EnemyBlueGhost(700, SCREEN_HEIGHT - 600)
        running_game = True
        while running_game:
            CLOCK.tick(FPS)
            world.draw()
            player.update()
            player.draw()
            player.health_bar()
            enemy_1.draw(screen)
            #essa = bullets.Bullets()
            #essa.shooting()
            play_menu_theme_music = False
            #for event in pygame.event.get():
            #    if event.type == pygame.MOUSEBUTTONUP:
             #       bullet_groups.add(player.shot_bullet())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running_game = False
                    running_menu = False
                elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    running_game = False
                    running_menu = False

            #bullet_groups.draw(screen)
            #bullet_groups.update()

            pygame.display.flip()

