from settings import *


class World:
    def __init__(self, data):
        self.x_cord = 0
        self.y_cord = 0
        self.tile_list = []
        dirt_img = pygame.image.load('assets/map_tiles/dirt_1.png').convert_alpha()
        stone_img = pygame.image.load('assets/map_tiles/stone 1.png').convert_alpha()
        background = pygame.image.load("assets/steampunk_city_1.jpg").convert_alpha()
        self.bg_background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    dirt_img = pygame.transform.scale(dirt_img, (TILE_SIZE, TILE_SIZE))
                    img_rect_dirt = dirt_img.get_rect()
                    img_rect_dirt.x = col_count * TILE_SIZE
                    img_rect_dirt.y = row_count * TILE_SIZE
                    tile = [dirt_img, img_rect_dirt]
                    self.tile_list.append(tile)

                if tile == 2:
                    stone_img = pygame.transform.scale(stone_img, (TILE_SIZE, TILE_SIZE))
                    img_rect_stone = stone_img.get_rect()
                    img_rect_stone.x = col_count * TILE_SIZE
                    img_rect_stone.y = row_count * TILE_SIZE
                    tile = [stone_img, img_rect_stone]
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        screen.blit(self.bg_background, (self.x_cord, self.y_cord))
        for tile in self.tile_list:
            tile[1][0] -= scroll_position_of_player[0]
            tile[1][1] = SCREEN_HEIGHT - TILE_SIZE
            screen.blit(tile[0], tile[1])
