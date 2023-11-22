from settings import *


class Bullets(pygame.sprite.Sprite):
    def __init__(self, position=[], direction=False):
        """
        Arguments: self, position - x and y position from which the projectile will be fired, direction - responsible for
            the direction in which the bullet flies
        Application: setting the basic parameters of the projectile
        Return: None
        """
        pygame.sprite.Sprite.__init__(self)
        self.bullet_image = pygame.image.load('assets/bullet.png').convert_alpha()
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
