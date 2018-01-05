import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Initialize the ship and its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rectangle
        self.image = pygame.image.load('img/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the left center of the screen
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # Store a value for ship's center
        self.center = float(self.rect.centery)

        # Movement flags
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on movement flags"""
        # Update the ship's center value and not the rectangle
        if self.moving_up and self.rect.top > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.ship_speed_factor

        # Update ship rect object from self.center
        self.rect.centery = self.center

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)