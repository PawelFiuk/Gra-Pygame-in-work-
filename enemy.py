import pygame
import math
import settings_file


class EnemyBlueGhost:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        blue_ghost_img = pygame.image.load("assets/enemy/enemy_1.png").convert_alpha()
        self.image = pygame.transform.scale(blue_ghost_img, (400, 400)).convert_alpha()

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))


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

    def move(self):
        # Przemieszczenie przeciwnika w przypadkowym kierunku
        self.x += self.speed * math.cos(pygame.time.get_ticks() / 1000)
        self.y += self.speed * math.sin(pygame.time.get_ticks() / 1000)

    def can_see_player(self, player):
        # Obliczenie odległości między przeciwnikiem a graczem
        distance = math.sqrt((player.x - self.x) ** 2 + (player.y - self.y) ** 2)
        return distance <= self.distance_threshold

    def attack(self, player):
        # Obliczenie odległości między przeciwnikiem a graczem
        distance = math.sqrt((player.x - self.x) ** 2 + (player.y - self.y) ** 2)
        if distance <= self.attack_range:
            player.take_damage(self.attack_damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0

    def draw(self):
        pygame.draw.circle(settings_file.screen, (255, 0, 0), (self.x, self.y), 20)
        pygame.draw.rect(settings_file.screen, (0, 255, 0), (self.x - 20, self.y - 30, 40, 10))
        pygame.draw.rect(settings_file.screen, (255, 0, 0),
                         (self.x - 20, self.y - 30, 40 * (1 - self.health / self.max_health), 10))
