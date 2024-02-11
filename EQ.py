import settings
"""
    This file contains EQ class which is responsible for mechanics of inventory interface for player.
    
"""
class PlayerInventory:
    def __init__(self, data):
        self.x_cord = 0
        self.y_cord = 0
        self.tile_inventory_list = []
        self.map_data = data
        slot_inventory_image = settings.pygame.image.load('assets/graphics/slot_inventory_image.png').convert_alpha()
        background = settings.pygame.image.load("assets/graphics/inventory_background.png").convert_alpha()
        self.bg_background = settings.pygame.transform.scale(background, (settings.SCREEN_WIDTH/2, settings.SCREEN_HEIGHT)).convert_alpha()

        self.row_count = 0
        for row in self.map_data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    slot_image = settings.pygame.transform.scale(slot_inventory_image,
                                                                       (settings.SLOT_SIZE, settings.SLOT_SIZE))
                    slot_inventory_rect = slot_image.get_rect()
                    slot_inventory_rect.x = col_count * settings.SLOT_SIZE + 150
                    slot_inventory_rect.y = self.row_count * settings.SLOT_SIZE + settings.SLOT_SIZE
                    tile = [slot_image, slot_inventory_rect]
                    self.tile_inventory_list.append(tile)

                col_count += 1
            self.row_count += 1

    def update(self):
        self.draw()

    def draw(self):
        paused = True
        while paused:
            current_time = settings.time.time()
            for event in settings.pygame.event.get():
                if event.type == settings.pygame.QUIT:
                    settings.pygame.quit()

                if settings.pygame.key.get_pressed()[settings.pygame.K_ESCAPE] or settings.pygame.key.get_pressed()[settings.pygame.K_p]:
                    if current_time - settings.last_skill_tree_time >= 0.5:
                        settings.last_skill_tree_time = current_time
                        paused = False
                        return paused
            #screen.blit(self.bg_background, [0, 0])
            settings.screen.blit(self.bg_background, (self.x_cord, self.y_cord))
            for tile in self.tile_inventory_list:
                settings.screen.blit(tile[0], tile[1])
            settings.pygame.display.flip()