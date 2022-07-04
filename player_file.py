from settings_file import *


class Player:
    def __init__(self, x, y):
        # Pobieramy zdjęcie Augustusa, dalej skalujemy (powiększamy) odpowiednio do mapy
        # pygame.sprite.Sprite.__init__(self)
        img_Augustus = pygame.image.load('Augustus IV wersja 4.png').convert_alpha()
        self.image = pygame.transform.scale(img_Augustus, (400, 400)).convert_alpha()
        self.rect = self.image.get_rect()  # dzielimy postać na kwadrat
        self.rect.x = x  # Wybieramy lokalizacje gdzie pojawi się postać
        self.rect.y = y
        self.width = self.image.get_width()  # Wymiary kwadratu dzielącego postać
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumper = "ready"  # zmienna pozwalająca na zablokowanie nieskończonego skakania

    def update(self):
        global tile
        dx = 0
        dy = 0

        # sterowanie klawiszami i szybkość poruszania się
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE] and self.jumper == "ready" or key[pygame.K_UP] and \
                self.jumper == "ready" or key[pygame.K_w] and self.jumper == "ready":
            self.vel_y = -10
            self.jumper = "jumping"

        if key[pygame.K_a] or key[pygame.K_LEFT]:
            dx -= 2

        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            dx += 2

        # dodanie grawitacji
        self.vel_y += 0.2
        if self.vel_y > 120:
            self.vel_y = dy
        dy += self.vel_y

        # sprawdzanie kolizji
        from main import world # import lokalny obiektu z pliku main
        for tile in world.tile_list:
            # sprawdzanie kolizji w osi x
            if tile[1].colliderect(self.rect.x + dx, self.rect.y + dy, self.width, self.height):
                dx = 0

            """if player.rect.x >= background_x-100:
                background_x += 100"""

            # sprawdzanie kolizji w osi y
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # sprawdz czy pod ziemia skaka
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                # sprawdz czy pod ziemia spada
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0
                    self.jumper = 'ready'

        # update koordynatów gracz
        self.rect.x += dx
        self.rect.y += dy
        # print(self.rect.x, self.rect.y)

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = tile[1].bottom
            self.jumper = "ready"

        # Przewijanie tła

        if self.rect.x >= resolution[0] / 2:
            x_screen = resolution[0] / 2
            self.rect.x = x_screen
            from main import world
           # world.x_cord -= dx
            scroll[0] = dx

            #self.rect.x -= dx
        elif self.rect.x <= resolution[0] - 1800:
            x_screen_left = resolution[0] - 1800
            self.rect.x = x_screen_left
            scroll[0] = 0
            scroll[0] -= dx

        #else:
            #x_screen = self.rect.x
            #self.rect.x = x_screen


        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

    def draw(self):
        screen.blit(self.image, self.rect)
