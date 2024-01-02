import pygame.sprite
from settings import *
from bullets import Bullets, Grenade
import time
import physics
from pygame.mask import from_surface

"""
    This class contains main functionality for player.    
    
"""


class Player(pygame.sprite.Sprite, physics.Physics):
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
        self.falling = True
        self.change_position_x_player = 0
        self.change_position_y_player = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.ground_collision = False
        self.experience_levels = {1: 20, 2: 50, 3: 75, 4: 100, 5:150, 6:200, 7:250}
        self.experience_bar_color = (255, 215, 0)  # Gold color for the XP bar
        self.health_bar_length = 300
        self.max_health = 100
        self.health_ratio = self.max_health / self.health_bar_length
        self.is_jumping = False
        self.airplane_mode = False
        self.mask = from_surface(self.image)
        self.is_magic_snus_taken = False
        self.missing_health_bar_colour = (255, 0, 0) # Red colour for normal health bar
        self.health_bar_colour_normal = (0, 255, 0)
        self.health_bar_colour_snus_effect = [0, 0, 255] # Blue colour got snus health bar
        self.actual_health_bar = self.health_bar_colour_normal
        self.invincibility_time = 0
        self.is_invincible = False



        #stats
        self.current_health = 100
        self.max_health = 100
        self.level = 1
        self.ability_points = 0
        self.experience = 0
        self.main_ammo_magazine = 20
        self.max_main_ammo_magazine = 20
        self.max_grenade_amount = 5
        self.current_amount_grenades = 5

        #animation
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
        self.current_frame = 0
        self.image = self.animation_frames[self.current_animation][self.current_frame]


    def update(self, world):
        """
           Arguments: self, world - world is an instance of the World object that generates the entire game world
           Application: method calls any other methods to be called or checked in each frame of the game,
                it serves as a handle
           Return: None
        """
        self.draw()
        self.handle_movement()
        self.animate()
        self.apply_gravity()
        self.check_collisions(world)
        self.update_camera()
        self.checking_is_dead_player()
        self.health_bar()
        self.show_main_ammo()
        self.draw_experience_bar(screen)
        self.update_mask()
        self.message_about_avalaible_ability_points()

    def handle_movement(self):
        """
           Arguments: self
           Application: the method checks whether the keys responsible for walking or other activities such as shooting
                or interacting with the environment have been pressed
           Return: None
        """
        key = pygame.key.get_pressed()

        self.change_position_x_player = 0
        self.change_position_y_player = 0

        if key[pygame.K_a]:
            self.change_position_x_player -= 8
            self.flip = True
            self.current_animation = 'walk'
            if self.change_position_x_player != 0:
                self.animate()

        elif key[pygame.K_d]:
            self.change_position_x_player += 8
            self.flip = False
            self.current_animation = 'walk'
            if self.change_position_x_player != 0:
                current_time_for_animation = pygame.time.get_ticks()
                if current_time_for_animation - self.last_walk_animation_time > 300:
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

        if (
            self.change_position_x_player == 0
            and not (key[pygame.K_SPACE] or key[pygame.K_w])
            ):
                self.current_animation = 'idle'
                self.animate_idle()

    def apply_gravity(self):
        """
            Arguments: self
            Application: the method refers to the Physics class, which is responsible
                for implementing gravity for the player
            Return: None
        """
        physics.Physics.apply_gravity(self)

    def check_collisions(self, world):
        """
           Arguments: self
           Application: checks collisions of the player with tiles from world
           Return: None
        """
        physics.Physics.check_collision(self, world)

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
        if not self.airplane_mode:
            empty_surface = pygame.Surface((400, 400), pygame.SRCALPHA)
            screen.blit(empty_surface, self.rect.topleft)
            screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def update_mask(self):
        self.mask = pygame.mask.from_surface(self.image)

    def health_bar(self):
        """
        Arguments: self
        Application: draws a bar with the player's HP number in the upper left corner of the screen
        Return: None
        """
        health_bar_width = 300  # Adjust the width of the health bar as needed
        health_bar_height = 30

        pygame.draw.rect(screen, self.missing_health_bar_colour, [10, 10, health_bar_width, health_bar_height])
        if not self.is_magic_snus_taken:
            pygame.draw.rect(screen, self.health_bar_colour_normal,
                             [10, 10, (self.current_health / self.max_health) * health_bar_width, health_bar_height])
        if self.is_magic_snus_taken:
            pygame.draw.rect(screen, self.health_bar_colour_snus_effect,
                             [10, 10, (self.current_health / self.max_health) * health_bar_width, health_bar_height])

    def show_main_ammo(self):
        """
        Arguments: self
        Application: draws a players number of main ammo in the upper left corner of the screen
        Return: None
        """
        text = font.render(str(self.main_ammo_magazine), True, (0, 0, 0))
        screen.blit(text, (50, 50))
        text_number_of_grenades = font.render(str(self.current_amount_grenades), True, (0, 0, 0))
        screen.blit(text_number_of_grenades, (50, 110))

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
        """
        Arguments: self
        Application: the method checks whether the player's health has dropped below zero,
            if so the return value is true
        Return: boolean True
        """
        if self.current_health <= 0:
            self.current_animation = 'dead'
            return True

    def animate(self):
        """
        Arguments: self
        Application: the method is responsible for turning on the appropriate animation for a given
            type of movement (like jumping, walking)
        Return: none
        """
        if self.is_jumping:
            elapsed_time = time.time() - self.jump_start_time
            jump_animation_speed = 8
            jump_frame_index = int(elapsed_time * jump_animation_speed) % len(self.animation_frames['jump'])
            self.image = self.animation_frames['jump'][jump_frame_index]
            if self.is_jumping and (jump_frame_index == 3):
                self.image = self.animation_frames['jump'][3]

        else:
            current_time = pygame.time.get_ticks()
            if self.current_animation == 'walk':
                animation_speed = 85
                if current_time - self.last_walk_animation_time > animation_speed:
                    self.last_walk_animation_time = current_time
                    self.current_frame = (self.current_frame + 1) % len(self.animation_frames[self.current_animation])
                    self.image = self.animation_frames[self.current_animation][self.current_frame]
            else:
                self.current_frame = (self.current_frame + 1) % len(self.animation_frames[self.current_animation])
                self.image = self.animation_frames[self.current_animation][self.current_frame]

    def animate_idle(self):
        """
        Arguments: self
        Application: the method is responsible for turning on the appropriate animation for a idle state
        Return: none
        """
        current_time = pygame.time.get_ticks()
        if self.current_animation == 'idle':
            animation_speed = 800
            if current_time - self.last_walk_animation_time > animation_speed:
                self.last_walk_animation_time = current_time
                self.current_frame = (self.current_frame + 1) % len(self.animation_frames[self.current_animation])
                self.image = self.animation_frames[self.current_animation][self.current_frame]

    def enter_airplane_mode(self):
        """
        Arguments: self
        Application: the method is responsible for activating the aircraft movement mode
        Return: none
        """
        self.airplane_mode = True

    def exit_airplane_mode(self, position_x, position_y):
        """
        Arguments: self, position_x, position_y - positions are equall to positions of rectangle of airplane,
        Application: the method is responsible for turning off the aircraft movement mode, with positions of airplane
            player can be respawned in place where airplane stops after exiting, self.airplane_mode is setting to False
            and player can be rendered again.
        Return: none
        """
        self.airplane_mode = False
        self.rect.x = position_x
        self.rect.y = position_y

    def gain_experience(self, points):
        """
        Arguments: self
        Application: the method adds all the experience points that the player has gained and checks whether
            a new level has been reached. If so, the level_up() method is called
        Return: none
        """
        self.experience += points

        if self.level < len(self.experience_levels) and self.experience >= self.experience_levels[self.level]:
            self.level_up()

    def level_up(self):
        """
        Arguments: self
        Application: the method is responsible for adding skill points when advancing to a new level
            and transferring the remaining experience points to a new level
        Return: none
        """
        temp_exp = self.experience -  self.experience_levels[self.level]
        self.level += 1
        self.ability_points += 2
        self.experience = temp_exp

    def message_about_avalaible_ability_points(self):
        if self.ability_points > 0:
            message_about_abilit_points =f"Awansowałeś! Masz {self.ability_points} punktów umiejętności, wciśnij r, żeby otworzyć drzewko umiejętności!"
            text_level = font_for_ability_message.render(message_about_abilit_points, True, (255, 255, 255))
            screen.blit(text_level, (1050, 10))


    def draw_experience_bar(self, screen):
        """
         Arguments: self, screeen - screen is instance of main window of game
         Application: the method is responsible for drawing experience bar on screen, on right sight of health bar,
            colour of experience bar is gold.
         Return: none
         """
        xp_bar_max_width = 300
        xp_bar_width = 300
        xp_bar_height = 30
        xp_percentage = (self.experience / self.experience_levels[self.level]) * xp_bar_max_width

        pygame.draw.rect(screen, (255, 255, 255),
                         [350, 10, xp_bar_width, xp_bar_height])
        pygame.draw.rect(screen, self.experience_bar_color,
                         [350, 10, xp_percentage, xp_bar_height])
        level = "   Level "
        text_level = font.render(str(self.level) + level, True, (255, 255, 255))
        screen.blit(text_level, (750, 10))

    def snus_special_effect(self):
        if self.is_magic_snus_taken:
            self.actual_health_bar = self.health_bar_colour_snus_effect
            self.current_health = self.max_health
            self.main_ammo_magazine = self.max_main_ammo_magazine
            self.current_amount_grenades = self.max_grenade_amount

    def throw_grenade(self):
        if not self.flip:
            pos_x = self.rect.x
            pos_y = self.rect.y
            return Grenade([pos_x + 460, pos_y + 220], False)

        if self.flip:
            pos_x = self.rect.x
            pos_y = self.rect.y
            return Grenade([pos_x +460, pos_y + 220], True)