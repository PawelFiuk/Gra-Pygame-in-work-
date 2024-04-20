import pygame

import settings
from settings import *
import bullets
"""
    These functions are used to better and nicer implement, among others, 
    the collision of the bullets with the enemies using groups from the pygame library.
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
def handle_entering_room_1_level_1(doors_group, player, door_object):
    for doors in doors_group:
        if player.rect.colliderect(doors):
            doors.show_information_about_interaction()
            if door_object.enter_room:
                settings.collision_with_doors = True

        else:
            settings.collision_with_doors = False
def fell_into_darkness(player):
    if not player.airplane_mode and player.rect.y > SCREEN_HEIGHT:
        player.current_health = 0

def fell_into_darkness_airplane(airplane, player):
    if airplane.rect.y > SCREEN_HEIGHT:
        player.current_health = 0

class RoomNavigator(pygame.sprite.Sprite):
    def __init__(self, x_cord: int, y_cord: int):
        """
        Arguments: self, position - x and y position where doors to enter should be placed,
        Application: s
        Return: None
        """
        pygame.sprite.Sprite.__init__(self)
        image_doors = pygame.image.load('assets/graphics/doors.png').convert_alpha()
        self.image = pygame.transform.scale(image_doors, (200, 300)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x_cord
        self.rect.y = y_cord
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        self.draw()
        self.update_camera()
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update_camera(self):
        """
            Arguments: self
            Application: updates the display of the package and the world based
                on the player's movement.
            Return: None
        """
        self.rect.x -= scroll_position_of_player[0]

    def show_information_about_interaction(self):
        interaction_information = "Wciśnij E, żeby wejść"
        text_interaction_info = font_skill_tree.render(interaction_information, True, (255, 255, 255))
        screen.blit(text_interaction_info, (550, 450))
        pygame.display.flip()

    def enter_room(self):
        return True
