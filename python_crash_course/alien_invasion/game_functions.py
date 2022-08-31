import sys
import pygame


def check_events(ship):
    """Check for keyboard and mouse actions."""
    for event in pygame.event.get():
        # --- IF USER CLICKS ON GAME WINDOW CLOSE BUTTON (TOP RIGHT X), THE GAME PROGRAM CLOSES --- #
        if event.type == pygame.QUIT:
            sys.exit()

        # --- IF A KEY IS PRESSED DOWN --- #
        elif event.type == pygame.KEYDOWN:            
            # --- CHECK IF DIRECTIONAL KEY IS PRESSED AND TURN MOVING FLAG TO TRUE --- #
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
            elif event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_UP:
                ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                ship.moving_down = True

        # --- CHECK IF DIRECTIONAL KEY IS RELEASED AND TURN MOVING FLAG TO FALSE SO SHIP STOPS MOVING --- #
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
            elif event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_UP:
                ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                ship.moving_down = False



def update_screen(ai_settings, screen, ship):
    """Fill the screen with background color, load shooter and display most recently drawn screen."""
    # --- FILL THE SCREEN WITH BACKGROUND COLOR AND LOAD THE SHOOTER AT STARTING POSITION --- #
    screen.fill(ai_settings.background_color)
    ship.blitme()

    # --- DISPLAY THE MOST RECENTLY DRAWN SCREEN --- #
    pygame.display.flip()
