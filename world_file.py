from pygame import key
import os
from settings_file import *


class World:
    def __init__(self, lvl):
        self.x_cord = 0
        self.y_cord = 0
        self.tile_list = []
        dirt_img = pygame.image.load('krajobraz/dirt_1.png').convert_alpha()
        stone_img = pygame.image.load('krajobraz/dirt_1.png').convert_alpha()
        #self.image = pygame.transform.scale(img_Augustus, (400, 400)).convert_alpha()
        background = pygame.image.load("miasto tlo.png").convert_alpha()
        self.bg_background = pygame.transform.scale(background, (1900, 900)).convert_alpha()
        with open(os.path.join(os.getcwd(), "worlds_files", "world_lvl" + str(lvl) + ".txt")) as file:
            world_data_tab = file.read().split('\n')[:-1]

        world_data = []
        for row in world_data_tab:
            world_data.append(list(map(int, row.split(' '))))

        for row_index, row in enumerate(world_data):
            for col_index, tile in enumerate(row):
                if tile == 1:
                    dirt_img = pygame.transform.scale(dirt_img, (TILE_SIZE, TILE_SIZE))
                    screen.blit(dirt_img)
                    img_rect_dirt = dirt_img.get_rect()
                    img_rect.x = col_index * TILE_SIZE
                    img_rect.y = row_index * TILE_SIZE
                    tile = [dirt_img, img_rect_dirt]
                    self.tile_list.append(tile)
                elif tile == 2:
                    stone_img = pygame.transform.scale(stone_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = stone_img.get_rect()
                    img_rect.x = col_index * TILE_SIZE
                    img_rect.y = row_index * TILE_SIZE
                    tile = (stone_img, img_rect)
                    self.tile_list.append(tile)

    def draw(self):
        screen.blit(self.bg_background, (self.x_cord, self.y_cord))
        for tile in self.tile_list:

            tile[1][0] -= scroll[0]
            screen.blit(tile[0], tile[1])
            #pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)
            #from main import player
            #if player.rect.x >= SCREEN_WIDTH:


        #screen.blit(self.bg_background, (self.x_cord, self.y_cord))

