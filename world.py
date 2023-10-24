from pygame import key

from settings import *


class World:
    def __init__(self, data):
        self.x_cord = 0
        self.y_cord = 0
        self.tile_list = []
        dirt_img = pygame.image.load('assets/map_tiles/dirt_1.png').convert_alpha()
        stone_img = pygame.image.load('assets/map_tiles/stone 1.png').convert_alpha()
        #self.image = pygame.transform.scale(img_Augustus, (400, 400)).convert_alpha()
        background = pygame.image.load("miasto tlo.png").convert_alpha()
        self.bg_background = pygame.transform.scale(background, (1900, 900)).convert_alpha()

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    dirt_img = pygame.transform.scale(dirt_img, (TILE_SIZE, TILE_SIZE))
                    #screen.blit(dirt_img)
                    img_rect_dirt = dirt_img.get_rect()
                    img_rect_dirt.x = col_count * TILE_SIZE
                    img_rect_dirt.y = row_count * TILE_SIZE
                    tile = [dirt_img, img_rect_dirt]
                    self.tile_list.append(tile)

                if tile == 2:
                    stone_img = pygame.transform.scale(stone_img, (TILE_SIZE, TILE_SIZE))
                    #screen.blit(stone_img)
                    img_rect_stone = stone_img.get_rect()
                    img_rect_stone.x = col_count * TILE_SIZE
                    img_rect_stone.y = row_count * TILE_SIZE
                    tile = (stone_img, img_rect_stone)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        screen.blit(self.bg_background, (self.x_cord, self.y_cord))
        for tile in self.tile_list:

            tile[1][0] -= scroll_position_of_player[0]
            #tile[1][0] -= scroll_position_of_player[1]
            screen.blit(tile[0], tile[1])
            #pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)
            #from main import player
            #if player.rect.x >= SCREEN_WIDTH:


        #screen.blit(self.bg_background, (self.x_cord, self.y_cord))

