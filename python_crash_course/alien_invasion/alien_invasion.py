import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


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
        gf.check_events(ship)
        ship.update_movement()
        gf.update_screen(ai_settings, screen, ship)


if __name__ == "__main__":
    main()
