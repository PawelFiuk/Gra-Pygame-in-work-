import pygame.sprite
from settings_file import *
from bullets import Bullets
import time

"""
    This class contains main functionality for player.
    
"""


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        IMAGE_AUGUSTUS = pygame.image.load('Augustus IV wersja 4.png').convert_alpha()
        self.image = pygame.transform.scale(IMAGE_AUGUSTUS, (400, 400)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.velocity_y = 0
        self.jumper = "ready"
        self.flip = False
        self.current_health = 100
        self.max_health = 100
        self.health_bar_length = 300
        self.health_ratio = self.max_health / self.health_bar_length
        self.main_ammo_magazine = 20

    def update(self):
        global tile
        change_position_x_player = 0
        change_position_y_player = 0

        # sterowanie klawiszami i szybkość poruszania się
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE] and self.jumper == "ready" or key[pygame.K_UP] and \
                self.jumper == "ready" or key[pygame.K_w] and self.jumper == "ready":
            self.velocity_y = -10
            self.jumper = "jumping"

        if key[pygame.K_a] or key[pygame.K_LEFT]:
            change_position_x_player -= 4
            self.flip = True

        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            change_position_x_player += 4
            self.flip = False

        if key[pygame.K_j]:
            self.current_health -= 20
            if self.current_health <= 0:
                self.current_health = 0

        if key[pygame.K_k]:
            self.current_health += 20
            if self.current_health >= self.max_health:
                self.current_health = self.max_health

        # dodanie grawitacji
        self.velocity_y += 0.2
        if self.velocity_y > 120:
            self.velocity_y = change_position_y_player
        change_position_y_player += self.velocity_y

        # sprawdzanie kolizji
        from main import world # import lokalny obiektu z pliku main
        for tile in world.tile_list:
            # sprawdzanie kolizji w osi x
            if tile[1].colliderect(self.rect.x + change_position_x_player, self.rect.y + change_position_y_player, self.width, self.height):
                change_position_x_player = 0

            """if player.rect.x >= background_x-100:
                background_x += 100"""

            # sprawdzanie kolizji w osi y
            if tile[1].colliderect(self.rect.x, self.rect.y + change_position_y_player, self.width, self.height):
                # sprawdz czy pod ziemia skaka
                if self.velocity_y < 0:
                    change_position_y_player = tile[1].bottom - self.rect.top
                    self.velocity_y = 0
                # sprawdz czy pod ziemia spada
                elif self.velocity_y >= 0:
                    change_position_y_player = tile[1].top - self.rect.bottom
                    self.velocity_y = 0
                    self.jumper = 'ready'

        # update koordynatów gracz
        self.rect.x += change_position_x_player
        self.rect.y += change_position_y_player
        # print(self.rect.x, self.rect.y)

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = tile[1].bottom
            self.jumper = "ready"

        # Przewijanie tła

        if self.rect.x >= resolution[0] / 2:
            x_screen = resolution[0] / 2
            self.rect.x = x_screen
            from main import world
            # world.x_cord -= change_position_x_player
            scroll_position_of_player[0] = change_position_x_player

            # self.rect.x -= change_position_x_player
        elif self.rect.x <= resolution[0] - 1800:
            x_screen_left = resolution[0] - 1800
            self.rect.x = x_screen_left
            scroll_position_of_player[0] = 0
            scroll_position_of_player[0] -= -change_position_x_player

        # else:
        #    x_screen = self.rect.x
        #    self.rect.x = x_screen

        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def health_bar(self):
        pygame.draw.rect(screen, (255, 0, 0), (10, 10, self.current_health / self.health_ratio, 30))

    def main_ammo(self):
        text = font.render(str(self.main_ammo_magazine), True, (0, 0, 0))
        screen.blit(text, (50, 50))

    def position(self):
        return [self.rect.x / 2], [self.rect.y]

    def shot_bullet(self):
        pos_x = self.rect.x
        pos_y = self.rect.y
        return Bullets([pos_x + 500, pos_y + 220])
