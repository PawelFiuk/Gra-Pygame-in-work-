import pygame
from settings_file import *


class Bullets(pygame.sprite.Sprite):
    def __int__(self):
        bullet_image = pygame.image.load('assets/bullet.png').convert_alpha()
        self.image = pygame.transform.scale(bullet_image, (10, 10)).convert_alpha()
        self.rect = self.image.get_rect()
        #self.rect.x = x_pos  # Wybieramy lokalizacje gdzie pojawi się postać
        #self.rect.y = y_pos
        self.velocity_of_bullet = 5

    def shooting(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_l]:
            screen.blit(self.image, [50, 50])

