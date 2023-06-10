import pygame.sprite
import time
import bullets
import player_file
import new_menu_file
import button
import enemy
import world_file
import sound
from settings_file import *


# Inicjalizacja gry
pygame.init()


running_game = False
running_menu = True

# grupy
bullet_groups = pygame.sprite.Group()

SHOOTING = False
IS_READY_SHOOTING = True
LAST_SHOT_TIME = 0
SHOOT_DELAY = 1

# Główna linia gry
while running_menu:
    menu_init = new_menu_file.Menu()
    menu_init.draw()

    if menu_init.draw():
        sound.stop_main_menu_music()
        world = world_file.World(1)
        player = player_file.Player(100, SCREEN_HEIGHT - 600)
        enemy_1 = enemy.EnemyBlueGhost(1200, SCREEN_HEIGHT - 400)

        running_game = True
        key = pygame.key.get_pressed()

        while running_game:
            current_time = time.time()
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running_game = False
                    running_menu = False
                elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    running_game = False
                    running_menu = False

            if IS_READY_SHOOTING:
                if pygame.key.get_pressed()[pygame.K_c]:

                    if current_time - LAST_SHOT_TIME > SHOOT_DELAY:
                        last_shot_time = current_time
                        bullet_groups.add(player.shot_bullet())
                        IS_READY_SHOOTING = False

                    if not IS_READY_SHOOTING and current_time - LAST_SHOT_TIME > SHOOT_DELAY:
                        IS_READY_SHOOTING = True


            CLOCK.tick(FPS)
            world.draw()

            bullet_groups.update()
            player.update()
            player.draw()
            bullet_groups.draw(screen)
            player.health_bar()
            enemy_1.draw(screen)
            play_menu_theme_music = False
            pygame.display.flip()
