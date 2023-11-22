import button
import settings
from button import *


def pause_menu_screen():
    """
    Arguments: None
    Application: This function is responsible for displaying the pause window during gameplay
    Return: None
    """
    paused = True
    while paused:
        current_time = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                if current_time - settings.last_esc_time >= 0.5:  # Sprawdź, czy minęła co najmniej 1 sekunda od ostatniego esc
                    settings.last_esc_time = current_time
                    paused = False
                    return paused

        screen.fill([100, 100, 100])
        pause_text = pygame.image.load("assets/pause_text.png").convert_alpha()
        screen_menu.blit(pause_text, (800, 100))
        button_start = button.Button(0, 500, start_button_img, 0.8)
        button_quit = button.Button(60, 850, exit_button_img, 0.025)

        if button_start.draw():
            paused = False
            return paused

        if button_quit.draw():
            pygame.quit()
        pygame.display.flip()

