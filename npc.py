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
                            "ESC to pauza")  # Twój tekst dialogu
        self.dialog_active = False
        self.last_dialog_time = 0
        self.current_display_text = ""
        self.font = pygame.font.Font(None, 35)

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

        rectangle_width, rectangle_height = 500, 300
        rectangle_x, rectangle_y = (SCREEN_WIDTH - rectangle_width) // 2, (SCREEN_HEIGHT - rectangle_height) // 2
        pygame.draw.rect(window, (0, 0, 0), pygame.Rect(rectangle_x, rectangle_y, rectangle_width, rectangle_height))

        # Podziel tekst na linie
        lines = self.wrap_text(self.dialog_text, self.font, rectangle_width)

        # Renderuj każdą linię tekstu
        for i, line in enumerate(lines):
            text_surface = self.font.render(line, True, (255, 255, 255))
            text_rect = text_surface.get_rect(
                center=(rectangle_x + rectangle_width // 2, rectangle_y + rectangle_height // 2 + i * 20))

            # Wyświetl renderowany tekst
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
