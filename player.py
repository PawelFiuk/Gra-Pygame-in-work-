import pygame.sprite
from settings import *
from bullets import Bullets
import time

"""
    This class contains main functionality for player.    
    
"""


class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        """
        Arguments: takes the coordinates (x: int,y: int) where the player should appear on the screen when the game starts.
        Application: setting default parameters for player, loading images etc.
        Return: None
        """
        pygame.sprite.Sprite.__init__(self)
        image_augustus = pygame.image.load('assets/graphics/augustus/SteamMan.png').convert_alpha()
        self.image = pygame.transform.scale(image_augustus, (400, 400)).convert_alpha()
        self.image_idle = pygame.transform.scale(image_augustus, (400, 400)).convert_alpha()
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
        self.max_main_ammo_magazine = 20
        self.falling = True
        self.change_position_x_player = 0
        self.change_position_y_player = 0
        self.ground_collision = False

        self.is_jumping = False
        self.jump_start_time = 0
        self.last_idle_animation_time = time.time()
        self.idle_animation_triggered = False

        # Load the sprite sheet with animation frames
        self.movement_sprite_sheet = pygame.image.load('assets/graphics/augustus/SteamMan_run.png').convert_alpha()
        self.idle_sprite_sheet = pygame.image.load('assets/graphics/augustus/SteamMan.png').convert_alpha()
        self.jump_sprite_sheet = pygame.image.load('assets/graphics/augustus/SteamMan_jump.png').convert_alpha()

        self.frame_width = self.movement_sprite_sheet.get_width() // 6  # Assuming 6 frames in a row
        self.frame_height = self.movement_sprite_sheet.get_height()
        self.last_walk_animation_time = pygame.time.get_ticks()

        self.animation_frames = {
            'idle': [pygame.transform.scale(
                self.idle_sprite_sheet.subsurface((i * self.frame_width, 0, self.frame_width, self.frame_height)),
                (400, 400)) for i in range(1)],
            'walk': [pygame.transform.scale(
                self.movement_sprite_sheet.subsurface((i * self.frame_width, 0, self.frame_width, self.frame_height)),
                (400, 400)) for i in range(6)],
            'jump': [pygame.transform.scale(
                self.jump_sprite_sheet.subsurface((i * self.frame_width, 0, self.frame_width, self.frame_height)),
                (400, 400)) for i in range(6)],
            'dead': [pygame.transform.scale(
                self.jump_sprite_sheet.subsurface((i * self.frame_width, 0, self.frame_width, self.frame_height)),
                (400, 400)) for i in range(6)],
        }

        self.current_animation = 'idle'  # Default animation
        self.current_frame = 0  # Current frame index
        #self.animation_speed = 100000  # Adjust the speed as needed

        self.image = self.animation_frames[self.current_animation][self.current_frame]

    def update(self):
        self.draw()
        self.handle_movement()
        self.animate()
        self.apply_gravity()
        self.check_collisions()
        self.update_camera()
        self.checking_is_dead_player()
        self.health_bar()
        self.main_ammo()

    def handle_movement(self):
        key = pygame.key.get_pressed()

        self.change_position_x_player = 0
        self.change_position_y_player = 0

        if key[pygame.K_a]:
            self.change_position_x_player -= 4
            self.flip = True
            self.current_animation = 'walk'
            if self.change_position_x_player != 0:
                self.animate()

        elif key[pygame.K_d]:

            self.change_position_x_player += 4

            self.flip = False

            if self.change_position_x_player != 0:
                current_time_for_animation = pygame.time.get_ticks()
                if current_time_for_animation - self.last_walk_animation_time > 100:  # 200 milisekund (0.2 sekundy)
                    self.last_walk_animation_time = current_time_for_animation
                    self.animate()

        elif key[pygame.K_SPACE] and self.jumper == "ready" or key[
            pygame.K_w] and self.jumper == "ready":
            self.velocity_y = -10
            self.jumper = "jumping"
            self.ground_collision = False
            self.is_jumping = True
            self.jump_start_time = time.time()
            self.current_animation = 'jump'
            self.animate()

        if key[pygame.K_j]:
            self.current_health -= 1
            self.current_health = max(self.current_health, 0)

        if key[pygame.K_k]:
            self.current_health += 1
            self.current_health = min(self.current_health, self.max_health)

        # Update the idle animation only once every 10 seconds
        if self.change_position_x_player == 0 and not (key[pygame.K_SPACE] or key[pygame.K_UP] or key[pygame.K_w]):
            self.current_animation = 'idle'
            self.animate_idle()

    def apply_gravity(self):
        if self.falling:
            self.velocity_y += 0.2

        if self.velocity_y == -10:
            self.falling = True

        self.change_position_y_player += self.velocity_y

    def check_collisions(self):
        from main import world
        for tile in world.tile_list:
            if tile[1].colliderect(self.rect.x + self.change_position_x_player,
                                   self.rect.y + self.change_position_y_player, self.width, self.height):
                self.change_position_x_player = 0

            if tile[1].colliderect(self.rect.x, self.rect.y + self.change_position_y_player, self.width, self.height):
                self.change_position_y_player = tile[1].top - self.rect.bottom
                self.velocity_y = 0
                self.jumper = 'ready'
                self.falling = False
                self.ground_collision = True
                self.is_jumping = False
                scroll_position_of_player[1] = 0
                self.change_position_y_player = 0

            # else:
            #    self.apply_gravity()

    def update_camera(self):
        """
        Arguments: self
        Application: updates the display of the player and the world based
            on the player's movement.
        Return: None
        """
        self.rect.x += self.change_position_x_player
        self.rect.y += self.change_position_y_player

        # Update scrolling for X axis
        if self.rect.x >= resolution[0] / 2:
            x_screen = resolution[0] / 2
            self.rect.x = x_screen
            scroll_position_of_player[0] = self.change_position_x_player

        elif self.rect.x <= resolution[0] - 1800:
            x_screen_left = resolution[0] - 1800
            self.rect.x = x_screen_left
            scroll_position_of_player[0] = self.change_position_x_player
        else:
            scroll_position_of_player[0] = 0

        # Update scrolling for Y axis
        scroll_position_of_player[1] = self.change_position_y_player

    def draw(self):
        """
        Arguments: self
        Application: draws the player's character in the game window, after each frame.
        Return: None
        """
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def health_bar(self):
        """
        Arguments: self
        Application: draws a bar with the player's HP number in the upper left corner of the screen
        Return: None
        """
        pygame.draw.rect(screen, (255, 0, 0), (10, 10, self.current_health / self.health_ratio, 30))

    def main_ammo(self):
        """
        Arguments: self
        Application: draws a bar with the player's HP number in the upper left corner of the screen
        Return: None
        """
        text = font.render(str(self.main_ammo_magazine), True, (0, 0, 0))
        screen.blit(text, (50, 50))

    def shot_bullet(self):
        """
        Arguments: self
        Application: This method is used to create a new class of projectile that will be fired after
            a specific game event. Supports shooting from two sides, when the player is turned and when he is not.
        Return: Bullets class
        """
        if not self.flip:
            pos_x = self.rect.x
            pos_y = self.rect.y
            return Bullets([pos_x + 460, pos_y + 220], False)

        if self.flip:
            pos_x = self.rect.x
            pos_y = self.rect.y
            return Bullets([pos_x + 115, pos_y + 220], True)

    def checking_is_dead_player(self):
        if self.current_health <= 0:
            self.current_animation = 'dead'
            return True

    def animate(self):
        if self.is_jumping:
            elapsed_time = time.time() - self.jump_start_time
            jump_animation_speed = 6  # Dopasuj szybkość animacji skoku
            jump_frame_index = int(elapsed_time * jump_animation_speed) % len(self.animation_frames['jump'])
            self.image = self.animation_frames['jump'][jump_frame_index]
            if self.is_jumping and (jump_frame_index == 3):
                self.image = self.animation_frames['jump'][3]
        else:
            self.current_frame = (self.current_frame + 1) % len(self.animation_frames[self.current_animation])
            self.image = self.animation_frames[self.current_animation][self.current_frame]

    def animate_idle(self):
        # Update the current frame based on the animation speed
        self.current_frame = (self.current_frame + 1) % len(self.animation_frames[self.current_animation])
        self.image = self.animation_frames[self.current_animation][self.current_frame]

    def event(self):
        pass

