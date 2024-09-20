import numpy as np
import random as ran
import pygame
import textwrap as wrap
import player
import enemy
import equip
import gui

iterable_enemy_objects = [enemy.Mouse,enemy.Giant_Rat,enemy.Rabid_Dog,enemy.Skeleton,enemy.Thief,enemy.Zombie,
                          enemy.Yeti,enemy.Vampire,enemy.Minotaur,enemy.Dragon]
active_enemy = iterable_enemy_objects[0]
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
# Make mouse enemy active from the start
enemy.Mouse.battling = True

# Create Custom event and timer for automatic battling
BATTLE_EVENT = pygame.USEREVENT + 1
timer = pygame.time.set_timer(BATTLE_EVENT,6000)


while running:
    # Draw Menu items that are always visible
    screen.fill('#bdbdbd')
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Main Event for Battling. Triggers regardless of active screen
        if event.type == BATTLE_EVENT:
            text = "You attacked the " + active_enemy.name
            wrapped_text = wrap.fill(text,280)
            gui.battle_text_surface = gui.game_menu_font.render(wrapped_text, True, 'Black')
        

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
                    active_enemy = iterable_enemy_objects[index]

            

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
        # Battle Text
        screen.blit(gui.battle_text_surface, (300, 300))

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
