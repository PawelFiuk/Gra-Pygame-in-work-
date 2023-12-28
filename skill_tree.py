import pygame.display

import settings
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
        pass

    def draw_skill_tree(self):
        self.display_surface.fill((0,0,0))

    def add_new_ability(self):
        pass

