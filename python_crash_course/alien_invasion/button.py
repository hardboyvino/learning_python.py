"""
Pygame module to render text to the screen.
"""
import pygame.font

class Button(object):
    """Creates a button class for the game."""

    def __init__(self, ai_settings, message, screen) -> None:
        """Initialize the play button."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # --- SET THE DIMENSIONS OF THE PLAY BUTTON --- #
        self.width, self.height = 200, 50
        self.button_colour = (0, 255, 0)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # --- BUILD THE BUTTON'S RECT OBJECT AND CENTER IT --- #
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # --- THE MESSAGE IN THE BUTTON --- #
        self.prep_message(message)


    def prep_message(self, message):
        """Turn the message into a rendered image and center the text on the button."""
        self.message_image = self.font.render(message, True, self.text_colour, self.button_colour)
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center


    def draw_button(self):
        """Draw the button onto the screen."""
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect)
