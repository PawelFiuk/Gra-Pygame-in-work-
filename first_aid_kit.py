from settings import  *

class FirstAidKit(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        """
        Arguments: self, position - x and y position where Aid Kit should be placed
        Application: setting the basic parameters of the Aid Kit
        Return: None
        """
        pygame.sprite.Sprite.__init__(self)
        item_image = pygame.image.load('assets/graphics/first_aid_kit.png').convert_alpha()
        self.image = pygame.transform.scale(item_image, (100, 80)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.is_take = False

    def update_package(self, window):
        """
           Arguments: self, window - main scene of the game
           Application: method calls any other methods to be called or checked in each frame of the game,
                it serves as a handle
           Return: None
        """
        if not self.is_take:
            self.draw_item(window)
            self.update_camera()
    def draw_item(self, window):
        """
           Arguments: self, window - main scene of the game
           Application: method draws First Aid Kit in the game
           Return: None
        """
        window.blit(self.image, (self.x, self.y))

    def action_health(self, player):
        """
           Arguments: self, player - object of the main character in game
           Application: method is checking current health of the player, if its not full, First Aid Kit will
                restores health by a certain amount
           Return: None
        """
        if not self.is_take and not player.current_health == player.max_health:
            remaining_health = player.max_health - player.current_health
            if remaining_health < 25:
                player.current_health = player.max_health
            else:
                player.current_health += 25
            self.is_take = True
            self.kill()


    def update_camera(self):
        """
           Arguments: self
           Application: method is updates position of First Aid Kit on the screen based on players movement
           Return: None
        """
        self.rect.x -= scroll_position_of_player[0]
        self.x -= scroll_position_of_player[0]
