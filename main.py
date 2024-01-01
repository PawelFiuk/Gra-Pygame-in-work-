
import bullets
import player
import new_menu
from enemy import EnemyBlueGhost,EnemySteamMachine, EnemyStaticMech
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

# Initialisation of game

pygame.init()
running_game = False
running_menu = True
paused = False

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


# Making objects of game
world = world.World(world_data)
player = player.Player(100, SCREEN_HEIGHT - 800)
enemy_1 = EnemyBlueGhost(2500, SCREEN_HEIGHT - 800)
npc_1 = npc.NPC(300, SCREEN_HEIGHT - 800, "assets/npc/npc_dirty.png")
npc_2 = npc.NPC2(4900, SCREEN_HEIGHT - 800, "assets/npc/Man.png")
airplane_level_1 = airplane.Airplane(5500, SCREEN_HEIGHT - 1000, "assets/graphics/ship.png")
mech_enemy = EnemySteamMachine(3700, SCREEN_HEIGHT-1000)
ammo_package_level_1_1 = ammunition_package.AmmunitionPackage(2000, SCREEN_HEIGHT - 500)
aid_kit_1 = first_aid_kit.FirstAidKit(1500, SCREEN_HEIGHT - 500)
skill_tree_for_player = skill_tree.SkillTree(player)
snus_1_1 = magic_snus.MagicSnus(2600, SCREEN_HEIGHT - 500)
static_mech_1 = EnemyStaticMech(7000, 930)
static_mech_2 = EnemyStaticMech(7600, 930)
static_mech_3 = EnemyStaticMech(8400, 930)
static_mech_4 = EnemyStaticMech(9500, 930)


# Adding objects to groups
enemies_group.add(enemy_1)
mech_group.add(mech_enemy)
static_mech_group.add(static_mech_1, static_mech_2, static_mech_3, static_mech_4)
aid_kit_group.add(aid_kit_1)
ammo_package_group.add(ammo_package_level_1_1)
blue_ghost_group.add(enemy_1)

all_enemies_group.add(mech_group, blue_ghost_group)



# Main line of game
while running_menu:
    menu_init = new_menu.Menu()
    menu_init.draw()

    if menu_init.draw():
        START_GAME = True
        sound.stop_main_music()
        running_menu = False

