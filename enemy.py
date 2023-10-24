import pygame
import math
from settings import  *


class EnemyBlueGhost(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        blue_ghost_img = pygame.image.load("assets/enemy/enemy_1.png").convert_alpha()
        self.image = pygame.transform.scale(blue_ghost_img, (400, 400)).convert_alpha()
        self.atack_area = 150
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, window):
        self.x -= scroll_position_of_player[0]
        self.y -= scroll_position_of_player[1]
        window.blit(self.image, (self.x, self.y))

    def atack_player(self):
        return True


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2
        self.distance_threshold = 200
        self.attack_range = 30
        self.attack_damage = 10
        self.max_health = 100
        self.health = self.max_health
        self.player_seen = False

    def update(self, player):
        if not self.player_seen:
            self.move()
            if self.can_see_player(player):
                self.player_seen = True
        else:
            self.attack(player)


    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0

    def draw(self):
        self.x -= scroll_position_of_player[0]
        self.y -= scroll_position_of_player[1]
        screen.blit(self.image, (self.x, self.y))


