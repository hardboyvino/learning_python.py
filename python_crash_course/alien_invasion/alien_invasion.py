"""Modules required from python libraries for making the game functional."""
import pygame
from pygame.sprite import Group

"""Import classes and functions from other files to main program for functionality."""
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats


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
    bullets = Group()
    aliens = Group()

    # --- CREATE A FLEET OF ALIENS --- #
    gf.create_fleet(ai_settings, aliens, screen)

    # --- CREATE AN INSTANCE TO STORE GAME STATISTICS --- #
    stats = GameStats(ai_settings)

    # --- START THE MAIN LOOP OF THE GAME --- #
    while True:
        gf.check_events(ai_settings, bullets, screen, ship)
        ship.update_movement()
        gf.update_bullets(ai_settings, aliens, bullets, screen)
        gf.update_aliens(ai_settings, aliens, bullets, screen, ship, stats)
        gf.update_screen(ai_settings, aliens, bullets, screen, ship)


if __name__ == "__main__":
    main()
