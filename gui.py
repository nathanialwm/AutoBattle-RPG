import pygame
from player import p1

pygame.init()
pygame.display.set_mode((960, 680))
# Setup text and menu items that will always display
game_menu_font = pygame.font.Font('fonts/Handjet-Regular.ttf', 50)
battle_result_font = pygame.font.Font('fonts/Handjet-Regular.ttf', 24)
top_stat_font = pygame.font.Font('fonts/Roboto-Regular.ttf', 18)
player_stat_font = pygame.font.Font('fonts/Handjet-Regular.ttf', 40)
# Top Stats
stat_level_surface = top_stat_font.render('Level: ' + str(p1.level), True, 'Black')
stat_level_rect = stat_level_surface.get_rect(topleft=(50, 15))
stat_exp_surface = top_stat_font.render('Exp to Level: ' + str(p1.exp_needed - p1.exp), True, 'Black')
stat_exp_rect = stat_exp_surface.get_rect(topleft=(290, 15))
stat_stats_surface = top_stat_font.render('Stat Points: ' + str(p1.stat_points), True, 'Black')
stat_stats_rect = stat_stats_surface.get_rect(topright=(670, 15))
stat_inventory_surface = top_stat_font.render('Inventory Free: ' + str(p1.inventory_size - p1.num_items), True, 'Black')
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
mouse_icon_rect = mouse_icon_surface.get_rect(midtop=(240, 140))

giant_rat_icon_surface = pygame.image.load('images/Icons/icon_giant_rat.jpg').convert_alpha()
giant_rat_icon_surface = pygame.transform.scale(giant_rat_icon_surface, (180, 180))
giant_rat_icon_rect = giant_rat_icon_surface.get_rect(midtop=(240, 140))

rabid_dog_icon_surface = pygame.image.load('images/Icons/icon_rabid_dog.jpg').convert_alpha()
rabid_dog_icon_surface = pygame.transform.scale(rabid_dog_icon_surface, (180, 180))
rabid_dog_icon_rect = rabid_dog_icon_surface.get_rect(midtop=(240, 140))

skeleton_icon_surface = pygame.image.load('images/Icons/icon_skeleton.jpg').convert_alpha()
skeleton_icon_surface = pygame.transform.scale(skeleton_icon_surface, (180, 180))
skeleton_icon_rect = skeleton_icon_surface.get_rect(midtop=(240, 140))

thief_icon_surface = pygame.image.load('images/Icons/icon_thief.jpg').convert_alpha()
thief_icon_surface = pygame.transform.scale(thief_icon_surface, (180, 180))
thief_icon_rect = thief_icon_surface.get_rect(midtop=(240, 140))

zombie_icon_surface = pygame.image.load('images/Icons/icon_zombie.jpg').convert_alpha()
zombie_icon_surface = pygame.transform.scale(zombie_icon_surface, (180, 180))
zombie_icon_rect = zombie_icon_surface.get_rect(midtop=(240, 140))

yeti_icon_surface = pygame.image.load('images/Icons/icon_yeti.jpg').convert_alpha()
yeti_icon_surface = pygame.transform.scale(yeti_icon_surface, (180, 180))
yeti_icon_rect = yeti_icon_surface.get_rect(midtop=(240, 140))

vampire_icon_surface = pygame.image.load('images/Icons/icon_vampire.jpg').convert_alpha()
vampire_icon_surface = pygame.transform.scale(vampire_icon_surface, (180, 180))
vampire_icon_rect = vampire_icon_surface.get_rect(midtop=(240, 140))

minotaur_icon_surface = pygame.image.load('images/Icons/icon_minotaur.jpg').convert_alpha()
minotaur_icon_surface = pygame.transform.scale(minotaur_icon_surface, (180, 180))
minotaur_icon_rect = minotaur_icon_surface.get_rect(midtop=(240, 140))

dragon_icon_surface = pygame.image.load('images/Icons/icon_dragon.jpg').convert_alpha()
dragon_icon_surface = pygame.transform.scale(dragon_icon_surface, (180, 180))
dragon_icon_rect = dragon_icon_surface.get_rect(midtop=(240, 140))

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

# Stats screen
available_stats_surface = game_menu_font.render('Available Points: ' + str(p1.stat_points), True, 'Black')
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
title_vit_surface = player_stat_font.render('Vitality: ' + str(p1.vit), True, 'Black')
title_vit_rect = title_vit_surface.get_rect(topleft=(180, 205))

title_str_surface = player_stat_font.render('Strength: ' + str(p1.str), True, 'Black')
title_str_rect = title_str_surface.get_rect(topleft=(180, 285))

title_fort_surface = player_stat_font.render('Fortitude: ' + str(p1.fort), True, 'Black')
title_fort_rect = title_fort_surface.get_rect(topleft=(180, 365))

title_dex_surface = player_stat_font.render('Dexterity: ' + str(p1.dex), True, 'Black')
title_dex_rect = title_dex_surface.get_rect(topleft=(180, 445))

title_agi_surface = player_stat_font.render('Agility: ' + str(p1.agi), True, 'Black')
title_agi_rect = title_agi_surface.get_rect(topleft=(180, 525))

# stat explanations


# Update all battle reliant texts
def update_battle_texts():
    # call global variables
    global stat_level_surface, stat_exp_surface, stat_stats_surface, stat_inventory_surface, available_stats_surface
    global title_vit_surface, title_str_surface, title_fort_surface, title_dex_surface, title_agi_surface
    #Top stats
    stat_level_surface = top_stat_font.render('Level: ' + str(p1.level), True, 'Black')
    stat_exp_surface = top_stat_font.render('Exp to Level: ' + str(p1.exp_needed - p1.exp), True, 'Black')
    stat_stats_surface = top_stat_font.render('Stat Points: ' + str(p1.stat_points), True, 'Black')
    stat_inventory_surface = top_stat_font.render('Inventory Free: ' + str(p1.inventory_size - p1.num_items), True, 'Black')
    # Stats page
    available_stats_surface = game_menu_font.render('Available Points: ' + str(p1.stat_points), True, 'Black')
    title_vit_surface = player_stat_font.render('Vitality: ' + str(p1.vit), True, 'Black')
    title_str_surface = player_stat_font.render('Strength: ' + str(p1.str), True, 'Black')
    title_fort_surface = player_stat_font.render('Fortitude: ' + str(p1.fort), True, 'Black')
    title_dex_surface = player_stat_font.render('Dexterity: ' + str(p1.dex), True, 'Black')
    title_agi_surface = player_stat_font.render('Agility: ' + str(p1.agi), True, 'Black')
