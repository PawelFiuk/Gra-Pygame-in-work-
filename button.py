from settings import *


class Button:
    def __init__(self, x: int, y: int, image, scale: float):
        """
        Arguments: self, position - x and y position where button should be placed, image - file with image of button,
            scale - a flaot number that is used to scale the image
        Application: setting the basic parameters of the projectile
        Return: None
        """
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        """
        Arguments: self
        Application: used to draw a button, if the mouse hovers over the button and clicks on it,
            the action will be triggered
        Return: boolean action
        """
        action = False   # mozna tworzyc na tym warunki po kliknieciu
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(self.image, (self.rect.x, self.rect.y))

        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 :
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action

