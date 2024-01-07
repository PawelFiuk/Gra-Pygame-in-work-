import pygame
import settings
from settings import *
import button
import UI


class SkillTree:
    def __init__(self, player):
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.height = self.display_surface.get_height() * 0.8
        self.width = self.display_surface.get_width() / 4
        self.image = pygame.image.load('assets/graphics/ability_tree_background.png').convert_alpha()
        self.bg_background = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
        self.ammo_icon = pygame.image.load('assets/graphics/ammo_icon.png').convert_alpha()
        self.image_ammo = pygame.transform.scale(self.ammo_icon, (100, 80)).convert_alpha()
        self.grenade_icon = pygame.image.load('assets/graphics/grenade.png').convert_alpha()
        self.image_grenade = pygame.transform.scale(self.grenade_icon, (50, 60)).convert_alpha()
        self.board = pygame.image.load('assets/graphics/board.png').convert_alpha()
        self.board_image =  pygame.transform.scale(self.board, (1400, 450)).convert_alpha()
        self.health = pygame.image.load('assets/graphics/health.png').convert_alpha()
        self.image_health = pygame.transform.scale(self.health, (140, 80)).convert_alpha()
        self.cooldown = 0

        self.selection_index= 0
        self.selection_time = None
        self.can_move = True
        self.add_ammo_button = button.Button(850, 410, add_ability_button_img, 0.1)
        self.add_grenade_buton = button.Button(850, 490, add_ability_button_img, 0.1)
        self.add_health_button = button.Button(850, 570, add_ability_button_img, 0.1)

    def update(self, player):
        self.draw_skill_tree(player)


    def draw_skill_tree(self, player):
        paused = True
        while paused:
            current_time = time.time()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if pygame.key.get_pressed()[pygame.K_ESCAPE] or pygame.key.get_pressed()[pygame.K_r]:
                    if current_time - settings.last_skill_tree_time >= 0.5:
                        settings.last_skill_tree_time = current_time
                        paused = False
                        return paused
            screen.blit(self.bg_background, [0,0])
            screen.blit(self.board_image, [500, 300])
            level_text = f"Level  {player.level}"
            level_in_ability_tree = font_skill_tree.render(level_text, True, (255, 255, 255))
            screen.blit(level_in_ability_tree, (500, 150))
            points_in_ability_tree = f"Masz {player.ability_points} punktów umiejętności"
            text_points = font_skill_tree.render(points_in_ability_tree, True, (255, 255, 255))
            screen.blit(text_points, (700, 150))
            screen.blit(self.image_ammo, (700, 390))
            screen.blit(self.image_grenade, (700, 490))
            screen.blit(self.image_health, (660, 560))
            ammo_text = f"{player.max_main_ammo_magazine} "
            ammo_in_ability_tree = font_skill_tree.render(ammo_text, True, (255, 255, 255))
            grenades_text = f" {player.max_grenade_amount} "
            grenades_in_ability_tree = font_skill_tree.render(grenades_text, True, (255, 255, 255))
            health_text = f"{player.max_health}"
            health_in_ability_tree = font_skill_tree.render(health_text, True, (255, 255, 255))
            screen.blit(ammo_in_ability_tree, (770, 410))
            screen.blit(grenades_in_ability_tree, (770, 510))
            screen.blit(health_in_ability_tree, (770, 580))
            if player.ability_points > 0:
                self.add_ammo_button.draw()
                if self.add_ammo_button.draw() and current_time - self.cooldown > 0.5:
                    player.max_main_ammo_magazine += 2
                    player.ability_points -=1
                    self.cooldown = current_time
                self.add_grenade_buton.draw()
                if self.add_grenade_buton.draw() and current_time - self.cooldown > 0.5:
                    player.max_grenade_amount += 1
                    player.ability_points -= 1
                    self.cooldown = current_time
                self.add_health_button.draw()
                if self.add_health_button.draw() and current_time - self.cooldown > 0.5:
                    player.max_health += 10
                    player.ability_points -= 1
                    self.cooldown = current_time
            pygame.display.flip()
