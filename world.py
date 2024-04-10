import pygame.sprite
from settings import *


class Level1:
    def __init__(self, data):
        self.x_cord = 0
        self.y_cord = 0
        self.tile_list = []
        self.map_data = data
        dark_underground_tile_img = pygame.image.load('assets/map_tiles/dark_underground_tile_1.png').convert_alpha()
        dark_top_tile_img = pygame.image.load('assets/map_tiles/dark_top_tile_2.png').convert_alpha()
        dark_right_tile_img = pygame.image.load('assets/map_tiles/dark_right_tile_3.png').convert_alpha()
        dark_left_tile_img = pygame.image.load('assets/map_tiles/dark_left_tile_4.png').convert_alpha()
        background = pygame.image.load("assets/graphics/steampunk_city_1.png").convert_alpha()
        self.bg_background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()

        self.row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    dark_underground_tile_img = pygame.transform.scale(dark_underground_tile_img, (TILE_SIZE, TILE_SIZE))
                    img_rect_dirt = dark_underground_tile_img.get_rect()
                    img_rect_dirt.x = col_count * TILE_SIZE
                    img_rect_dirt.y = self.row_count * TILE_SIZE - TILE_SIZE
                    tile = [dark_underground_tile_img, img_rect_dirt]
                    self.tile_list.append(tile)

                elif tile == 2:
                    dark_top_tile_img = pygame.transform.scale(dark_top_tile_img, (TILE_SIZE, TILE_SIZE))
                    img_rect_stone = dark_top_tile_img.get_rect()
                    img_rect_stone.x = col_count * TILE_SIZE
                    img_rect_stone.y = self.row_count * TILE_SIZE - TILE_SIZE
                    tile = [dark_top_tile_img, img_rect_stone]
                    self.tile_list.append(tile)

                elif tile == 3:
                    dark_right_tile_img = pygame.transform.scale(dark_right_tile_img, (TILE_SIZE, TILE_SIZE))
                    img_rect_right_stone = dark_right_tile_img.get_rect()
                    img_rect_right_stone.x = col_count * TILE_SIZE
                    img_rect_right_stone.y = self.row_count * TILE_SIZE - TILE_SIZE
                    tile = [dark_right_tile_img, img_rect_right_stone]
                    self.tile_list.append(tile)

                elif tile == 4:
                    dark_left_tile_img = pygame.transform.scale(dark_left_tile_img, (TILE_SIZE, TILE_SIZE))
                    img_rect_left_stone = dark_left_tile_img.get_rect()
                    img_rect_left_stone.x = col_count * TILE_SIZE
                    img_rect_left_stone.y = self.row_count * TILE_SIZE - TILE_SIZE
                    tile = [dark_left_tile_img, img_rect_left_stone]
                    self.tile_list.append(tile)
                col_count += 1
            self.row_count += 1

    def draw(self):
        screen.blit(self.bg_background, (self.x_cord, self.y_cord))
        for tile in self.tile_list:
            tile[1][0] -= scroll_position_of_player[0]
            #tile[1][1] -= scroll_position_of_player[1]
            screen.blit(tile[0], tile[1])
            # to do : create Y axix scrolling after jumping