while START_GAME:
    running_game = True
    while running_game:
        current_time = time.time()

        for event in pygame.event.get():

            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                if current_time - last_esc_time >= 0.5:
                    last_esc_time = current_time
                    pause_menu_screen()

            elif event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    if player.rect.colliderect(airplane_level_1.rect) and not airplane_level_1.player_in_airplane:
                        time_entered_airplane = current_time
                        airplane_level_1.player_in_airplane = True
                        player.enter_airplane_mode()

                    if player.rect.colliderect(npc_1.rect):
                        npc_1.dialog_box()

                    if player.rect.colliderect(npc_2.rect):
                        npc_2.dialog_box()

            elif airplane_level_1.player_in_airplane and pygame.key.get_pressed()[pygame.K_e]:
                if current_time - time_entered_airplane >= 2.0:
                    airplane_level_1.player_in_airplane = False
                    player.exit_airplane_mode(airplane_level_1.rect.x, airplane_level_1.rect.y)

            elif pygame.key.get_pressed()[pygame.K_r]:
                skill_tree_for_player.update()

        # mechanics of shooting
        if is_ready_shooting:
            if pygame.key.get_pressed()[pygame.K_c] and not airplane_level_1.player_in_airplane:
                if current_time - last_shot_time_main_weapon > SHOOT_DELAY and player.main_ammo_magazine > 0:
                    sound.shotgun_sound()
                    last_shot_time_main_weapon = current_time
                    bullet_groups.add(player.shot_bullet())
                    if not player.is_magic_snus_taken:
                        player.main_ammo_magazine -= 1
                    if player.main_ammo_magazine < 1:
                        out_of_main_ammo = True
                    is_ready_shooting = False
            elif player.main_ammo_magazine > 0 :
                out_of_main_ammo = False
        if pygame.key.get_pressed()[pygame.K_c] and out_of_main_ammo :
            sound.empty_magazine_sound()

        if is_ready_throwing:
            if pygame.key.get_pressed()[pygame.K_v] and not airplane_level_1.player_in_airplane:
                if current_time - last_time_throw_grenade > THROW_DELAY and player.current_amount_grenades > 0:
                    last_time_throw_grenade = current_time
                    grenades_group.add(player.throw_grenade())
                    if not player.is_magic_snus_taken:
                        player.current_amount_grenades -= 1
                    if player.main_ammo_magazine < 1:
                        out_of_grenades = True
                    is_ready_throwing = False
            elif player.main_ammo_magazine > 0:
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


        for bullet in bullet_groups:
            for blue_ghost in blue_ghost_group:
                if pygame.sprite.collide_mask(bullet, blue_ghost):
                    blue_ghost.current_health -= bullet.damage_of_bullet
                    bullet.kill()
                    if blue_ghost.checking_is_dead_enemy():
                        player.gain_experience(blue_ghost.exp_for_player)
                        blue_ghost.kill()

        for bullet in bullet_groups:
            for mech in mech_group:
                if pygame.sprite.collide_mask(bullet, mech):
                    mech.current_health -= bullet.damage_of_bullet
                    enemy.received_damage_animation()
                    bullet.kill()
                    if mech.checking_is_dead_enemy():
                        player.gain_experience(mech.exp_for_player)
                        mech.kill()

        for bomb in airplane_bullets_group:
            for static_mech in static_mech_group:
                if pygame.sprite.collide_mask(bomb, static_mech):
                    static_mech.current_health -= bomb.damage
                    bomb.kill()

                    explosion_effect = bullets.Explosion(static_mech.rect.x - 90, static_mech.rect.y - 150)
                    explosions_group.add(explosion_effect)

                    if static_mech.checking_is_dead_enemy():
                        player.gain_experience(static_mech.exp_for_player)
                        static_mech.kill()

        for enemy in mech_group:
            if enemy.current_animation == 'fight' and enemy.send_damage_to_player_flag:
                if not enemy.damage_sent_to_player:
                    if not player.is_magic_snus_taken:
                        player.current_health -= 10
                        enemy.damage_sent_to_player = True
            else:
                enemy.damage_sent_to_player = False

        for grenade in grenades_group:
            for enemy in all_enemies_group:
                if pygame.sprite.collide_mask(grenade, enemy):
                    enemy.current_health -= grenade.damage
                    grenade.kill()

                    explosion_effect = bullets.Explosion(enemy.rect.x - 90, enemy.rect.y - 150)
                    explosions_group.add(explosion_effect)

                    if enemy.checking_is_dead_enemy():
                        player.gain_experience(enemy.exp_for_player)
                        enemy.kill()

        if player.rect.colliderect(ammo_package_level_1_1):
            ammo_package_level_1_1.action_ammo(player)
            ammo_package_level_1_1.kill()
            ammo_package_group.remove(ammo_package_level_1_1)
            out_of_main_ammo = False

        if player.rect.colliderect(aid_kit_1):
            aid_kit_1.action_health(player)
            aid_kit_group.remove(aid_kit_1)

        if player.rect.colliderect(snus_1_1) and player.is_magic_snus_taken == False:
            snus_taken_time = current_time
            snus_1_1.action_magic_stats(player)
            player.snus_special_effect()

        if current_time - snus_taken_time > 5:
            player.is_magic_snus_taken = False

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

        explosions_group.draw(screen)
        explosions_group.update()
        snus_1_1.update_package(screen)
        bullet_groups.update()
        bullet_groups.draw(screen)
        grenades_group.update()
        grenades_group.draw(screen)
        airplane_bullets_group.update()
        airplane_bullets_group.draw(screen)
        enemy_1.update()
        mech_enemy.update(player.rect.x, player.current_health)
        npc_1.update(screen)
        npc_2.update(screen)
        airplane_level_1.update(screen, world)
        ammo_package_level_1_1.update_package(screen)
        aid_kit_1.update_package(screen)
        static_mech_group.draw(screen)
        static_mech_group.update()
        player.update(world)

        pygame.display.flip()
