import bullets
import player_file, world_file, enemy, button, new_menu_file
from settings_file import *


# Inicjalizacja gry
pygame.init()


running_game = False
running_menu = True

#grupy


# Główna linia gry
while running_menu:
    menu_init = new_menu_file.Menu()
    menu_init.draw()

    if menu_init.draw():
        world = world_file.World(world_data)
        player = player_file.Player(100, SCREEN_HEIGHT - 600)
        enemy_1 = enemy.EnemyBlueGhost(700, SCREEN_HEIGHT - 600)
        bullet_groups = pygame.sprite.Group()
        running_game = True
        key = pygame.key.get_pressed()
        #kulka  = bullets.Bullets(10, 10)
        #print(kulka)
        while running_game:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running_game = False
                    running_menu = False
                elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    running_game = False
                    running_menu = False
            if pygame.key.get_pressed()[pygame.K_c]:

                bullet_groups.add(player.shot_bullet())

            CLOCK.tick(FPS)
            world.draw()

            #bullet_groups.update()
            player.update()
            player.draw()
            #bullet_groups.draw(screen)
            player.health_bar()
            enemy_1.draw(screen)
            play_menu_theme_music = False
            pygame.display.flip()

