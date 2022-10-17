"""
All the game functions.
"""

import sys
import pygame

from car import VillianCar


def check_events(hero_car):
    """Check for keyboard and mouse events."""
    # --- watch for keyboard and mouse events.
    for event in pygame.event.get():
        # --- if a key is pressed down, check what the response should be
        if event.type == pygame.KEYDOWN:
            check_keydown_events(hero_car, event)
        # --- if a key is released, check what the response should be
        elif event.type == pygame.KEYUP:
            check_keyup_events(hero_car, event)


def check_keyup_events(hero_car, event):
    """Check event reaction when keys are released."""
    if event.key == pygame.K_RIGHT:
        hero_car.moving_right = False
    elif event.key == pygame.K_LEFT:
        hero_car.moving_left = False
    elif event.key == pygame.K_UP:
        hero_car.moving_up = False
    elif event.key == pygame.K_DOWN:
        hero_car.moving_down = False


def check_keydown_events(hero_car, event):
    """Check event reaction when keys are pressed down."""
    if event.key == pygame.K_RIGHT:
        hero_car.moving_right = True
    elif event.key == pygame.K_LEFT:
        hero_car.moving_left = True
    elif event.key == pygame.K_UP:
        hero_car.moving_up = True
    elif event.key == pygame.K_DOWN:
        hero_car.moving_down = True

    # --- quit the game when the escape key is pressed
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def new_car(villian_cars, screen, settings):
    """Create a new villian car and add it to the villian group."""
    if len(villian_cars) < settings.cars_allowed:
        new_car = VillianCar(screen, settings)
        villian_cars.add(new_car)

        # --- spacing between cars
        villian_height = new_car.rect.height
        available_space = settings.screen_height - (2 * villian_height)
        number_villians = int(available_space / (2 * villian_height))

    # --- get rid of cars that are offscreen
    for villian_car in villian_cars.copy():
        if villian_car.rect.top > settings.screen_height:
            villian_cars.remove(villian_car)


def car_collision(villian_cars, settings, stats, screen, background):
    """Detect car collisions and end the game if out of lives."""
    if stats.cars_left > 0:
        stats.cars_left -= 1

        # --- empty the villian cars sprite group
        villian_cars.empty()

        new_car(villian_cars, screen, settings)

    else:
        villian_cars.empty()
        background.scroll = 0
        stats.game_active = False


def update_cars(hero_car, villian_cars, settings, stats, screen,background):
    """Update game reaction when there is a collision."""
    if pygame.sprite.spritecollideany(hero_car, villian_cars):
        car_collision(villian_cars, settings, stats, screen, background)


# def stop_game(settings, clock, start):
#     start -= 1

#     if start == 0:
#         settings.increase_difficulty()
#         print("Yes!")
#         # start = 500

#     clock.tick(100)


def update_screen(hero_car, villian_cars):
    """Update the screen with required images and background colours."""
    # --- fill the screen with specific background colour
    # --- draw the car to screen
    # screen.fill(settings.background_colour)
    hero_car.blitme()

    # --- draw each villian car in the group onscreen
    for villian_car in villian_cars.sprites():
        villian_car.blitme()

    # --- make the most recently drawn screen visible
    pygame.display.flip()
