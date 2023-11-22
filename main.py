import player
import new_menu
import enemy
import world
import sound
from pause_menu import *
import npc
import gameover_menu
from settings import *


# Initialisation of game

pygame.init()
running_game = False
running_menu = True
paused = False

# Groups
all_sprites = pygame.sprite.Group()
bullet_groups = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()

# Main line of game
while running_menu:
    menu_init = new_menu.Menu()
    menu_init.draw()

    if menu_init.draw():
        sound.stop_main_music()
        world = world.World(world_data)
        player = player.Player(100, SCREEN_HEIGHT - 800)
        enemy_1 = enemy.EnemyBlueGhost(2500, SCREEN_HEIGHT - 800)
        enemies_group.add(enemy_1)
        npc_1 = npc.NPC(300, SCREEN_HEIGHT - 800, "assets/npc/npc_dirty.png")
        running_game = True

        if player not in all_sprites:
            all_sprites.add(player)

        if enemy_1 not in all_sprites:
            all_sprites.add(enemy_1)

        while running_game:
            current_time = time.time()

            #all_sprites.update()

            for event in pygame.event.get():

                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    if current_time - last_esc_time >= 0.5:  # Sprawdź, czy minęła co najmniej 1 sekunda od ostatniego esc
                        last_esc_time = current_time
                        pause_menu_screen()

                if event.type == pygame.QUIT:
                    pygame.quit()

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
                    enemy_1.current_health -= 5

                    if enemy_1.checking_is_dead_enemy():
                        enemies_group.remove(enemy)
                        all_sprites.remove(enemy)

            # event for dialogs with npc
            if pygame.key.get_pressed()[pygame.K_e] and player.rect.colliderect(npc_1.rect):
                npc_1.dialog_box()

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
            npc_1.update(screen)

            pygame.display.flip()
