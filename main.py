import numpy as np
import random
import pygame
import player
import enemy
import equip
import gui

# Set mouse as active enemy when game loads
active_enemy = enemy.Enemy.all_enemies[0]

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
current_interval = 1

BAR_EVENT = pygame.USEREVENT + 2
bar_timer = pygame.time.set_timer(BAR_EVENT, 500)

# Battle logic
def battle_instance():
    # define variables to tracks hits and misses
    player_misses = 0
    player_hits = 0
    player_total_attacks = player_hits + player_misses

    enemy_misses = 0
    enemy_hits = 0
    enemy_total_attacks = enemy_hits + enemy_misses
    # Set variables to track total damage dealt
    player_total_damage = 0
    enemy_total_damage = 0
    # Setup special boss stat trackers
    boss_crits = 0
    boss_regen = 0

    # track winning condition
    exp_gained = 0
    level_gained = 0

    while player.p1.temp_health > 0 and active_enemy.temp_health > 0:
        
        # If the player hits
        if active_enemy.player_hit_chance():
            player_damage = round(player.p1.player_this_attack() * (1 - active_enemy.enemy_mitigation()))
            active_enemy.temp_health = active_enemy.temp_health - player_damage
            player_hits += 1
            player_total_damage += player_damage
        else:
            player_misses += 1
        
        if active_enemy.enemy_hit_chance():
            enemy_damage = round(active_enemy.enemy_this_attack() * (1 - active_enemy.player_mitigation()))
            player.p1.temp_health = player.p1.temp_health - enemy_damage
            enemy_hits += 1
            enemy_total_damage += enemy_damage
        else:
            enemy_misses += 1

        # if player wins
        if active_enemy.temp_health <= 0:
            player_total_attacks = player_hits + player_misses
            enemy_total_attacks = enemy_hits + enemy_misses
            exp_gained = active_enemy.exp_award
            player.p1.exp += exp_gained
            # if player exp causes a level up
            while player.p1.exp >= player.p1.exp_needed:
                player.p1.level_up()
                level_gained += 1


            battle_text1 = "You defeated the " + active_enemy.name + ". You attacked the " + active_enemy.name + " " + str(player_total_attacks) 
            battle_text2 = "times, hitting " + str(player_hits) + " times, dealing " + str(player_total_damage) + " damage. The " + active_enemy.name 
            battle_text3 = "attacked you " + str(enemy_total_attacks) + " times, hitting " + str(enemy_hits) + " dealing " + str(enemy_total_damage) + " damage to you."
            battle_text4 = "You gained " + str(exp_gained) + " experience points and leveled up " + str(level_gained) + " times."
            gui.battle_text_surface1 = gui.battle_result_font.render(battle_text1, True, 'Black')
            gui.battle_text_surface2 = gui.battle_result_font.render(battle_text2, True, 'Black')
            gui.battle_text_surface3 = gui.battle_result_font.render(battle_text3, True, 'Black')
            gui.battle_text_surface4 = gui.battle_result_font.render(battle_text4, True, 'Black')
            break

        # if player loses
        if player.p1.temp_health <= 0:
            player_total_attacks = player_hits + player_misses
            enemy_total_attacks = enemy_hits + enemy_misses
            battle_text1 = "You died to the " + active_enemy.name + ". You attacked the " + active_enemy.name + " " + str(player_total_attacks) 
            battle_text2 = " times, hitting " + str(player_hits) + " times, dealing " + str(player_total_damage) + " damage. The " + active_enemy.name 
            battle_text3 = " attacked you " + str(enemy_total_attacks) + " times, hitting " + str(enemy_hits) + " dealing " + str(enemy_total_damage) + " damage to you."
            battle_text4 = "You gained 0 experience points and leveled up 0 times."
            gui.battle_text_surface1 = gui.battle_result_font.render(battle_text1, True, 'Black')
            gui.battle_text_surface2 = gui.battle_result_font.render(battle_text2, True, 'Black')
            gui.battle_text_surface3 = gui.battle_result_font.render(battle_text3, True, 'Black')
            gui.battle_text_surface4 = gui.battle_result_font.render(battle_text4, True, 'Black')
            break
        
