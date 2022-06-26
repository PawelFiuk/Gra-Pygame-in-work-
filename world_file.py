from settings_file import *


class World:
    def __init__(self, data):
        self.x_cord = 0
        self.y_cord = 0
        self.tile_list = []
        dirt_img = pygame.image.load('krajobraz/dirt_1.png').convert()
        stone_img = pygame.image.load('krajobraz/dirt_1.png').convert()
        self.bg_background = pygame.image.load("miasto tlo.png").convert_alpha()

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    dirt_img = pygame.transform.scale(dirt_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = dirt_img.get_rect()
                    img_rect.x = col_count * TILE_SIZE + self.x_cord
                    img_rect.y = row_count * TILE_SIZE + self.y_cord
                    tile = (dirt_img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    stone_img = pygame.transform.scale(stone_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = stone_img.get_rect()
                    img_rect.x = col_count * TILE_SIZE + self.x_cord
                    img_rect.y = row_count * TILE_SIZE + self.y_cord
                    tile = (stone_img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            #pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)
            #if player.rect.x /2 < screen_width:
            #   screen.blit(, kafle, [-player.rect.x])

        screen.blit(self.bg_background, (self.x_cord, self.y_cord))

