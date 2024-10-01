import numpy as np
import random
import pygame
import player
import enemy
import equip

# Set mouse as active enemy when game loads
active_enemy = enemy.Enemy.all_enemies[0]
all_items = equip.Item.all_items
# pygame setup
pygame.init()
screen = pygame.display.set_mode((960, 680))
pygame.display.set_caption('AutoBattle RPG')
clock = pygame.time.Clock()
running = True

player_inventory = equip.Inventory()

# Set all surfaces and rects for gui items
game_menu_font = pygame.font.Font('fonts/Handjet-Regular.ttf', 50)
battle_result_font = pygame.font.Font('fonts/Handjet-Regular.ttf', 24)
top_stat_font = pygame.font.Font('fonts/Roboto-Regular.ttf', 18)
player_stat_font = pygame.font.Font('fonts/Handjet-Regular.ttf', 40)
# Top Stats
stat_level_surface = top_stat_font.render('Level: ' + str(player.p1.level), True, 'Black')
stat_level_rect = stat_level_surface.get_rect(topleft=(50, 15))
stat_exp_surface = top_stat_font.render('Exp to Level: ' + str(player.p1.exp_needed - player.p1.exp), True, 'Black')
stat_exp_rect = stat_exp_surface.get_rect(topleft=(290, 15))
stat_stats_surface = top_stat_font.render('Stat Points: ' + str(player.p1.stat_points), True, 'Black')
stat_stats_rect = stat_stats_surface.get_rect(topright=(670, 15))
stat_inventory_surface = top_stat_font.render('Inventory Free: ' + str(player.p1.inventory_size - player.p1.num_items), True, 'Black')
stat_inventory_rect = stat_inventory_surface.get_rect(topright=(910, 15))
# Top Menu
menu_battle_surface = game_menu_font.render('Battle', True, 'Black')
menu_battle_rect = menu_battle_surface.get_rect(midtop=(240, 45))
menu_equip_surface = game_menu_font.render('Equipment', True, 'Black')
menu_equip_rect = menu_equip_surface.get_rect(midtop=(480, 45))
menu_stats_surface = game_menu_font.render('Stats', True, 'Black')
menu_stats_rect = menu_stats_surface.get_rect(midtop=(720, 45))

# Create visuals and menus for battle screen
battle_text_surface1 = battle_result_font.render('',True, 'Black')
battle_text_surface2 = battle_result_font.render('',True, 'Black')
battle_text_surface3 = battle_result_font.render('',True, 'Black')
battle_text_surface4 = battle_result_font.render('',True, 'Black')

loading_bar_rect = pygame.Rect(120, 105, 720, 20)
# Enemy Portrait Icons

mouse_icon_surface = pygame.image.load('images/Icons/icon_mouse.jpg').convert_alpha()
mouse_icon_surface = pygame.transform.scale(mouse_icon_surface, (180, 180))
mouse_icon_rect = mouse_icon_surface.get_rect(midtop=(240, 180))

giant_rat_icon_surface = pygame.image.load('images/Icons/icon_giant_rat.jpg').convert_alpha()
giant_rat_icon_surface = pygame.transform.scale(giant_rat_icon_surface, (180, 180))
giant_rat_icon_rect = giant_rat_icon_surface.get_rect(midtop=(240, 180))

rabid_dog_icon_surface = pygame.image.load('images/Icons/icon_rabid_dog.jpg').convert_alpha()
rabid_dog_icon_surface = pygame.transform.scale(rabid_dog_icon_surface, (180, 180))
rabid_dog_icon_rect = rabid_dog_icon_surface.get_rect(midtop=(240, 180))

skeleton_icon_surface = pygame.image.load('images/Icons/icon_skeleton.jpg').convert_alpha()
skeleton_icon_surface = pygame.transform.scale(skeleton_icon_surface, (180, 180))
skeleton_icon_rect = skeleton_icon_surface.get_rect(midtop=(240, 180))

