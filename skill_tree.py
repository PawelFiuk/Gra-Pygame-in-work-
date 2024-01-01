import pygame
import settings
from settings import *
import button


class SkillTree:
    def __init__(self, player):
        self.display_surface = pygame.display.get_surface()
        self.player = player
        #self.atribute_names = list(pl)

        self.height = self.display_surface.get_height() * 0.8
        self.width = self.display_surface.get_width() / 4


        self.selection_index= 0
        self.selection_time = None
        self.can_move = True

    def update(self):
        self.input()
        self.selection_cooldown()
        self.draw_skill_tree()

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and self.can_move:
            self.selection_index += 1
            self.selection_time = pygame.time.get_ticks()
            self.can_move = False
        elif keys[pygame.K_LEFT] and self.can_move:
            self.selection_index -= 1
            self.selection_time = pygame.time.get_ticks()
            self.can_move = False
        elif keys[pygame.K_SPACE]:
            self.selection_time = pygame.time.get_ticks()
            self.can_move = False

    def selection_cooldown(self):
        if not self.can_move:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 300:
                self.can_move = True


    def draw_skill_tree(self):
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
            screen.fill([0, 0, 0])
            pygame.display.flip()

    def add_new_ability(self):
        pass

