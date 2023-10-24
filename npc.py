from settings import *
import pygame
import player


class NPC:
    def __init__(self, x, y, image_source):
        pygame.sprite.Sprite.__init__(self)
        image_npc = pygame.image.load(image_source).convert_alpha()
        self.image = pygame.transform.scale(image_npc, (400, 400)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.velocity_y = 0
        self.flip = False
        self.x = x
        self.y = y
        self.dialog_active = False

    def dialog_box(self):
        self.dialog_active = not self.dialog_active

    def draw(self, window):
        self.rect.x -= scroll_position_of_player[0]
        self.x -= scroll_position_of_player[0]
        self.y -= scroll_position_of_player[1]
        window.blit(self.image, (self.x, self.y))
        if self.dialog_active:
            self.draw_dialog()

    def draw_dialog(self):
        rectangle_width, rectangle_height = 200, 100
        rectangle_x, rectangle_y = (SCREEN_WIDTH - rectangle_width) // 2, (SCREEN_HEIGHT - rectangle_height) // 2
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(rectangle_width, rectangle_height, rectangle_x, rectangle_y))
        pygame.display.flip()


