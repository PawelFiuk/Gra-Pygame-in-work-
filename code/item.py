from settings import *

class Item:
    def __init__(self, x: int, y: int, convert_x, convert_y, name, image_source):
        """
        Arguments: takes the coordinates (x: int,y: int) where the item should appear on the screen when the game starts.
        Application: setting default parameters for player, loading images etc.
        Return: None
        """
        self.image = pygame.image.load(image_source).convert_alpha()
        self.image = pygame.transform.scale(self.image, (convert_x, convert_y)).convert_alpha()
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.taken = False
        self.position_in_inventory = 0

class ItemData(Item):
    def __init__(self):
        pass

items = {
  "metal_gear": 'assets/graphics/items/metal_gear_scrap.png',
}