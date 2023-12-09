from settings import *
import pygame

class Item:
    def __init__(self, x: int, y: int, name: str):
        item_image = pygame.image.load('assets/graphics/augustus/Augustus_IV.png').convert_alpha()
        self.image = pygame.transform.scale(item_image, (75, 50)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.name_of_item = name

    def draw_item(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def action_of_item(self):
        pass


items: dict[str, Item] = {
    'ammunitionPackage':Item(),
    'snus':Item(),
    'hpPotion':Item(),
}

