from settings import  *

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2
        self.distance_threshold = 200
        self.attack_range = 30
        self.attack_damage = 10
        self.player_seen = False
        self.current_health = 100
        self.max_health = 25
        self.health_bar_length = 300
        self.health_ratio = self.max_health / self.health_bar_length

    def update(self, player):
        self.draw()
        self.draw_health_bar()


    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0

    def draw(self, window):
        """
        Arguments: self, window - main screen for gameplay
        Application: drawing of the enemy Blue Ghost in the screen
        Return: None
        """
        self.x -= scroll_position_of_player[0]
        self.y -= scroll_position_of_player[1]
        window.blit(self.image, (self.x, self.y))

    def draw_health_bar(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.rect.x, self.rect.y - 200, self.current_health / self.health_ratio, 30))


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

    def receive_damage(self):
        pass

    def checking_is_dead_enemy(self):
        if self.current_health <= 0:
            self.is_dead = True
            return True
