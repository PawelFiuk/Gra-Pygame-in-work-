from pkg_resources import resource_dir

from settings import *
import os

class Bullets(pygame.sprite.Sprite):
    def __init__(self, position=[], direction=False):
        """
        Arguments: self, position - x and y position from which the projectile will be fired, direction - responsible for
            the direction in which the bullet flies
        Application: setting the basic parameters of the projectile
        Return: None
        """
        pygame.sprite.Sprite.__init__(self)
        self.bullet_image = pygame.image.load('assets/graphics/bullet.png').convert_alpha()
        self.image = pygame.transform.scale(self.bullet_image, (100, 40)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.rect.center = (position[0], position[1])
        self.direction = direction
        self.velocity_of_bullet = 5
        self.rect = self.bullet_image.get_rect(center=(position[0], position[1]))
        self.distance_of_bullet = 0
        self.flip = False
        self.damage_of_bullet = 5

    def update(self):
        """
        Arguments: self
        Application: used to add dynamics to the bullet, if the player is turned around, the bullet will fly the other way, if
            the projectile reaches a certain distance, it will be destroyed
        Return: None
        """
        if not self.direction:
            self.rect.x += 15
        if self.direction:
            screen.blit(pygame.transform.flip(self.image, self.direction, False), self.rect)
            self.rect.x -= 15

        self.distance_of_bullet += 15

        if self.distance_of_bullet >= 800:
            self.kill()

class AirplaneBulelts(pygame.sprite.Sprite):
    def __init__(self, position=[]):
        """
        Arguments: self, position - x and y position from which the projectile will be fired, direction - responsible for
            the direction in which the bullet flies
        Application: setting the basic parameters of the projectile
        Return: None
        """
        pygame.sprite.Sprite.__init__(self)
        self.airplane_bullet_image = pygame.image.load('assets/graphics/pixel_b.png').convert_alpha()
        self.image = pygame.transform.scale(self.airplane_bullet_image, (200, 200)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.rect.center = (position[0], position[1])
        self.rect = self.airplane_bullet_image.get_rect(center=(position[0], position[1]))
        self.distance_of_bullet = 0


    def update(self):
        """
        Arguments: self
        Application: used to add dynamics to the bullet, if the player is turned around, the bullet will fly the other way, if
            the projectile reaches a certain distance, it will be destroyed
        Return: None
        """
        self.rect.y += 10
        self.distance_of_bullet += 10

        if self.distance_of_bullet >= 1700:
           self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.explosion_images = [pygame.image.load(os.path.join('assets/graphics/special_effects', f'explosion_{i}.png')).convert_alpha()
                                 for i in range(10)]
        self.image = self.explosion_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.frame = 0
        self.animation_speed = 5
        self.last_update = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosion_images):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.explosion_images[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
