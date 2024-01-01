import pygame.sprite
from settings import *
import physics
from bullets import AirplaneBulelts

class Airplane(pygame.sprite.Sprite):
    def __init__(self, x, y, image_source):
        pygame.sprite.Sprite.__init__(self)
        airplane_image = pygame.image.load(image_source).convert_alpha()
        self.image = pygame.transform.scale(airplane_image, (1200, 600)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.velocity_y = 0
        self.flip = False
        self.x = x
        self.y = y
        self.player_in_airplane = False
        self.change_position_x_airplane = 0
        self.change_position_y_airplane = 0




    def update(self, window, world):
        self.update_camera()
        self.draw(window)
        if self.player_in_airplane:
            self.control()
            self.check_collisions(world)


    def draw(self, window):
            window.blit(self.image, (self.rect.x, self.rect.y))

    def update_camera(self):
        self.rect.x -= scroll_position_of_player[0]
        self.rect.x += self.change_position_x_airplane
        self.rect.y += self.change_position_y_airplane



    def control(self):
        keys = pygame.key.get_pressed()

        self.change_position_x_airplane= 0
        self.change_position_y_airplane = 0

        if keys[pygame.K_a]:
            self.change_position_x_airplane -= 8
        if keys[pygame.K_d]:
            self.change_position_x_airplane += 8
        if keys[pygame.K_w]:
            self.rect.y -= 5
        if keys[pygame.K_s]:
            self.rect.y += 5

    def check_collisions(self, world):
        """
           Arguments: self
           Application: updates the display of the airplane and the world based
               on the player's movement.
           Return: None
        """
        physics.Physics.check_collision_airplane(self, world)

    def shot_bullet(self):
        """
        Arguments: self
        Application: This method is used to create a new class of projectile that will be fired after
            a specific game event. Supports shooting from two sides, when the player is turned and when he is not.
        Return: Bullets class
        """
        pos_x = self.rect.x + self.width // 2
        pos_y = self.rect.y + self.height + 250
        return AirplaneBulelts([pos_x , pos_y ])
