from settings import *
import button


def draw_gameover_menu():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                paused = False
                return paused

        screen.fill([90, 90, 90])
        gameover_image = pygame.image.load("assets/graphics/gameover_background.png").convert_alpha()
        gameover_scaled_image = pygame.transform.scale(gameover_image, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
        screen_menu.blit(gameover_scaled_image, (0, 0))
        button_quit = button.Button(60, 700, exit_button_img, 0.025)


        if button_quit.draw():
            pygame.quit()
        pygame.display.flip()