

from settings_file import *


class Bullets(pygame.sprite.Sprite):
    def __int__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.bullet_image = pygame.image.load('assets/bullet.png').convert_alpha()
        self.image = pygame.transform.scale(self.bullet_image, (100, 40)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x_pos  # Wybieramy lokalizacje gdzie pojawi się postać
        self.rect.y = y_pos
        self.rect.center = (x_pos, y_pos)
        #self.direction = direction
        #self.velocity_of_bullet = 5
        #self.rect = self.bullet_image.get_rect(center=(x_pos, y_pos))

    def update(self):
        self.rect.x += 5

    def draw(self, window):
        window.blit(self.bullet_image, (self.rect.x, self.rect.y))

