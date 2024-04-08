import pygame

from settings import *
import bullets
"""
    These functions are used to better and nicer implement, among others, 
    the collision of the bullets with the enemy using groups from the pygame library.
    Functions are later called in main file in main loop of the game.

"""

def handle_blue_ghost_collision_with_bullet(bullet_group, enemy_group, player_exp_mechanism, player_object):
    for bullet in bullet_group:
        for enemy in enemy_group:
            if pygame.sprite.collide_mask(bullet, enemy):
                enemy.current_health -= bullet.damage_of_bullet
                bullet.kill()
                if enemy.checking_is_dead_enemy():
                    player_exp_mechanism.gain_experience(enemy.exp_for_player, player_object)
                    enemy.kill()

def handle_mech_collision_with_bullet(bullet_groups, mech_group, player_exp_mechanism, player):
    for bullet in bullet_groups:
        for mech in mech_group:
            if pygame.sprite.collide_mask(bullet, mech):
                mech.current_health -= bullet.damage_of_bullet
                mech.received_damage_animation()
                bullet.kill()
                if mech.checking_is_dead_enemy():
                    player_exp_mechanism.gain_experience(mech.exp_for_player, player)
                    mech.kill()

def handle_airplane_bombs_collision(airplane_bullets_group, static_mech_group, player_exp_mechanism, player, explosions_group):
    for bomb in airplane_bullets_group:
        for static_mech in static_mech_group:
            if pygame.sprite.collide_mask(bomb, static_mech):
                static_mech.current_health -= bomb.damage
                bomb.kill()

                explosion_effect = bullets.Explosion(static_mech.rect.x - 90, static_mech.rect.y - 150)
                explosions_group.add(explosion_effect)

                if static_mech.checking_is_dead_enemy():
                    player_exp_mechanism.gain_experience(static_mech.exp_for_player, player)
                    static_mech.kill()

def handle_mech_damage(mech_group, player):
    for enemy in mech_group:
        if enemy.current_animation == 'fight' and enemy.send_damage_to_player_flag:
            if not enemy.damage_sent_to_player and not player.is_magic_snus_taken:
                player.current_health -= 10
                enemy.damage_sent_to_player = True
        else:
            enemy.damage_sent_to_player = False

def handle_grenade_collision(grenade_group, enemy_group, player_exp_mechanism, player, explosions_group):
    for grenade in grenade_group:
        for enemy in enemy_group:
            if pygame.sprite.collide_mask(grenade, enemy):
                enemy.current_health -= grenade.damage
                grenade.kill()
                explosion_effect = bullets.Explosion(grenade.rect.x, grenade.rect.y)
                explosions_group.add(explosion_effect)
                if enemy.checking_is_dead_enemy():
                    player_exp_mechanism.gain_experience(enemy.exp_for_player, player)
                    enemy.kill()

def handle_boss_damage(boss_group, player):
    for enemy in boss_group:
        if enemy.current_animation == 'fight' and enemy.send_damage_to_player_flag:
            if not enemy.damage_sent_to_player and not player.is_magic_snus_taken:
                player.current_health -= 10
                enemy.damage_sent_to_player = True
        else:
            enemy.damage_sent_to_player = False

def handle_boss_collision_with_bullet(bullet_groups, boss_group, player_exp_mechanism, player):
    for bullet in bullet_groups:
        for boss in boss_group:
            if pygame.sprite.collide_mask(bullet, boss):
                boss.current_health -= bullet.damage_of_bullet
                boss.received_damage_animation()
                bullet.kill()
                if boss.checking_is_dead_enemy():
                    player_exp_mechanism.gain_experience(boss.exp_for_player, player)
                    boss.kill()

def handle_pickup_ammo_package(ammo_package_group, player):
    if not player.current_amount_grenades == player.max_grenade_amount or not player.main_ammo_magazine == player.max_main_ammo_magazine:
        for ammo_package in ammo_package_group:
            if player.rect.colliderect(ammo_package):
                ammo_package.action_ammo(player)
                ammo_package.kill()
                return True

def fell_into_darkness(player):
    if not player.airplane_mode and player.rect.y > SCREEN_HEIGHT:
        player.current_health = 0

def fell_into_darkness_airplane(airplane, player):
    if airplane.rect.y > SCREEN_HEIGHT:
        player.current_health = 0

class RoomNavigator:
    def __init__(self, x_cord: int, y_cord: int):
        """
        Arguments: self, position - x and y position where doors to enter should be placed,
        Application: s
        Return: None
        """
        self.entrance = pygame.Rect(x_cord, y_cord, 50, 50)
        self.entrance_alpha = 0  # Przezroczystość wejścia (0 - całkowicie przezroczyste, 255 - całkowicie nieprzezroczyste)
        self.entrance_color = (255, 0, 0)
        self.is_clicked_e = False

    def draw(self):
        screen.blit(self.entrance, (self.x_cord, self.y_cord))
        pygame.display.flip()