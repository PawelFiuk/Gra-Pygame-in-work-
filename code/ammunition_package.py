from settings import  *

class AmmunitionPackage(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        """
        Arguments: takes the coordinates (x: int,y: int) where the package should appear on the screen when the game starts.
        Application: setting default parameters for package, loading images etc.
        Return: None
        """
        pygame.sprite.Sprite.__init__(self)
        item_image = pygame.image.load('code/assets/graphics/ammo_package.png').convert_alpha()
        self.image = pygame.transform.scale(item_image, (100, 80)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.is_take = False

    def update(self, window):
        """
           Arguments: self, window - main scene for game
           Application: method calls any other methods to be called or checked in each frame of the game,
                it serves as a handle
           Return: None
        """
        if not self.is_take:
            self.draw_item(window)
            self.update_camera()
    def draw_item(self, window):
        """
           Arguments: self, window - main scene for game
           Application: draws package on screen
           Return: None
        """
        window.blit(self.image, (self.x, self.y))

    def action_ammo(self, player):
        """
           Arguments: self, player - object of player in the game
           Application: method checks amount of ammunition and grenades of player, if there is maximum amount of them
                player can't pick up a package, if something is missing, package will add an ammunition
           Return: None
        """
        if not self.is_take:
            remaining_ammo = player.max_main_ammo_magazine - player.main_ammo_magazine
            if remaining_ammo < 5:
                player.main_ammo_magazine = player.max_main_ammo_magazine
            else:
                player.main_ammo_magazine += 5

            remaining_grenades = player.max_grenade_amount - player.current_amount_grenades
            if remaining_grenades < 3:
                player.current_amount_grenades = player.max_grenade_amount
            else:
                player.current_amount_grenades += 2
            self.is_take = True
            self.kill()


    def update_camera(self):
        """
            Arguments: self
            Application: updates the display of the package and the world based
                on the player's movement.
            Return: None
        """
        self.rect.x -= scroll_position_of_player[0]
        self.x -= scroll_position_of_player[0]
