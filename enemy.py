from settings import  *
import math


class EnemyBlueGhost(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """
        Arguments: self, position - x and y position where Enemy should be placed
        Application: setting the basic parameters of the enemy Blue Ghost
        Return: None
        """
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        blue_ghost_img = pygame.image.load("assets/enemy/enemy_1.png").convert_alpha()
        self.image = pygame.transform.scale(blue_ghost_img, (400, 400)).convert_alpha()
        self.atack_area = 150
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.current_health = 25
        self.max_health = 25
        self.health_bar_length = 200
        self.health_ratio = self.max_health / self.health_bar_length
        self.is_dead = False
        self.exp_for_player = 10


    def update(self):
        if not self.is_dead:
            self.draw()
            self.draw_health_bar()

    def draw(self):
        """
        Arguments: self, window - main screen for gameplay
        Application: drawing of the enemy Blue Ghost in the screen
        Return: None
        """
        self.rect.x -= scroll_position_of_player[0]
        #self.rect.y -= scroll_position_of_player[1]
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def draw_health_bar(self):
        pygame.draw.rect(screen, (255, 0, 0), (int(self.rect.x) + 90, int(self.rect.y) - 40 , self.current_health / self.health_ratio, 30))

    def atack_player(self, position_of_player):
        if self.rect.x - position_of_player < 300:
            return True

    def checking_is_dead_enemy(self):
        if self.current_health <= 0:
            self.is_dead = True
            return True


class EnemySteamMachine(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """
        Arguments: self, position - x and y position where Enemy should be placed
        Application: setting the basic parameters of the enemy Blue Ghost
        Return: None
        """
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        mech_img = pygame.image.load("assets/graphics/mech/Mech_walk.png").convert_alpha()
        self.image = pygame.transform.scale(mech_img, (400, 400)).convert_alpha()
        self.atack_area = 150
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.current_health = 50
        self.max_health = 50
        self.health_bar_length = 200
        self.health_ratio = self.max_health / self.health_bar_length
        self.is_dead = False
        self.atack_player_flag = False
        self.ground_collision = False
        self.flip = False

        self.movement_sprite_sheet = pygame.image.load('assets/graphics/mech/Mech_walk.png').convert_alpha()

        self.fight_1_sprite_sheet = pygame.image.load('assets/graphics/mech/Mech_attack1.png').convert_alpha()
        self.hurt_sprite_sheet = pygame.image.load('assets/graphics/mech/Mech_hurt.png').convert_alpha()

        self.frame_width = self.movement_sprite_sheet.get_width() // 6
        self.frame_height = self.movement_sprite_sheet.get_height()
        self.last_walk_animation_time = pygame.time.get_ticks()
        self.last_attack_animation_time = pygame.time.get_ticks()
        self.falling = True
        self.velocity_y = 0
        self.change_position_x_mech = 0
        self.change_position_y_mech = 0
        self.send_damage_to_player_flag = False
        self.animation_hurt_play_count = 0
        self.exp_for_player = 15

        self.animation_frames = {
            'fight': [pygame.transform.scale(
                self.fight_1_sprite_sheet.subsurface((i * self.frame_width, 0, self.frame_width, self.frame_height)),
                (400, 400)) for i in range(6)],
            'walk': [pygame.transform.scale(
                self.movement_sprite_sheet.subsurface((i * self.frame_width, 0, self.frame_width, self.frame_height)),
                (400, 400)) for i in range(6)],
            'hurt': [pygame.transform.scale(
                self.hurt_sprite_sheet.subsurface((i * self.frame_width, 0, self.frame_width, self.frame_height)),
                (400, 400)) for i in range(2)],
        }

        self.current_animation = 'walk'  # Default animation
        self.current_frame = 0  # Current frame index
        self.image = self.animation_frames[self.current_animation][self.current_frame]



    def update(self, position_x_player, player_health):
        if not self.is_dead:
            self.draw()
            self.draw_health_bar()
            self.apply_gravity()
            self.check_collisions()
            self.update_camera()
            self.animate()
            self.atack_player(position_x_player)
            if self.atack_player_flag:
                self.check_is_player_visible(position_x_player)
                self.attack_animation(player_health)


    def draw(self):
        """
        Arguments: self, window - main screen for gameplay
        Application: drawing of the enemy Steam Mech in the screen
        Return: None
        """
        self.rect.x -= scroll_position_of_player[0]
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def draw_health_bar(self):
        pygame.draw.rect(screen, (255, 0, 0), (int(self.rect.x) + 90, int(self.rect.y) - 40 , self.current_health / self.health_ratio, 30))

    def atack_player(self, position_of_player):
        if self.rect.x - position_of_player < 700:
            self.atack_player_flag = True

        else:
            self.atack_player_flag = False

    def checking_is_dead_enemy(self):
        if self.current_health <= 0:
            self.is_dead = True
            return True

    def animate(self):
        current_time = pygame.time.get_ticks()
        if self.current_animation == 'walk':
            animation_speed = 120
            if current_time - self.last_walk_animation_time > animation_speed:
                self.last_walk_animation_time = current_time
                self.current_frame = (self.current_frame + 1) % len(self.animation_frames[self.current_animation])
                self.image = self.animation_frames[self.current_animation][self.current_frame]

    def check_is_player_visible(self, player_rect):
        distance_to_player = abs(self.rect.x - player_rect)

        if distance_to_player < 900:
            if self.rect.x < player_rect:
                self.rect.x += 4.5
                self.flip = False
            elif self.rect.x > player_rect:
                self.rect.x -= 4.5
                self.flip = True
        else:
            self.atack_player_flag = False

    def apply_gravity(self):
        if self.falling:
            self.velocity_y += 0.2

        self.change_position_y_mech += self.velocity_y

    def check_collisions(self):
        from main import world
        for tile in world.tile_list:
            if tile[1].colliderect(self.rect.x + self.change_position_x_mech,
                                   self.rect.y + self.change_position_y_mech, self.width, self.height):
                self.change_position_x_mech = 0

            if tile[1].colliderect(self.rect.x, self.rect.y + self.change_position_y_mech, self.width, self.height):
                self.change_position_y_mech = tile[1].top - self.rect.bottom
                self.velocity_y = 0
                self.falling = False
                self.ground_collision = True
                self.change_position_y_mech = 0
                self.rect.y += self.change_position_y_mech

    def update_camera(self):
        """
        Arguments: self
        Application: updates the display of the enemy and the world based
            on the enemy movement.
        Return: None
        """
        self.rect.x += self.change_position_x_mech
        self.rect.y += self.change_position_y_mech

    def attack_animation(self, player_health):
        """
        Arguments: self
        Application: Plays the attack animation.
        Return: None
        """
        current_time = pygame.time.get_ticks()
        attack_animation_speed = 120  # Prędkość animacji ataku
        attack_cooldown = 2000  # Czas odnowienia ataku w milisekundach (4 sekundy)

        if current_time - self.last_attack_animation_time > attack_cooldown:
                self.last_attack_animation_time = current_time
                self.current_animation = 'fight'

        if self.current_animation == 'fight':
            if current_time - self.last_attack_animation_time > attack_animation_speed:
                self.last_attack_animation_time = current_time
                self.current_frame = (self.current_frame + 1) % len(self.animation_frames[self.current_animation])
                self.image = self.animation_frames[self.current_animation][self.current_frame]
                # Dodaj kod obsługujący efekty ataku (np. zadawanie obrażeń graczowi)
                self.send_damage_to_player_flag = True
            if self.current_frame == 5 :
                self.send_damage_to_player_flag = False
                self.current_animation = 'walk'
                self.current_frame = 0

    def received_damage_animation(self):
        current_time = pygame.time.get_ticks()
        previous_animation = self.current_animation

        self.current_animation = 'hurt'
        if self.current_animation == 'hurt':
            animation_speed = 50
            if current_time - self.last_walk_animation_time > animation_speed:
                self.last_walk_animation_time = current_time
                self.current_frame = (self.current_frame + 1) % len(self.animation_frames[self.current_animation])
                self.image = self.animation_frames[self.current_animation][self.current_frame]
                self.current_animation = previous_animation


class EnemyStaticMech(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """
        Arguments: self, position - x and y position where Enemy should be placed
        Application: setting the basic parameters of the enemy Blue Ghost
        Return: None
        """
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.mech_static_img = pygame.image.load("assets/enemy/Mech_static.png").convert_alpha()
        self.image = pygame.transform.scale(self.mech_static_img, (80, 80)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.current_health = 25
        self.max_health = 25
        self.health_bar_length = 150
        self.health_ratio = self.max_health / self.health_bar_length
        self.is_dead = False
        self.exp_for_player = 5


    def update(self):
        if not self.is_dead:
            self.draw()
            self.draw_health_bar()

    def draw(self):
        """
        Arguments: self, window - main screen for gameplay
        Application: drawing of the enemy Blue Ghost in the screen
        Return: None
        """
        self.rect.x -= scroll_position_of_player[0]
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def draw_health_bar(self):
        pygame.draw.rect(screen, (255, 0, 0), (int(self.rect.x) -50, int(self.rect.y) - 40 , self.current_health / self.health_ratio, 30))


    def checking_is_dead_enemy(self):
        if self.current_health <= 0:
            self.is_dead = True
            return True
