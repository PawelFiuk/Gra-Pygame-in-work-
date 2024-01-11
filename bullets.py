import pygame.sprite
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
        self.damage = 15

    def update(self):
        """
        Arguments: self
        Application: used to add dynamics to the bullet, if the player is turned around, the bullet will fly the other way, if
            the projectile reaches a certain distance, it will be destroyed
        Return: None
        """
        self.rect.y += 10
        self.distance_of_bullet += 10
        self.rect.x -= scroll_position_of_player[0]

        if self.distance_of_bullet >= 1700:
           self.kill()

    #def collision_with_enemy(self, enemy):
    #    if pygame.sprite.spritecollide(self, enemy, True):
    #        enemy.current_health -=15

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, animation_speed=35):
        """
        Arguments: self, position - x and y position from which the explosion animation will be started, animation_speed -
            the speed at which animation frames will change
        Application: setting the basic parameters of the explosion animation
        Return: None
        """
        pygame.sprite.Sprite.__init__(self)
        self.explosion_images = [pygame.image.load(os.path.join('assets/graphics/special_effects/Circle_explosion', f'Circle_explosion{i}.png')).convert_alpha()
                                 for i in range(1, 11)]
        self.image = self.explosion_images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.frame = 0
        self.animation_speed = animation_speed
        self.last_update = pygame.time.get_ticks()

    def update(self):
        """
           Arguments: self
           Application: method calls any other methods to be called or checked in each frame of the game,
                it serves as a handle
           Return: None
        """
        self.animate()
        self.draw()

    def animate(self):
        """
           Arguments: self
           Application: method supports animations, changes frames after time, etc.
           Return: None
        """
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
    def draw(self):
        """
           Arguments: self
           Application: method draws animation of explosion on screen
           Return: None
        """
        self.rect.x -= scroll_position_of_player[0]
        screen.blit(self.image, self.rect)

class Grenade(pygame.sprite.Sprite):
    def __init__(self, position=[], direction=False):
        """
        Arguments: self, position - x and y position from which the grenade will be throwed, direction - responsible for
            the direction in which the bullet flies
        Application: setting the basic parameters of the projectile
        Return: None
        """
        pygame.sprite.Sprite.__init__(self)
        self.grenade_image = pygame.image.load('assets/graphics/grenade.png').convert_alpha()
        self.image = pygame.transform.scale(self.grenade_image, (40, 40)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.rect.center = (position[0], position[1])
        self.direction = direction
        self.velocity_of_grenade_y = -30
        self.velocity_of_grenade_x = 5
        self.rect = self.grenade_image.get_rect(center=(position[0]- 90, position[1] + 250))
        self.distance_of_grenade = 0
        self.flip = False
        self.damage = 10

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
        self.velocity_of_grenade_y += 1.5
        dy = self.velocity_of_grenade_y
        self.rect.y += dy
        self.distance_of_grenade += 2


        if self.distance_of_grenade >= 90:
            self.kill()
