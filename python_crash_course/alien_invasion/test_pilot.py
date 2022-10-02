"""Modules required from python libraries for making the game functional."""
import pygame
from pygame.sprite import Group

"""Import classes and functions from other files to main program for functionality."""
from settings import Settings
from ship import Ship
import game_functions as gf


def main():
    """The main function of the game."""
    run_game()


def run_game():
    """Run the initial alien invasion game screen and settings."""

    # --- INITIALIZE THE GAME CONSTRUCTOR --- #
    pygame.init()

    # --- CREATE SETTINGS INSTANCE --- #
    ai_settings = Settings()

    # --- OPEN UP THE WINDOW WITH A WINDOW CAPTION DISPLAYED --- #
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # --- CREATE SHIP, ALIENS, ALIEN FLEET, BULLETS INSTANCES --- #
    ship = Ship(ai_settings, screen)
    rain = Group()
    aliens = Group()

    # --- CREATE A FLEET OF ALIENS --- #
    gf.create_fleet(ai_settings, aliens, screen, ship)

    # --- START THE MAIN LOOP OF THE GAME --- #
    while True:
        gf.check_events(ai_settings, rain, screen, ship)
        ship.update_movement()
        # --- UPDATE BULLET POSITION --- #
        rain.update()
        # --- DELETE rain THAT ARE NO LONGER ON THE SCREEN --- #
        # --- FOR EACH BULLET IN THE COPY OF rain LIST --- #
        for bullet in rain.copy():
            # --- IF THE BOTTOM OF THE BULLET IS OFF SCREEN --- #
            if bullet.rect.bottom <= 0:
                # --- REMOVE THE BULLET FROM THE ORIGINAL BULLET LIST --- #
                rain.remove(rain)  
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, aliens, rain, screen, ship)


if __name__ == "__main__":
    main()
