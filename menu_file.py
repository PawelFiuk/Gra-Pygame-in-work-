from settings_file import *
import button
from pygame import mixer


class Menu:
    def __init__(self):
        #main.running_game = False
        self.bg_menu = pygame.image.load("assets/menu_bg.png").convert_alpha()
        self.bg_menu = pygame.transform.scale(self.bg_menu, (1900, 900)).convert_alpha()
        pygame.display.set_caption("Obsesion")
        mixer.music.load("assets/Phonothek_Red_Moon.mp3")
        mixer.music.play(-1)

    def draw(self):
        #screen_menu.blit(self.bg_menu, (0, 0))
        self.running_menu = True
        from main import button_start, button_quit
        while self.running_menu:
            screen_menu.blit(self.bg_menu, (0, 0))
            button_start.draw()
            button_quit.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running_menu = False
                elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    self.running_menu = False

            if button_quit.draw():
                self.running_menu = False
                pygame.quit()
                break

            if button_start.draw():
                self.running_menu = False
                import main
                main.running_menu = True
                pygame.quit()
                break

            pygame.display.flip()
        pygame.quit()

