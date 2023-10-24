import settings
import pygame

import unittest
import pygame
from player import Player  # Replace 'your_module' with the actual module name where Player is defined

class TestPlayer(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.player = Player(0, 0, headless=True)

    def tearDown(self):
        pygame.quit()

    def test_initialization(self):
        self.assertEqual(self.player.rect.x, 0)
        self.assertEqual(self.player.rect.y, 0)
        self.assertEqual(self.player.current_health, 100)
        self.assertEqual(self.player.max_health, 100)
        self.assertEqual(self.player.main_ammo_magazine, 20)

    def test_update(self):
        # You can simulate key presses or other actions to test the update method.
        # Example: Simulate a jump action
        self.player.update()  # Simulate an update without any key presses
        initial_y = self.player.rect.y
        self.player.velocity_y = -10
        self.player.jumper = "ready"
        self.player.update()  # Simulate an update after a jump action
        self.assertNotEqual(self.player.rect.y, initial_y)  # Check if the player's position changed after a jump

    def test_health_bar(self):
        # You can create a mock screen surface to test the health bar rendering.
        # Example: Test if the health bar gets drawn correctly
        mock_screen = pygame.Surface((800, 600))  # Create a mock screen surface
        self.player.health_bar()
        # Add assertions to check if the health bar was drawn correctly on the mock screen

    def test_main_ammo(self):
        # You can create a mock screen surface to test the main ammo rendering.
        # Example: Test if the main ammo count gets rendered correctly
        mock_screen = pygame.Surface((800, 600))  # Create a mock screen surface
        self.player.main_ammo()
        # Add assertions to check if the main ammo count was rendered correctly on the mock screen

    def test_position(self):
        position = self.player.position()
        self.assertEqual(len(position), 2)
        self.assertEqual(len(position[0]), 1)
        self.assertEqual(len(position[1]), 1)
        # Add assertions to check the correctness of the player's position

    def test_shot_bullet(self):
        # Example: Test if the shot_bullet method returns a Bullets object with correct coordinates
        bullet = self.player.shot_bullet()
        self.assertEqual(bullet.flip, self.player.flip)
        if self.player.flip:
            self.assertEqual(bullet.pos[0], self.player.rect.x - 100)
        else:
            self.assertEqual(bullet.pos[0], self.player.rect.x + 500)
        self.assertEqual(bullet.pos[1], self.player.rect.y + 220)

if __name__ == "__main__":
    unittest.main()