from settings import *

def grenades_icon():
    grenade_icon = pygame.image.load('assets/graphics/grenade.png').convert_alpha()
    image = pygame.transform.scale(grenade_icon, (35, 40)).convert_alpha()
    screen.blit(image, (0, 110))
def ammo_icon():
    grenade_icon = pygame.image.load('assets/graphics/ammo_icon.png').convert_alpha()
    image = pygame.transform.scale(grenade_icon, (70, 60)).convert_alpha()
    screen.blit(image, (0, 40))