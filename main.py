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
from pause_menu import *
import npc


# Initialisation of game

pygame.init()
running_game = False
running_menu = True
paused = False
# Groups

bullet_groups = pygame.sprite.Group()

# Main line of game
while running_menu:
    menu_init = new_menu_file.Menu()
    menu_init.draw()

    if menu_init.draw():
        sound.stop_main_music()
        world = world_file.World(world_data)
        player = player_file.Player(100, SCREEN_HEIGHT - 600)
        enemy_1 = enemy.EnemyBlueGhost(2500, SCREEN_HEIGHT - 600)
        npc_1 = npc.NPC(300, SCREEN_HEIGHT - 600, "assets/npc/npc_dirty.png")

        running_game = True
        key = pygame.key.get_pressed()

        while running_game:
            current_time = time.time()
            for event in pygame.event.get():

                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    
                    pause_menu_screen()
                if event.type == pygame.QUIT:
                    pygame.quit()

            if is_ready_shooting:
                if pygame.key.get_pressed()[pygame.K_c]:

                    if current_time - last_shot_time_main_weapon > SHOOT_DELAY:
                        sound.shotgun_sound()
                        last_shot_time_main_weapon = current_time
                        bullet_groups.add(player.shot_bullet())
                        player.main_ammo_magazine -= 1
                        if player.main_ammo_magazine < 1:
                            out_of_main_ammo = True
                        is_ready_shooting = False

            if not is_ready_shooting and current_time - last_shot_time_main_weapon > SHOOT_DELAY \
                    and not out_of_main_ammo:
                is_ready_shooting = True

            tmp = False

            if pygame.key.get_pressed()[pygame.K_e]:
                tmp = True
                if player.rect.colliderect(npc_1.rect):
                    dialogue_switch = True
                else:
                    dialogue_switch = False

            while dialogue_switch or tmp:
                npc_1.dialog_box()
                if pygame.key.get_pressed()[pygame.K_e]:
                    dialogue_switch = False

            CLOCK.tick(FPS)
            world.draw()

            bullet_groups.update()
            player.update()
            player.draw()
            bullet_groups.draw(screen)
            player.health_bar()
            player.main_ammo()
            enemy_1.draw(screen)
            play_menu_theme_music = False
            npc_1.draw(screen)

            pygame.display.flip()
