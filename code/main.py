import player
import new_menu
from enemy import EnemyBlueGhost,EnemySteamMachine, EnemyStaticMech, EnemyBossFirstLevel
import world
import sound
from pause_menu import *
import npc
import gameover_menu
from settings import *
import airplane
import ammunition_package
import first_aid_kit
import skill_tree
import magic_snus
import events
import UI
import EQ


# Initialisation of game

pygame.init()
running_game = True
running_level_1 = False
running_menu = True
paused = False
running_level_1_room_1 = False

# Groups
bullet_groups = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()
ammo_package_group = pygame.sprite.Group()
aid_kit_group = pygame.sprite.Group()
mech_group = pygame.sprite.Group()
airplane_bullets_group = pygame.sprite.Group()
static_mech_group = pygame.sprite.Group()
snus_group = pygame.sprite.Group()
explosions_group = pygame.sprite.Group()
grenades_group = pygame.sprite.Group()
blue_ghost_group = pygame.sprite.Group()
all_enemies_group = pygame.sprite.Group()
boss_group = pygame.sprite.Group()
doors_group_level_1 = pygame.sprite.Group()
doors_group_level_1_room_1 = pygame.sprite.Group()

# Making objects of game
world_level_1 = world.Level1(world_data)
world_level_2 = world.Level1(world_data_level_2)
player_object = player.Player(100, SCREEN_HEIGHT - 800)
player_ui = player.PlayerUI(player_object)
player_experience_mechanism = player.PlayerLevelMechanism(player_object)
enemy_1 = EnemyBlueGhost(2500, SCREEN_HEIGHT - 800)
npc_1 = npc.NPC(300, SCREEN_HEIGHT - 800, "assets/graphics/npc/npc_dirty.png")
npc_2 = npc.NPC2(4900, SCREEN_HEIGHT - 800, "assets/graphics/npc/Man.png")
airplane_level_1 = airplane.Airplane(5500, SCREEN_HEIGHT - 1000, "assets/graphics/ship.png")
mech_enemy = EnemySteamMachine(3700, SCREEN_HEIGHT-1000)
mech_enemy_2 = EnemySteamMachine(11500, SCREEN_HEIGHT-1000)
mech_enemy_3 = EnemySteamMachine(13000, SCREEN_HEIGHT-1000)
mech_enemy_4 = EnemySteamMachine(14000, SCREEN_HEIGHT-1000)
ammo_package_level_1_1 = ammunition_package.AmmunitionPackage(2000, SCREEN_HEIGHT - 500)
ammo_package_level_1_2 = ammunition_package.AmmunitionPackage(13000, SCREEN_HEIGHT - 500)
ammo_package_level_1_3 = ammunition_package.AmmunitionPackage(12000, SCREEN_HEIGHT - 500)
aid_kit_1 = first_aid_kit.FirstAidKit(1500, SCREEN_HEIGHT - 500)
aid_kit_2 = first_aid_kit.FirstAidKit(12100, SCREEN_HEIGHT - 500)
skill_tree_for_player = skill_tree.SkillTree(player_object)
snus_1_1 = magic_snus.MagicSnus(14000, SCREEN_HEIGHT - 500)
static_mech_1 = EnemyStaticMech(7000, 930)
static_mech_2 = EnemyStaticMech(7600, 930)
static_mech_3 = EnemyStaticMech(8400, 930)
static_mech_4 = EnemyStaticMech(9500, 930)
boss = EnemyBossFirstLevel(15500, SCREEN_HEIGHT - 800)
player_eq = EQ.PlayerInventory(slot_invetory_data)
doors_to_level_1_room_1 = events.RoomNavigator(1200, 350)
doors_to_back_level_1 = events.RoomNavigator(100, 150)

# Adding objects to groups
enemies_group.add(enemy_1)
mech_group.add(mech_enemy, mech_enemy_2, mech_enemy_3, mech_enemy_4)
static_mech_group.add(static_mech_1, static_mech_2, static_mech_3, static_mech_4)
aid_kit_group.add(aid_kit_1 ,aid_kit_2)
ammo_package_group.add(ammo_package_level_1_1, ammo_package_level_1_2, ammo_package_level_1_3)
blue_ghost_group.add(enemy_1)
boss_group.add(boss)
doors_group_level_1.add(doors_to_level_1_room_1)
doors_group_level_1_room_1.add(doors_to_back_level_1)

