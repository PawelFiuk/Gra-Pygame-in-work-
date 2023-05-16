import pygame

import settings_file


class EnemyBlueGhost():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        blue_ghost_img = pygame.image.load("assets/enemy/enemy_1.png").convert_alpha()
        self.image = pygame.transform.scale(blue_ghost_img, (400, 400)).convert_alpha()

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
