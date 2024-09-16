import numpy as np
import random as ran
import pygame
import player
import enemy
import equip

# pygame setup
pygame.init()
screen = pygame.display.set_mode((960, 680))
pygame.display.set_caption('AutoBattle RPG')
clock = pygame.time.Clock()
running = True

# Set booleans for deciding what screen is visible
battle_screen = True
equip_screen = False
stat_screen = False

# Setup text and menu items that will always display
# Top Menu
game_menu_font = pygame.font.Font('fonts/Handjet-Regular.ttf', 50)
menu_battle_surface = game_menu_font.render('Battle', True, 'Black')
menu_battle_rect = menu_battle_surface.get_rect(midtop = (240, 20))
menu_equip_surface = game_menu_font.render('Equipment', True, 'Black')
menu_equip_rect = menu_equip_surface.get_rect(midtop = (480, 20))
menu_stats_surface = game_menu_font.render('Stats', True, 'Black')
menu_stats_rect = menu_stats_surface.get_rect(midtop = (720, 20))

# Create visuals and menus for battle screen

while running:
    # Draw Menu items that are always visible
    screen.fill('#bdbdbd')
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Create all click events
        if event.type == pygame.MOUSEBUTTONUP:
            # Clicking between menus
            if menu_battle_rect.collidepoint(pygame.mouse.get_pos()):
                battle_screen = True
                equip_screen = False
                stat_screen = False
            if menu_equip_rect.collidepoint(pygame.mouse.get_pos()):
                battle_screen = False
                equip_screen = True
                stat_screen = False
            if menu_stats_rect.collidepoint(pygame.mouse.get_pos()):
                battle_screen = False
                equip_screen = False
                stat_screen = True
    # Hover effects for top menu
    if menu_battle_rect.collidepoint(pygame.mouse.get_pos()):
        menu_battle_surface = game_menu_font.render('Battle', True, 'Blue')
    else:
        menu_battle_surface = game_menu_font.render('Battle', True, 'Black')
    if menu_equip_rect.collidepoint(pygame.mouse.get_pos()):
        menu_equip_surface = game_menu_font.render('Equipment', True, 'Blue')
    else:
        menu_equip_surface = game_menu_font.render('Equipment', True, 'Black')
    if menu_stats_rect.collidepoint(pygame.mouse.get_pos()):
        menu_stats_surface = game_menu_font.render('Stats', True, 'Blue')
    else:
        menu_stats_surface = game_menu_font.render('Stats', True, 'Black')

    # Put menu items on screen
    screen.blit(menu_battle_surface, menu_battle_rect)
    screen.blit(menu_equip_surface, menu_equip_rect)
    screen.blit(menu_stats_surface, menu_stats_rect)

    # Create screen elements for each of the three 'pages'
    # Create battle screen
    if battle_screen:
        pass

    # Create equipment screen
    if equip_screen:
        pass

    # create stat screen
    if stat_screen:
        pass

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
