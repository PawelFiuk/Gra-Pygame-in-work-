from settings import *
import pygame
class Physics:
    @staticmethod
    def check_collision(player, world):
        for tile in world.tile_list:
            if tile[1].colliderect(player.rect.x + player.change_position_x_player,
                                   player.rect.y + player.change_position_y_player, player.width, player.height):
                player.change_position_x_player = 0

            if not player.ground_collision:
                if tile[1].colliderect(player.rect.x, player.rect.y + player.change_position_y_player,
                                       player.width, player.height):
                    player.change_position_y_player = tile[1].top - player.rect.bottom
                    player.velocity_y = 0
                    player.jumper = 'ready'
                    player.falling = False
                    player.ground_collision = True
                    player.is_jumping = False
                    scroll_position_of_player[1] = 0
                    player.change_position_y_player = 0
    @staticmethod
    def apply_gravity(player):
        if player.falling:
            player.velocity_y += 0.2

        if player.velocity_y == -10 or not player.ground_collision:
            player.falling = True

        player.change_position_y_player += player.velocity_y

    @staticmethod
    def check_collision_airplane(airplane, world):
        for tile in world.tile_list:
            if tile[1].colliderect(airplane.rect.x + airplane.change_position_x_airplane,
                                   airplane.rect.y, airplane.width, airplane.height):
                airplane.change_position_x_airplane = 0
                #airplane.change_position_x_airplane = tile[1].top - airplane.rect.bottom
                scroll_position_of_player[0] = 0


            if tile[1].colliderect(airplane.rect.x, airplane.rect.y + airplane.change_position_y_airplane,
                                   airplane.width, airplane.height):
                airplane.change_position_y_airplane = tile[1].top - airplane.rect.bottom
                airplane.velocity_y = 0
                scroll_position_of_player[1] = 0
                #airplane.change_position_y_airplane = 0