all_enemies_group.add(mech_group, blue_ghost_group, boss_group)

# Main line of game
while running_menu:
    menu_init = new_menu.Menu()
    menu_init.draw()

    if menu_init.draw():
        sound.stop_main_music()
        running_level_1 = True
        running_menu = False

while running_game:
    while running_level_1:
        current_time = time.time()

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE] and current_time - last_esc_time >= 0.5:
                last_esc_time = current_time
                pause_menu_screen()

            elif event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    if player_object.rect.colliderect(airplane_level_1.rect) and not airplane_level_1.player_in_airplane:
                        time_entered_airplane = current_time
                        airplane_level_1.player_in_airplane = True
                        player_object.enter_airplane_mode()

                    elif settings.collision_with_doors:
                        player_object.rect.x = 250
                        player_object.rect.y = 480
                        running_level_1_room_1 = True
                        running_level_1 = False

                    if player_object.rect.colliderect(npc_1.rect) or player_object.rect.colliderect(npc_2.rect):
                        npc_1.dialog_box()
                    if tutorial_flag:
                        if player_object.rect.colliderect(npc_1.rect) or player_object.rect.colliderect(npc_2.rect):
                            tutorial_flag = False
                            npc_1.clicked_tutorial = True

            elif airplane_level_1.player_in_airplane and keys[pygame.K_e] and current_time - time_entered_airplane >= 2.0:
                airplane_level_1.player_in_airplane = False
                player_object.exit_airplane_mode(airplane_level_1.rect.x, airplane_level_1.rect.y)

            elif keys[pygame.K_r]:
                skill_tree_for_player.update(player_object)

            elif keys[pygame.K_p]:
                player_eq.update()

        # mechanics of shooting
        if is_ready_shooting:
            if pygame.key.get_pressed()[pygame.K_c] and not airplane_level_1.player_in_airplane:
                if current_time - last_shot_time_main_weapon > SHOOT_DELAY and player_object.main_ammo_magazine > 0:
                    sound.shotgun_sound()
                    last_shot_time_main_weapon = current_time
                    bullet_groups.add(player_object.shot_bullet())
                    if not player_object.is_magic_snus_taken:
                        player_object.main_ammo_magazine -= 1
                    elif player_object.main_ammo_magazine < 1:
                        player_object.main_ammo_magazine = 0
                        out_of_main_ammo = True
                    is_ready_shooting = False
            elif player_object.main_ammo_magazine > 0 :
                out_of_main_ammo = False
        if pygame.key.get_pressed()[pygame.K_c] and out_of_main_ammo :
            sound.empty_magazine_sound()

        if player_object.main_ammo_magazine > 0:
            out_of_main_ammo = False
        if is_ready_throwing:
            if pygame.key.get_pressed()[pygame.K_v] and not airplane_level_1.player_in_airplane:
                if current_time - last_time_throw_grenade > THROW_DELAY and player_object.current_amount_grenades > 0:
                    last_time_throw_grenade = current_time
                    grenades_group.add(player_object.throw_grenade())
                    if not player_object.is_magic_snus_taken:
                        player_object.current_amount_grenades -= 1
                    elif player_object.main_ammo_magazine < 1:
                        out_of_grenades = True
                    is_ready_throwing = False
        if player_object.current_amount_grenades > 0:
            out_of_grenades = False

        if not is_ready_throwing and current_time - last_shot_time_main_weapon > THROW_DELAY \
                and not out_of_grenades:
            is_ready_throwing = True

        if is_ready_shooting_airplane:
            if pygame.key.get_pressed()[pygame.K_c] and airplane_level_1.player_in_airplane:
                time_since_last_airplane_shot = current_time - last_shot_time_airplane
                if time_since_last_airplane_shot >= 2.0:
                    last_shot_time_airplane = current_time
                    airplane_bullets_group.add(airplane_level_1.shot_bullet())
                    is_ready_shooting_airplane = False

        if not is_ready_shooting_airplane and (current_time - last_shot_time_airplane > SHOOT_DELAY_AIRPLANE):
            is_ready_shooting_airplane = True

        if not is_ready_shooting and current_time - last_shot_time_main_weapon > SHOOT_DELAY \
                and not out_of_main_ammo:
            is_ready_shooting = True

        events.handle_blue_ghost_collision_with_bullet(bullet_groups, blue_ghost_group, player_experience_mechanism, player_object)
        events.handle_mech_collision_with_bullet(bullet_groups, mech_group, player_experience_mechanism, player_object)
        events.handle_airplane_bombs_collision(airplane_bullets_group, static_mech_group, player_experience_mechanism, player_object, explosions_group)
        events.handle_mech_damage(mech_group, player_object)
        events.handle_grenade_collision(grenades_group, all_enemies_group, player_experience_mechanism, player_object, explosions_group)
        events.handle_boss_damage(boss_group, player_object)
        events.handle_boss_collision_with_bullet(bullet_groups, boss_group, player_experience_mechanism, player_object)
        events.handle_pickup_ammo_package(ammo_package_group, player_object)
        events.fell_into_darkness(player_object)
        events.fell_into_darkness_airplane(airplane_level_1, player_object)
        events.handle_entering_room_1_level_1(doors_group_level_1, player_object, doors_to_level_1_room_1)



        if player_object.rect.colliderect(aid_kit_1):
            aid_kit_1.action_health(player_object)
            aid_kit_group.remove(aid_kit_1)

        if player_object.rect.colliderect(snus_1_1) and player_object.is_magic_snus_taken == False:
            snus_taken_time = current_time
            snus_1_1.action_magic_stats(player_object)
            player_object.snus_special_effect()

        if current_time - snus_taken_time > 5:
            player_object.is_magic_snus_taken = False

        #sound efects
        if not ambient_music_switch_level_1:
            sound.wind_outside_sound()
            ambient_music_switch_level_1 = True

        play_menu_theme_music = False

        if player_object.checking_is_dead_player():
            gameover_menu.draw_gameover_menu()

        # main updates for every frame of game
        CLOCK.tick(FPS)

        world_level_1.draw()
        snus_1_1.update_package(screen)
        bullet_groups.update()
        bullet_groups.draw(screen)
        grenades_group.update()
        grenades_group.draw(screen)
        airplane_bullets_group.update()
        airplane_bullets_group.draw(screen)
        enemy_1.update()
        mech_group.update(player_object.rect.x, world_level_1)

        boss_group.update(player_object.rect.x, world_level_1)
        explosions_group.draw(screen)
        explosions_group.update()
        doors_to_level_1_room_1.update()

        npc_1.update(screen)
        npc_2.update(screen)
        airplane_level_1.update(screen, world_level_1, player_object)
        ammo_package_group.update(screen)
        aid_kit_1.update_package(screen)
        static_mech_group.draw(screen)
        static_mech_group.update()
        player_object.update_level_1(world_level_1, airplane_level_1)
        player_ui.update_player_ui(player_object)
        UI.grenades_icon()
        UI.ammo_icon()
        pygame.display.flip()


    while running_level_1_room_1:
        current_time = time.time()
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE] and current_time - last_esc_time >= 0.5:
                last_esc_time = current_time
                pause_menu_screen()

            elif event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    if settings.collision_with_doors:
                        running_level_1 = True
                        running_level_1_room_1 = False


            elif keys[pygame.K_r]:
                skill_tree_for_player.update(player_object)

            elif keys[pygame.K_p]:
                player_eq.update()

        events.handle_entering_room_1_level_1(doors_group_level_1_room_1, player_object, doors_to_back_level_1)

        world_level_2.draw()
        doors_to_back_level_1.update()
        player_object.update_level_1_room_1(world_level_2)
        CLOCK.tick(FPS)
        pygame.display.flip()