thief_icon_surface = pygame.image.load('images/Icons/icon_thief.jpg').convert_alpha()
thief_icon_surface = pygame.transform.scale(thief_icon_surface, (180, 180))
thief_icon_rect = thief_icon_surface.get_rect(midtop=(240, 180))

zombie_icon_surface = pygame.image.load('images/Icons/icon_zombie.jpg').convert_alpha()
zombie_icon_surface = pygame.transform.scale(zombie_icon_surface, (180, 180))
zombie_icon_rect = zombie_icon_surface.get_rect(midtop=(240, 180))

yeti_icon_surface = pygame.image.load('images/Icons/icon_yeti.jpg').convert_alpha()
yeti_icon_surface = pygame.transform.scale(yeti_icon_surface, (180, 180))
yeti_icon_rect = yeti_icon_surface.get_rect(midtop=(240, 180))

vampire_icon_surface = pygame.image.load('images/Icons/icon_vampire.jpg').convert_alpha()
vampire_icon_surface = pygame.transform.scale(vampire_icon_surface, (180, 180))
vampire_icon_rect = vampire_icon_surface.get_rect(midtop=(240, 180))

minotaur_icon_surface = pygame.image.load('images/Icons/icon_minotaur.jpg').convert_alpha()
minotaur_icon_surface = pygame.transform.scale(minotaur_icon_surface, (180, 180))
minotaur_icon_rect = minotaur_icon_surface.get_rect(midtop=(240, 180))

dragon_icon_surface = pygame.image.load('images/Icons/icon_dragon.jpg').convert_alpha()
dragon_icon_surface = pygame.transform.scale(dragon_icon_surface, (180, 180))
dragon_icon_rect = dragon_icon_surface.get_rect(midtop=(240, 180))

# Buttons for enemy types | Button size 340x42
enemy_mouse_surface = pygame.image.load('images/Buttons/button_mouse.png').convert_alpha()
enemy_mouse_rect = enemy_mouse_surface.get_rect(topleft=(134, 442))

enemy_giant_rat_surface = pygame.image.load('images/Buttons/button_giant-rat.png').convert_alpha()
enemy_giant_rat_rect = enemy_giant_rat_surface.get_rect(topleft=(134, 487))

enemy_rabid_dog_surface = pygame.image.load('images/Buttons/button_rabid-dog.png').convert_alpha()
enemy_rabid_dog_rect = enemy_rabid_dog_surface.get_rect(topleft=(134, 532))

enemy_skeleton_surface = pygame.image.load('images/Buttons/button_skeleton.png').convert_alpha()
enemy_skeleton_rect = enemy_skeleton_surface.get_rect(topleft=(134, 577))

boss_thief_surface = pygame.image.load('images/Buttons/button_thief.png').convert_alpha()
boss_thief_rect = boss_thief_surface.get_rect(topleft=(134, 622))

enemy_zombie_surface = pygame.image.load('images/Buttons/button_zombie.png').convert_alpha()
enemy_zombie_rect = enemy_zombie_surface.get_rect(topleft=(486, 442))

enemy_yeti_surface = pygame.image.load('images/Buttons/button_yeti.png').convert_alpha()
enemy_yeti_rect = enemy_yeti_surface.get_rect(topleft=(486, 487))

enemy_vampire_surface = pygame.image.load('images/Buttons/button_vampire.png').convert_alpha()
enemy_vampire_rect = enemy_vampire_surface.get_rect(topleft=(486, 532))

enemy_minotaur_surface = pygame.image.load('images/Buttons/button_minotaur.png').convert_alpha()
enemy_minotaur_rect = enemy_minotaur_surface.get_rect(topleft=(486, 577))

boss_dragon_surface = pygame.image.load('images/Buttons/button_dragon.png').convert_alpha()
boss_dragon_rect = boss_dragon_surface.get_rect(topleft=(486, 622))

# lists to allow looping through and indexing gui variables
enemy_surfaces = [mouse_icon_surface,giant_rat_icon_surface,rabid_dog_icon_surface,skeleton_icon_surface,
                  thief_icon_surface,zombie_icon_surface,yeti_icon_surface,vampire_icon_surface,
                  minotaur_icon_surface,dragon_icon_surface]
