from settings import  *

class MagicSnus(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        """
        Arguments: self, takes the coordinates (x: int,y: int) where the magic snus should appear on the screen when the game starts.
        Application: setting default parameters for snus, loading images etc.
        Return: None
        """
        pygame.sprite.Sprite.__init__(self)
        item_image = pygame.image.load('assets/graphics/magic_snus.png').convert_alpha()
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
        Application: method draws snus on the screen of the game
        Return: None
        """
        window.blit(self.image, (self.x, self.y))

    def action_magic_stats(self, player):
        """
        Arguments: self, player - main character of the game
        Application: method sets flags of taken snus and launches special effects
        Return: None
        """
        if not self.is_take:
            player.is_magic_snus_taken = True
            self.is_take = True

    def update_camera(self):
        """
        Arguments: self
        Application: method updates position of snus based on players position
        Return: None
        """
        self.rect.x -= scroll_position_of_player[0]
        self.x -= scroll_position_of_player[0]
