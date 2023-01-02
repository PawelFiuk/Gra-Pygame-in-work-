import settings_file
import pygame


# narysowanie siatki na kafelkach
def test_draw_grid_tile():
    for line in range(0, 16):
        pygame.draw.line(settings_file.screen, (255, 255, 255), (0, line * settings_file.TILE_SIZE),
                         (settings_file.SCREEN_WIDTH, line * settings_file.TILE_SIZE))
        pygame.draw.line(settings_file.screen, (255, 255, 255), (line * settings_file.TILE_SIZE, 0),
                         (line * settings_file.TILE_SIZE, settings_file.SCREEN_HEIGHT))

# narysowanie kwadratu na postaci

def test_draw_rect_player():
    pass

def test_draw_rect_bullet():
    pass

def test_draw_rect_enemy():
    pass

def test_bars_ui():
    pass

def test_draw_rect_npc():
    pass

def test_draw_chatting():
    pass

def test_draw_ui_eq():
    pass
