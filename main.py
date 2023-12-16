import pygame.sprite

import player
import new_menu
import enemy
import world
import sound
from pause_menu import *
import npc
import gameover_menu
from settings import *
import airplane
import ammunition_package
import first_aid_kit

# Initialisation of game

pygame.init()
running_game = False
running_menu = True
paused = False

# Groups
all_sprites = pygame.sprite.Group()
bullet_groups = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()
ammo_package_group = pygame.sprite.Group()
aid_kit_group = pygame.sprite.Group()


player = player.Player(100, SCREEN_HEIGHT - 800)
enemy_1 = enemy.EnemyBlueGhost(2500, SCREEN_HEIGHT - 800)
npc_1 = npc.NPC(300, SCREEN_HEIGHT - 800, "assets/npc/npc_dirty.png")
airplane_level_1 = airplane.Airplane(5300, SCREEN_HEIGHT - 1000, "assets/graphics/ship.png")
mech_enemy = enemy.EnemySteamMachine(3700, SCREEN_HEIGHT-1000)
ammo_package_level_1_1 = ammunition_package.AmmunitionPackage(2000, SCREEN_HEIGHT - 500)
aid_kit_1 = first_aid_kit.FirstAidKit(1500, SCREEN_HEIGHT - 500)

enemies_group.add(enemy_1)
enemies_group.add(mech_enemy)
aid_kit_group.add(aid_kit_1)
ammo_package_group.add(ammo_package_level_1_1)
all_sprites.add(player)
all_sprites.add(enemy_1)
all_sprites.add(mech_enemy)

# Main line of game
while running_menu:
    menu_init = new_menu.Menu()
    menu_init.draw()

    if menu_init.draw():
        sound.stop_main_music()
        world = world.World(world_data)
        running_game = True
        while running_game:
            current_time = time.time()

            for event in pygame.event.get():

                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    if current_time - last_esc_time >= 0.5:
                        last_esc_time = current_time
                        pause_menu_screen()

                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        if player.rect.colliderect(airplane_level_1.rect):
                            airplane_level_1.player_in_airplane = True
                            player.enter_airplane_mode()

                        if player.rect.colliderect(npc_1.rect):
                            npc_1.dialog_box()

            # mechanics of shooting
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
            if pygame.key.get_pressed()[pygame.K_c] and out_of_main_ammo :
                sound.empty_magazine_sound()

            if not is_ready_shooting and current_time - last_shot_time_main_weapon > SHOOT_DELAY \
                    and not out_of_main_ammo:
                is_ready_shooting = True

            collisions = pygame.sprite.groupcollide(enemies_group, bullet_groups, False, True)
            for enemy, bullets_hit in collisions.items():
                for bullet in bullets_hit:
                    enemy.current_health -= 5

                    if enemy.checking_is_dead_enemy():
                        enemies_group.remove(enemy)
                        all_sprites.remove(enemy)

            if player.rect.colliderect(ammo_package_level_1_1):
                ammo_package_level_1_1.action_ammo(player)
                ammo_package_group.remove(ammo_package_level_1_1)

            if player.rect.colliderect(aid_kit_1):
                aid_kit_1.action_health(player)
                aid_kit_group.remove(aid_kit_1)

            #sound efects
            if not ambient_music_switch_level_1:
                sound.wind_outside_sound()
                ambient_music_switch_level_1 = True

            play_menu_theme_music = False

            if player.checking_is_dead_player():
                gameover_menu.draw_gameover_menu()

            # main updates for every frame of game
            CLOCK.tick(FPS)

            # updates section
            world.draw()
            player.update()
            bullet_groups.update()
            bullet_groups.draw(screen)
            enemy_1.update()
            mech_enemy.update(player.rect.x)
            npc_1.update(screen)
            airplane_level_1.update(screen, player)
            ammo_package_level_1_1.update_package(screen)
            aid_kit_1.update_package(screen)

            pygame.display.flip()
