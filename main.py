import numpy as np
import random as ran
import pygame
import textwrap
import time
import player
import enemy
import equip
import gui

y_offset = 0

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

# Loading bar logic
total_time = 6
interval_time = 0.5
total_intervals = total_time/interval_time
current_interval = 0

#textwrap
wrapper = textwrap.TextWrapper(width=200) 

BAR_EVENT = pygame.USEREVENT + 2
bar_timer = pygame.time.set_timer(BAR_EVENT, 500)
while running:
    # Draw Menu items that are always visible
    screen.fill('#bdbdbd')
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Main Event for Battling. Triggers regardless of active screen
        if event.type == BATTLE_EVENT:
            # Battle Result Text
            battle_text1 = "You defeated the " + active_enemy.name + ". You attacked the " + active_enemy.name + " " + "x" 
            battle_text2 = " times, " + "dealing " + "x " + " damage. The " + active_enemy.name + " attacked you "
            battle_text3 = "x" + " times, dealing " + "x" + " damage to you."
            battle_text4 = "You gained x experience points and leveled up x times."
            gui.battle_text_surface1 = gui.battle_result_font.render(battle_text1, True, 'Black')
            gui.battle_text_surface2 = gui.battle_result_font.render(battle_text2, True, 'Black')
            gui.battle_text_surface3 = gui.battle_result_font.render(battle_text3, True, 'Black')
            gui.battle_text_surface4 = gui.battle_result_font.render(battle_text4, True, 'Black')

        # Event for bar animation
        if event.type == BAR_EVENT:
            current_interval += 1
            if current_interval > total_intervals:
                current_interval = 0 

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
        screen.blit(gui.battle_text_surface1, (380, 150))
        screen.blit(gui.battle_text_surface2, (380, 190))
        screen.blit(gui.battle_text_surface3, (380, 230))
        screen.blit(gui.battle_text_surface4, (380, 290))

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
    
    # Draw Loading Bar
    fill_width = (current_interval / total_intervals) * 720
    pygame.draw.rect(screen, (255,255,255), gui.loading_bar_rect, 2)
    filled_rect = pygame.Rect(gui.loading_bar_rect.x, gui.loading_bar_rect.y, fill_width, 20)
    pygame.draw.rect(screen, (0,255,0), filled_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