# Use switch case for stat plus buttons
while running:
    # Draw Menu items that are always visible
    screen.fill('#bdbdbd')
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Main Event for Battling. Triggers regardless of active screen
        if event.type == BATTLE_EVENT:
            # Main battle loop
            # Reset temp health if needed
            player.p1.temp_health = player.p1.health
            active_enemy.temp_health = active_enemy.health
            # Call main loop
            battle_instance()
            # put top of screen stats on screen
            gui.stat_level_surface = gui.top_stat_font.render('Level: ' + str(player.p1.level), True, 'Black')
            gui.stat_exp_surface = gui.top_stat_font.render('Exp to Level: ' + str(player.p1.exp_needed - player.p1.exp), True, 'Black')
            gui.stat_stats_surface = gui.top_stat_font.render('Stat Points: ' + str(player.p1.stat_points), True, 'Black')
            gui.stat_inventory_surface = gui.top_stat_font.render('Inventory Free: ' + str(player.p1.inventory_size - player.p1.num_items), True, 'Black')
            gui.available_stats_surface = gui.game_menu_font.render('Available Points: ' + str(player.p1.stat_points), True, 'Black')
            print(str(player.p1.agi))

        # Event for bar animation
        if event.type == BAR_EVENT:
            current_interval += 1
            if current_interval > total_intervals:
                current_interval = 1

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
                    for en in enemy.Enemy.all_enemies:
                        en.battling = False
                    enemy.Enemy.all_enemies[index].battling = True
                    active_enemy = enemy.Enemy.all_enemies[index]
            
            # Find out which stat increase button is clicked
            for i, rect in enumerate(gui.stat_plus_rects):
                if rect.collidepoint(pygame.mouse.get_pos()) and player.p1.stat_points > 0:
                    # update proper player stat
                    if i == 0:  # Vitality
                        player.p1.vit += 1
                    elif i == 1:  # Strength
                        player.p1.str += 1
                    elif i == 2:  # Fortitude
                        player.p1.fort += 1
                    elif i == 3:  # Dexterity
                        player.p1.dex += 1
                    elif i == 4:  # Agility
                        player.p1.agi += 1

                    # Deduct a stat point
                    player.p1.stat_points -= 1
                    # Update stat point GUIs
                    gui.available_stats_surface = gui.game_menu_font.render('Available Points: ' + str(player.p1.stat_points), True, 'Black')
                    gui.stat_stats_surface = gui.top_stat_font.render('Stat Points: ' + str(player.p1.stat_points), True, 'Black')
                    break  # Exit the loop after the first match

            

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

    # put top stats on screen
    screen.blit(gui.stat_level_surface, gui.stat_level_rect)
    screen.blit(gui.stat_exp_surface, gui.stat_exp_rect)
    screen.blit(gui.stat_stats_surface, gui.stat_stats_rect)
    screen.blit(gui.stat_inventory_surface, gui.stat_inventory_rect)
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
        screen.blit(gui.battle_text_surface1, (370, 150))
        screen.blit(gui.battle_text_surface2, (370, 190))
        screen.blit(gui.battle_text_surface3, (370, 230))
        screen.blit(gui.battle_text_surface4, (370, 290))

        # Determine which monster is active
        for index, en in enumerate(enemy.Enemy.all_enemies):
            if en.battling:
                screen.blit(gui.enemy_surfaces[index], gui.enemy_rects[index])
             
             
    # Create equipment screen
    if equip_screen:
        pass

    # create stat screen
    if stat_screen:
        # plus buttons
        screen.blit(gui.available_stats_surface, gui.available_stats_rect)
        screen.blit(gui.plus_vit_surface, gui.plus_vit_rect)
        screen.blit(gui.plus_str_surface, gui.plus_str_rect)
        screen.blit(gui.plus_fort_surface, gui.plus_fort_rect)
        screen.blit(gui.plus_dex_surface, gui.plus_dex_rect)
        screen.blit(gui.plus_agi_surface, gui.plus_agi_rect)
        # stat name text
        screen.blit(gui.title_vit_surface, gui.title_vit_rect)
    
    # Draw Loading Bar
    fill_width = (current_interval / total_intervals) * 720
    pygame.draw.rect(screen, (255,255,255), gui.loading_bar_rect, 2)
    filled_rect = pygame.Rect(gui.loading_bar_rect.x, gui.loading_bar_rect.y, fill_width, 20)
    pygame.draw.rect(screen, (0,255,0), filled_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
