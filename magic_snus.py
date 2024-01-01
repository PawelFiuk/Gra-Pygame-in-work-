from settings import  *

class MagicSnus():
    def __init__(self, x, y):
        #pygame.sprite.Sprite.__init__(self)
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
        if not self.is_take:
            self.draw_item(window)
            self.update_camera()

    def draw_item(self, window):
        window.blit(self.image, (self.x, self.y))

    def action_magic_stats(self, player):
        if not self.is_take:
            player.is_magic_snus_taken = True
            self.is_take = True

    def update_camera(self):
        self.rect.x -= scroll_position_of_player[0]
        self.x -= scroll_position_of_player[0]
