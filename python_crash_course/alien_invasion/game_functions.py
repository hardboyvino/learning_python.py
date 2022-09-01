"""Modules required from python libraries for making the game functional."""
import sys
import pygame
from time import sleep

from bullet import Bullet
from alien import Alien


def check_events(ai_settings, bullets, screen, ship):
    """Check for keyboard and mouse actions."""
    for event in pygame.event.get():
        # --- IF A KEY IS PRESSED DOWN --- #
        # --- CHECK IF DIRECTIONAL KEY IS PRESSED AND TURN MOVING FLAG TO TRUE --- #
        if event.type == pygame.KEYDOWN:
            check_keydown_events(ai_settings, bullets, screen, ship, event)

        # --- CHECK IF DIRECTIONAL KEY IS RELEASED AND TURN MOVING FLAG TO FALSE SO SHIP STOPS MOVING --- #
        elif event.type == pygame.KEYUP:
            check_keyup_events(ship, event)


def check_keyup_events(ship, event):
    """Response to keyup events."""
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_keydown_events(ai_settings, bullets, screen, ship, event):
    """Response to keydown events."""
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    # --- CHECK IF SPACEBAR IS PRESSED FOR BULLETS --- #
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, bullets, screen, ship)
    # --- IF USER CLICKS ON ESC, THE GAME PROGRAM CLOSES --- #
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def fire_bullet(ai_settings, bullets, screen, ship):
    """Fire bullets and add onscreen bullets to a list within list limit."""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(ai_settings, aliens, bullets, screen):
    """Show bullets on screen and remove those on screen to save memory usage."""
    # --- UPDATE BULLET POSITION --- #
    bullets.update()
    # --- DELETE BULLETS THAT ARE NO LONGER ON THE SCREEN --- #
    # --- FOR EACH BULLET IN THE COPY OF BULLETS LIST --- #
    for bullet in bullets.copy():
        # --- IF THE BOTTOM OF THE BULLET IS OFF SCREEN --- #
        if bullet.rect.bottom <= 0:
            # --- REMOVE THE BULLET FROM THE ORIGINAL BULLET LIST --- #
            bullets.remove(bullet)

    check_bullet_alien_collision(ai_settings, aliens, bullets, screen)


def check_bullet_alien_collision(ai_settings, aliens, bullets, screen):
    """Reponse when bullet hits aliens."""
    # --- CHECK FOR ANY BULLETS THTA HAVE HIT ALIENS --- #
    # --- IF SO, GET RID OF THE BULLETS AND THE ALIEN --- #
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)

    # --- IF THERE ARE NO ALIENS ON THE SCREEN, CREATE A NEW FLEET --- #
    #  EMPTY ANY BULLETS THAT MIGHT BE ON SCREEN --- #
    if len(aliens) == 0:
        bullets.empty()
        update_game_engine(ai_settings)
        create_fleet(ai_settings, aliens, screen)


def update_aliens(ai_settings, aliens, bullets, screen, ship, stats):
    """Move the aliens to the side without moving out of the screen."""
    # --- UPDATE ALLIENS POSITION --- #
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # --- CHECK FOR SHIP-ALIEN COLLISION --- #
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, aliens, bullets, screen, ship, stats)

    # --- CHECK FOR ALIEN REACHING BOTTOM OF THE SCREEN --- #
    check_aliens_bottom(ai_settings, aliens, bullets, screen, ship, stats)


def create_fleet(ai_settings, aliens, screen):
    """Create a fleet of aliens."""
    # --- CREATE AN ALIEN AND FIND HOW MANY ALIENS CAN BE IN A ROW --- #
    # --- SPACING BETWEEN EACH ALIEN IS EQUAL TO ONE ALIEN WIDTH AND HEIGHT--- #
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_y(ai_settings, alien.rect.height)

    # -- CREATE ROW OF ALIENS --- #
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, aliens, alien_number, row_number, screen)


def create_alien(ai_settings, aliens, alien_number, row_number, screen):
    """Create an alien and place it in the row."""
    # --- CREATE INDIVIDUAL ALIEN AND PLACE IT IN A ROW --- #
    # --- CREATE ALIEN INSTANCE --- #
    alien = Alien(ai_settings, screen)
    # --- ASSIGN THE WIDTH OF THE ALIEN RECT TO A VARIABLE FOR CALCULATIONS --- #
    alien_width = alien.rect.width
    alien.rect.x = alien_width + (2 * alien_width) * alien_number
    alien.rect.y = alien.rect.height + (2 * alien.rect.height) * row_number
    aliens.add(alien)


def get_number_aliens_x(ai_settings, alien_width):
    """Get the number of aliens per row."""
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_y(ai_settings, alien_height):
    """Determine the number of rows of aliens can fit on half the screen."""
    available_space_y = (ai_settings.screen_height / 2)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def check_fleet_edges(ai_settings, aliens):
    """Respond to the aliens hitting the edge."""
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Change the fleet direction accordingly."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, aliens, bullets, screen, ship, stats):
    """Respond to alien hitting ship."""
    # --- DECREASE THE NUMBER OF SHIPS BY 1 --- #
    stats.ships_left -= 1

    # --- REMOVE ALL REMAINING ALIENS AND BULLETS FROM THE SCREEN ONCE A HIT NOTICED --- #
    aliens.empty()
    bullets.empty()

    # --- CREATE A NEW FLEET --- #
    create_fleet(ai_settings, aliens, screen)
    ship.center_ship()

    # --- LET PLAYER NOTICE THERE WAS A CRASH AND RESET HAPPENING --- #
    sleep(1)

def update_game_engine(ai_settings):
    """Update the game settings to make the game faster if all aliens are killed."""
    # --- SHIP SPEED SETTINGS --- #
    ai_settings.ship_speed_factor *= 1.5

    # --- BULLET SETTINGS
    # --- HAVE THE BULLETS TRAVEL AT HALF THE SPEED OF THE SHIP --- #
    ai_settings.bullet_speed_factor *= 1.5
    ai_settings.bullet_width *= 1.5
    ai_settings.bullets_allowed *= 2

    ai_settings.alien_speed_factor *= 1.1


def check_aliens_bottom(ai_settings, aliens, bullets, screen, ship, stats):
    """Check if the aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            """Response the same as ship getting hit."""
            ship_hit(ai_settings, aliens, bullets, screen, ship, stats)
            break


def update_screen(ai_settings, aliens, bullets, screen, ship):
    """Fill the screen with background colour, load shooter and display most recently drawn screen."""
    # --- FILL THE SCREEN WITH BACKGROUND COLOR --- #
    screen.fill(ai_settings.background_colour)

    # --- DRAW BULLETS ON SCREEN --- #
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # --- DRAW SHOOTER SHIP IN STARTING POSITION --- #
    ship.blitme()

    # --- DRAW THE FLEET OF ALIENS --- #
    aliens.draw(screen)

    # --- DISPLAY THE MOST RECENTLY DRAWN SCREEN --- #
    pygame.display.flip()
