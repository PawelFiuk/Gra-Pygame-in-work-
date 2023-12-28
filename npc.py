from settings import *
import pygame
import time



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
        self.dialog_text = ("Augustus, pozwól że pomogę ci się stąd wydostać! "
                            "Kierujesz WSAD, strzelasz C, interakcja z obiektami E, "
                            "ESC to pauza")
        self.dialog_active = False
        self.last_dialog_time = 0
        self.current_display_text = ""
        self.dialog_box_image = pygame.image.load("assets/graphics/dialog_box_icon.png").convert_alpha()

        self.last_dialog_time = 0

    def update(self, window):
        self.update_camera()
        self.draw(window)

    def dialog_box(self):
        """

        :return:
        """
        current_time = time.time()
        if current_time - self.last_dialog_time >= 1:
            self.dialog_active = not self.dialog_active
            self.last_dialog_time = current_time
            if self.dialog_active:
                self.current_display_text = ""

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        if self.dialog_active:
            self.draw_dialog(window)

    def update_camera(self):
        self.rect.x -= scroll_position_of_player[0]
        self.x -= scroll_position_of_player[0]

    def draw_dialog(self, window):

        obraz_x, obraz_y = 500, 50
        window.blit(self.dialog_box_image, (obraz_x, obraz_y))
        box_dialogue_width, box_dialogue_height = self.dialog_box_image.get_size()
        lines = self.wrap_text(self.dialog_text, font_for_dialogs, box_dialogue_width)

        for i, line in enumerate(lines):
            text_surface = font_for_dialogs.render(line, True, (255, 255, 255))
            text_rect = text_surface.get_rect(
                center=(obraz_x + box_dialogue_width // 2, obraz_y + box_dialogue_height // 2 + i * 20))
            window.blit(text_surface, text_rect)

    def wrap_text(self, text, font, max_width):
        words = text.split()
        lines = []
        current_line = words[0]

        for word in words[1:]:
            test_line = current_line + " " + word
            width, _ = font.size(test_line)

            if width <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word

        lines.append(current_line)
        return lines


class NPC2(NPC):
    def __init__(self, x, y, image_source):
        super().__init__(x, y, image_source)
        self.dialog_text = ("To jest statek powietrzny którym sie stad wydostasz! "
                            "Kierujesz WSAD, strzelasz C, interakcja z obiektami E, "
                            "zestrzel wszystkie beczki!")
