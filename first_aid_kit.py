from settings import  *

class FirstAidKit(pygame.sprite.Sprite):
    def __init__(self, x, y):
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
        if not self.is_take:
            self.draw_item(window)
            self.update_camera()
    def draw_item(self, window):
        window.blit(self.image, (self.x, self.y))

    def action_health(self, player):
        if not self.is_take and not player.current_health == player.max_health:
            remaining_health = player.max_health - player.current_health
            if remaining_health < 25:
                player.current_health = player.max_health
            else:
                player.current_health += 25
            self.is_take = True
            self.kill()


    def update_camera(self):
        self.rect.x -= scroll_position_of_player[0]
        self.x -= scroll_position_of_player[0]