enemy_rects = [mouse_icon_rect,giant_rat_icon_rect,rabid_dog_icon_rect,skeleton_icon_rect,
                  thief_icon_rect,zombie_icon_rect,yeti_icon_rect,vampire_icon_rect,
                  minotaur_icon_rect,dragon_icon_rect]
enemy_button_rects = [enemy_mouse_rect, enemy_giant_rat_rect, enemy_rabid_dog_rect, enemy_skeleton_rect,
                      boss_thief_rect, enemy_zombie_rect, enemy_yeti_rect, enemy_vampire_rect, enemy_minotaur_rect,
                      boss_dragon_rect]
# Equip Screen

# Bottom icons

# Stats screen
available_stats_surface = game_menu_font.render('Available Points: ' + str(player.p1.stat_points), True, 'Black')
available_stats_rect = available_stats_surface.get_rect(midtop=(480, 130))
# Plus Buttons
plus_vit_surface = pygame.image.load('images/Icons/icon_plus.png').convert_alpha()
plus_vit_surface = pygame.transform.scale(plus_vit_surface, (80, 80))
plus_vit_rect = plus_vit_surface.get_rect(topleft=(670, 200))

plus_str_surface = pygame.image.load('images/Icons/icon_plus.png').convert_alpha()
plus_str_surface = pygame.transform.scale(plus_str_surface, (80, 80))
plus_str_rect = plus_str_surface.get_rect(topleft=(670, 280))

plus_fort_surface = pygame.image.load('images/Icons/icon_plus.png').convert_alpha()
plus_fort_surface = pygame.transform.scale(plus_fort_surface, (80, 80))
plus_fort_rect = plus_fort_surface.get_rect(topleft=(670, 360))

plus_dex_surface = pygame.image.load('images/Icons/icon_plus.png').convert_alpha()
plus_dex_surface = pygame.transform.scale(plus_dex_surface, (80, 80))
plus_dex_rect = plus_dex_surface.get_rect(topleft=(670, 440))

plus_agi_surface = pygame.image.load('images/Icons/icon_plus.png').convert_alpha()
plus_agi_surface = pygame.transform.scale(plus_agi_surface, (80, 80))
plus_agi_rect = plus_agi_surface.get_rect(topleft=(670, 520))
# create a list of buttons to make looping possible
stat_plus_rects = [plus_vit_rect, plus_str_rect, plus_fort_rect, plus_dex_rect, plus_agi_rect]

# Stat names
title_vit_surface = player_stat_font.render('Vitality: ' + str(player.p1.vit), True, 'Black')
title_vit_rect = title_vit_surface.get_rect(topleft=(180, 205))

title_str_surface = player_stat_font.render('Strength: ' + str(player.p1.str), True, 'Black')
title_str_rect = title_str_surface.get_rect(topleft=(180, 285))

title_fort_surface = player_stat_font.render('Fortitude: ' + str(player.p1.fort), True, 'Black')
title_fort_rect = title_fort_surface.get_rect(topleft=(180, 365))

title_dex_surface = player_stat_font.render('Dexterity: ' + str(player.p1.dex), True, 'Black')
title_dex_rect = title_dex_surface.get_rect(topleft=(180, 445))

title_agi_surface = player_stat_font.render('Agility: ' + str(player.p1.agi), True, 'Black')
title_agi_rect = title_agi_surface.get_rect(topleft=(180, 525))

# Stat explanations
explain_vit_surface = battle_result_font.render('Increases health points', True, 'Black')
explain_vit_rect = explain_vit_surface.get_rect(topleft=(200, 250))

explain_str_surface = battle_result_font.render('Increases min and max damage', True, 'Black')
explain_str_rect = explain_str_surface.get_rect(topleft=(200, 330))

explain_fort_surface = battle_result_font.render('Increases damage mitigation', True, 'Black')
explain_fort_rect = explain_fort_surface.get_rect(topleft=(200, 410))

