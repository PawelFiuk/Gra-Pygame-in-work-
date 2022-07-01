from settings_file import *
import button


class Menu:
    def __init__(self):
        #main.running_game = False
        self.running_menu = True
        self.bg_menu = pygame.image.load("assets/menu_bg.png").convert_alpha()
        self.bg_menu = pygame.transform.scale(self.bg_menu, (1900, 900)).convert_alpha()
        pygame.display.set_caption("Menu")

    def draw(self):
        #screen_menu.blit(self.bg_menu, (0, 0))
        self.running_menu = True
        while self.running_menu:
            screen_menu.blit(self.bg_menu, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running_menu = False
                elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    self.running_menu = False
            screen_menu.blit(self.bg_menu, (0, 0))
            pygame.display.flip()
        pygame.quit()

    def play(self):
        pass

    def quit(self):
        pass
