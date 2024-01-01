from settings import  *

class AmmunitionPackage(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        item_image = pygame.image.load('assets/graphics/ammo_package.jpg').convert_alpha()
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

    def action_ammo(self, player):
        if not self.is_take and not player.main_ammo_magazine == 20:
            remaining_ammo = player.max_main_ammo_magazine - player.main_ammo_magazine
            if remaining_ammo < 5:
                player.main_ammo_magazine = 20
            else:
                player.main_ammo_magazine += 5

            remaining_grenades = player.max_grenade_amount - player.current_amount_grenades
            if remaining_grenades < 3:
                player.current_amount_grenades = 5
            else:
                player.current_amount_grenades += 2
            self.is_take = True
            self.kill()


    def update_camera(self):
        self.rect.x -= scroll_position_of_player[0]
        self.x -= scroll_position_of_player[0]