explain_dex_surface = battle_result_font.render('Increases chance to hit', True, 'Black')
explain_dex_rect = explain_dex_surface.get_rect(topleft=(200, 490))

explain_agi_surface = battle_result_font.render('Increases chance to evade damage', True, 'Black')
explain_agi_rect = explain_agi_surface.get_rect(topleft=(200, 570))

# player equipment
def draw_player_equips():
    global helm_rect, armor_rect, boot_rect, neck_rect, wep_rect
    #helm slot
    helm_border_rect = pygame.Rect(620,160,65,65)
    pygame.draw.rect(screen, '#5f5f5f', helm_border_rect)
    helm_rect = pygame.Rect(625,165,55,55)
    pygame.draw.rect(screen, '#ababab', helm_rect)

    #armor slot
    armor_border_rect = pygame.Rect(620,260,65,65)
    pygame.draw.rect(screen, '#5f5f5f', armor_border_rect)
    armor_rect = pygame.Rect(625,265,55,55)
    pygame.draw.rect(screen, '#ababab', armor_rect)

    #boots slot
    boot_border_rect = pygame.Rect(620,360,65,65)
    pygame.draw.rect(screen, '#5f5f5f', boot_border_rect)
    boot_rect = pygame.Rect(625,365,55,55)
    pygame.draw.rect(screen, '#ababab', boot_rect)

    # necklace slot
    neck_border_rect = pygame.Rect(720,210,65,65)
    pygame.draw.rect(screen, '#5f5f5f', neck_border_rect)
    neck_rect = pygame.Rect(725,215,55,55)
    pygame.draw.rect(screen, '#ababab', neck_rect)

    # weapon slot
    wep_border_rect = pygame.Rect(520,260,65,65)
    pygame.draw.rect(screen, '#5f5f5f', wep_border_rect)
    wep_rect = pygame.Rect(525,265,55,55)
    pygame.draw.rect(screen, '#ababab', wep_rect)

