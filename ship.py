import pygame

from settings import Settings

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Inizialize the ship and set its starting position"""
        # assign the screen to an attribute of ship
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store a decimal for the ship's horizontal position
        self.x = float(self.rect.x)

        # movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        # update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # update rect object from self.x
        self.rect.x = self.x
    
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
