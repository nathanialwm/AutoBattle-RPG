import numpy as np
import random as ran
import pygame
import player
import enemy
import equip
import gui

iterable_enemy_objects = [enemy.Mouse,enemy.Giant_Rat,enemy.Rabid_Dog,enemy.Skeleton,enemy.Thief,enemy.Zombie,
                          enemy.Yeti,enemy.Vampire,enemy.Minotaur,enemy.Dragon]
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
            if gui.menu_battle_rect.collidepoint(pygame.mouse.get_pos()):
                battle_screen = True
                equip_screen = False
                stat_screen = False
            if gui.menu_equip_rect.collidepoint(pygame.mouse.get_pos()):
                battle_screen = False
                equip_screen = True
                stat_screen = False
            if gui.menu_stats_rect.collidepoint(pygame.mouse.get_pos()):
                battle_screen = False
                equip_screen = False
                stat_screen = True

            # Clicking between enemy types
            for index, rect in enumerate(gui.enemy_button_rects):
                if rect.collidepoint(pygame.mouse.get_pos()) and battle_screen:
                    for enemy in iterable_enemy_objects:
                        enemy.battling = False
                    iterable_enemy_objects[index].battling = True

            

    # Hover effects for top menu
    if gui.menu_battle_rect.collidepoint(pygame.mouse.get_pos()):
        gui.menu_battle_surface = gui.game_menu_font.render('Battle', True, 'Blue')
    else:
        gui.menu_battle_surface = gui.game_menu_font.render('Battle', True, 'Black')
    if gui.menu_equip_rect.collidepoint(pygame.mouse.get_pos()):
        gui.menu_equip_surface = gui.game_menu_font.render('Equipment', True, 'Blue')
    else:
        gui.menu_equip_surface = gui.game_menu_font.render('Equipment', True, 'Black')
    if gui.menu_stats_rect.collidepoint(pygame.mouse.get_pos()):
        gui.menu_stats_surface = gui.game_menu_font.render('Stats', True, 'Blue')
    else:
        gui.menu_stats_surface = gui.game_menu_font.render('Stats', True, 'Black')

    # Put menu items on screen
    screen.blit(gui.menu_battle_surface, gui.menu_battle_rect)
    screen.blit(gui.menu_equip_surface, gui.menu_equip_rect)
    screen.blit(gui.menu_stats_surface, gui.menu_stats_rect)

    # Create screen elements for each of the three 'pages'
    # Create battle screen
    if battle_screen:
        # Put enemy button objects on screen
        screen.blit(gui.enemy_mouse_surface, gui.enemy_mouse_rect)
        screen.blit(gui.enemy_giant_rat_surface, gui.enemy_giant_rat_rect)
        screen.blit(gui.enemy_rabid_dog_surface, gui.enemy_rabid_dog_rect)
        screen.blit(gui.enemy_skeleton_surface, gui.enemy_skeleton_rect)
        screen.blit(gui.boss_thief_surface, gui.boss_thief_rect)
        screen.blit(gui.enemy_zombie_surface, gui.enemy_zombie_rect)
        screen.blit(gui.enemy_yeti_surface, gui.enemy_yeti_rect)
        screen.blit(gui.enemy_vampire_surface, gui.enemy_vampire_rect)
        screen.blit(gui.enemy_minotaur_surface, gui.enemy_minotaur_rect)
        screen.blit(gui.boss_dragon_surface, gui.boss_dragon_rect)

        # Determine which monster is active
        for index, enemy in enumerate(iterable_enemy_objects):
            if enemy.battling:
                screen.blit(gui.enemy_surfaces[index], gui.enemy_rects[index])


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