# update all dynamic battle reliant texts
def update_battle_texts():
    # call global variables
    global stat_level_surface, stat_exp_surface, stat_stats_surface, stat_inventory_surface, available_stats_surface
    global title_vit_surface, title_str_surface, title_fort_surface, title_dex_surface, title_agi_surface
    #Top stats
    stat_level_surface = top_stat_font.render('Level: ' + str(player.p1.level), True, 'Black')
    stat_exp_surface = top_stat_font.render('Exp to Level: ' + str(player.p1.exp_needed - player.p1.exp), True, 'Black')
    stat_stats_surface = top_stat_font.render('Stat Points: ' + str(player.p1.stat_points), True, 'Black')
    stat_inventory_surface = top_stat_font.render('Inventory Free: ' + str(player.p1.inventory_size - player.p1.num_items), True, 'Black')
    # Stats page
    available_stats_surface = game_menu_font.render('Available Points: ' + str(player.p1.stat_points), True, 'Black')
    title_vit_surface = player_stat_font.render('Vitality: ' + str(player.p1.vit), True, 'Black')
    title_str_surface = player_stat_font.render('Strength: ' + str(player.p1.str), True, 'Black')
    title_fort_surface = player_stat_font.render('Fortitude: ' + str(player.p1.fort), True, 'Black')
    title_dex_surface = player_stat_font.render('Dexterity: ' + str(player.p1.dex), True, 'Black')
    title_agi_surface = player_stat_font.render('Agility: ' + str(player.p1.agi), True, 'Black')

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
        global battle_text_surface1, battle_text_surface2, battle_text_surface3, battle_text_surface4
        
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
            roll_for_item = random.randint(1,10)
            for _ in range(0,10):
                new_item = equip.Item()
                new_item.roll_item(active_enemy)
                player_inventory.get_next_available_space(new_item)
            if roll_for_item == 10:
                new_item = equip.Item()
                new_item.roll_item(active_enemy)
                player_inventory.get_next_available_space(new_item)
                player.p1.num_items += 1
            # if player exp causes a level up
            while player.p1.exp >= player.p1.exp_needed:
                player.p1.level_up()
                level_gained += 1


            battle_text1 = "You defeated the " + active_enemy.name + ". You attacked the " + active_enemy.name + " " + str(player_total_attacks) 
            battle_text2 = "times, hitting " + str(player_hits) + " times, dealing " + str(player_total_damage) + " damage. The " + active_enemy.name 
            battle_text3 = "attacked you " + str(enemy_total_attacks) + " times, hitting " + str(enemy_hits) + " dealing " + str(enemy_total_damage) + " damage to you."
            battle_text4 = "You gained " + str(exp_gained) + " experience points and leveled up " + str(level_gained) + " times."
            battle_text_surface1 = battle_result_font.render(battle_text1, True, 'Black')
            battle_text_surface2 = battle_result_font.render(battle_text2, True, 'Black')
            battle_text_surface3 = battle_result_font.render(battle_text3, True, 'Black')
            battle_text_surface4 = battle_result_font.render(battle_text4, True, 'Black')
            break

        # if player loses
        if player.p1.temp_health <= 0:
            player_total_attacks = player_hits + player_misses
            enemy_total_attacks = enemy_hits + enemy_misses
            battle_text1 = "You died to the " + active_enemy.name + ". You attacked the " + active_enemy.name + " " + str(player_total_attacks) 
            battle_text2 = " times, hitting " + str(player_hits) + " times, dealing " + str(player_total_damage) + " damage. The " + active_enemy.name 
            battle_text3 = " attacked you " + str(enemy_total_attacks) + " times, hitting " + str(enemy_hits) + " dealing " + str(enemy_total_damage) + " damage to you."
            battle_text4 = "You gained 0 experience points and leveled up 0 times."
            battle_text_surface1 = battle_result_font.render(battle_text1, True, 'Black')
            battle_text_surface2 = battle_result_font.render(battle_text2, True, 'Black')
            battle_text_surface3 = battle_result_font.render(battle_text3, True, 'Black')
            battle_text_surface4 = battle_result_font.render(battle_text4, True, 'Black')
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
            update_battle_texts()
            # put top of screen stats on screen
            stat_level_surface = top_stat_font.render('Level: ' + str(player.p1.level), True, 'Black')
            stat_exp_surface = top_stat_font.render('Exp to Level: ' + str(player.p1.exp_needed - player.p1.exp), True, 'Black')
            stat_stats_surface = top_stat_font.render('Stat Points: ' + str(player.p1.stat_points), True, 'Black')
            stat_inventory_surface = top_stat_font.render('Inventory Free: ' + str(player.p1.inventory_size - player.p1.num_items), True, 'Black')
            available_stats_surface = game_menu_font.render('Available Points: ' + str(player.p1.stat_points), True, 'Black')

        # Event for bar animation
        if event.type == BAR_EVENT:
            current_interval += 1
            if current_interval > total_intervals:
                current_interval = 1

        # Create all click events
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # Clicking between menus
            if menu_battle_rect.collidepoint(pos):
                battle_screen = True
                equip_screen = False
                stat_screen = False
            if menu_equip_rect.collidepoint(pos):
                battle_screen = False
                equip_screen = True
                stat_screen = False
            if menu_stats_rect.collidepoint(pos):
                battle_screen = False
                equip_screen = False
                stat_screen = True

            # Clicking between enemy types
            for index, rect in enumerate(enemy_button_rects):
                if rect.collidepoint(pygame.mouse.get_pos()) and battle_screen:
                    for en in enemy.Enemy.all_enemies:
                        en.battling = False
                    enemy.Enemy.all_enemies[index].battling = True
                    active_enemy = enemy.Enemy.all_enemies[index]
            
            # Find out which stat increase button is clicked
            for i, rect in enumerate(stat_plus_rects):
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
                    update_battle_texts()
                    break  # Exit the loop after the first match
            
            for item in all_items:
                if item.rect.collidepoint(pygame.mouse.get_pos()) and equip_screen:
                    if pygame.mouse.get_pressed()[0]:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            player_inventory.remove_item_image(item)
                            all_items.remove(item)
                            del item                          
                            player.p1.num_items -= 1

                    if pygame.mouse.get_pressed()[2]:
                        player_inventory.remove_item_image(item)
                        player.p1.num_items -= 1
                        player_inventory.move_item_image(screen, item)
                            
                        

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

    # put top stats on screen
    screen.blit(stat_level_surface, stat_level_rect)
    screen.blit(stat_exp_surface, stat_exp_rect)
    screen.blit(stat_stats_surface, stat_stats_rect)
    screen.blit(stat_inventory_surface, stat_inventory_rect)
    # Put menu items on screen
    screen.blit(menu_battle_surface, menu_battle_rect)
    screen.blit(menu_equip_surface, menu_equip_rect)
    screen.blit(menu_stats_surface, menu_stats_rect)

    # Create screen elements for each of the three 'pages'
    # Create battle screen
    if battle_screen:
        # Put enemy button objects on screen
        screen.blit(enemy_mouse_surface, enemy_mouse_rect)
        screen.blit(enemy_giant_rat_surface, enemy_giant_rat_rect)
        screen.blit(enemy_rabid_dog_surface, enemy_rabid_dog_rect)
        screen.blit(enemy_skeleton_surface, enemy_skeleton_rect)
        screen.blit(boss_thief_surface, boss_thief_rect)
        screen.blit(enemy_zombie_surface, enemy_zombie_rect)
        screen.blit(enemy_yeti_surface, enemy_yeti_rect)
        screen.blit(enemy_vampire_surface, enemy_vampire_rect)
        screen.blit(enemy_minotaur_surface, enemy_minotaur_rect)
        screen.blit(boss_dragon_surface, boss_dragon_rect)

        # Battle Text
        screen.blit(battle_text_surface1, (370, 190))
        screen.blit(battle_text_surface2, (370, 230))
        screen.blit(battle_text_surface3, (370, 270))
        screen.blit(battle_text_surface4, (370, 330))

        # Determine which monster is active
        for index, en in enumerate(enemy.Enemy.all_enemies):
            if en.battling:
                screen.blit(enemy_surfaces[index], enemy_rects[index])
             
             
    # Create equipment screen
    if equip_screen:
        player_inventory.draw(screen)
        draw_player_equips()
        for item in all_items:
            if item.rect.collidepoint(pygame.mouse.get_pos()):
                tooltip_font = pygame.font.Font('fonts/Roboto-Regular.ttf', 20)
                tooltip_text = tooltip_font.render('Item Score: ' + str(item.item_score), True, 'Black')
                screen.blit(tooltip_text, (650, 445))


    # create stat screen
    if stat_screen:
        # plus buttons
        screen.blit(available_stats_surface, available_stats_rect)
        screen.blit(plus_vit_surface, plus_vit_rect)
        screen.blit(plus_str_surface, plus_str_rect)
        screen.blit(plus_fort_surface, plus_fort_rect)
        screen.blit(plus_dex_surface, plus_dex_rect)
        screen.blit(plus_agi_surface, plus_agi_rect)
        # stat name text
        screen.blit(title_vit_surface, title_vit_rect)
        screen.blit(title_str_surface, title_str_rect)
        screen.blit(title_fort_surface, title_fort_rect)
        screen.blit(title_dex_surface, title_dex_rect)
        screen.blit(title_agi_surface, title_agi_rect)
        # stat explanation text
        screen.blit(explain_vit_surface, explain_vit_rect)
        screen.blit(explain_str_surface, explain_str_rect)
        screen.blit(explain_fort_surface, explain_fort_rect)
        screen.blit(explain_dex_surface, explain_dex_rect)
        screen.blit(explain_agi_surface, explain_agi_rect)
    
    # Draw Loading Bar
    fill_width = (current_interval / total_intervals) * 720
    pygame.draw.rect(screen, (255,255,255), loading_bar_rect, 2)
    filled_rect = pygame.Rect(loading_bar_rect.x, loading_bar_rect.y, fill_width, 20)
    pygame.draw.rect(screen, (0,255,0), filled_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
