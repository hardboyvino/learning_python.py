import sys
import pygame

from settings import Settings
from ship import Ship


def main():
    run_game()


def run_game():
    """Run the initial alien invasion game screen and settings."""

    # --- INITIALIZE THE GAME CONSTRUCTOR --- #
    pygame.init()

    # --- CREATE SETTINGS INSTANCE --- #
    ai_settings = Settings()

    # --- SET SCREEN RESOLUTION TUPLE AND BACKGROUND COLOR --- #
    resolution = (ai_settings.screen_width, ai_settings.screen_height)

    # --- OPEN UP THE WINDOW WITH A WINDOW CAPTION DISPLAYED --- #
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Alien Invasion")

    # --- CREATE SHIP INSTANCE --- #
    ship = Ship(screen)

    # --- START THE MAIN LOOP OF THE GAME --- #
    while True:

        # --- CHECK FOR KEYBOARD AND MOUSE ACTIONS --- #
        for event in pygame.event.get():
            # --- IF USER CLICKS ON GAME WINDOW CLOSE BUTTON (TOP RIGHT X), THE GAME PROGRAM CLOSES --- #
            if event.type == pygame.QUIT:
                sys.exit()

        # --- FILL THE SCREEN WITH BACKGROUND COLOR AND LOAD THE SHOOTER AT STARTING POSITION --- #
        screen.fill(ai_settings.background_color)
        ship.blitme()

        # --- DISPLAY THE MOST RECENTLY DRAWN SCREEN --- #
        pygame.display.flip()


if __name__ == "__main__":
    main()
