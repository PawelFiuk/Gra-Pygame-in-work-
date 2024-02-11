from settings import *

class Item:
    def __init__(self, x: int, y: int, image, convert_x, convert_y):
        """
        Arguments: takes the coordinates (x: int,y: int) where the player should appear on the screen when the game starts.
        Application: setting default parameters for player, loading images etc.
        Return: None
        """
        image = pygame.image.load('assets/graphics/augustus/SteamMan.png').convert_alpha()
        self.image = pygame.transform.scale(image, (convert_x, convert_y)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.velocity_y = 0