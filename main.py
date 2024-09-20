import numpy as np
import random as ran
import pygame
import player
import enemy
import equip

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

# Setup text and menu items that will always display
# Top Menu
game_menu_font = pygame.font.Font('fonts/Handjet-Regular.ttf', 50)
menu_battle_surface = game_menu_font.render('Battle', True, 'Black')
menu_battle_rect = menu_battle_surface.get_rect(midtop=(240, 20))
menu_equip_surface = game_menu_font.render('Equipment', True, 'Black')
menu_equip_rect = menu_equip_surface.get_rect(midtop=(480, 20))
menu_stats_surface = game_menu_font.render('Stats', True, 'Black')
menu_stats_rect = menu_stats_surface.get_rect(midtop=(720, 20))

# Create visuals and menus for battle screen
# Enemy Portrait Icons
mouse_icon_surface = pygame.image.load('images/Icons/icon_mouse.jpg').convert_alpha()
mouse_icon_surface = pygame.transform.scale(mouse_icon_surface, (180, 180))
mouse_icon_rect = mouse_icon_surface.get_rect(midtop=(240, 100))

giant_rat_icon_surface = pygame.image.load('images/Icons/icon_giant_rat.jpg').convert_alpha()
giant_rat_icon_surface = pygame.transform.scale(giant_rat_icon_surface, (180, 180))
giant_rat_icon_rect = giant_rat_icon_surface.get_rect(midtop=(240, 100))

rabid_dog_icon_surface = pygame.image.load('images/Icons/icon_rabid_dog.jpg').convert_alpha()
rabid_dog_icon_surface = pygame.transform.scale(rabid_dog_icon_surface, (180, 180))
rabid_dog_icon_rect = rabid_dog_icon_surface.get_rect(midtop=(240, 100))

skeleton_icon_surface = pygame.image.load('images/Icons/icon_skeleton.jpg').convert_alpha()
skeleton_icon_surface = pygame.transform.scale(skeleton_icon_surface, (180, 180))
skeleton_icon_rect = skeleton_icon_surface.get_rect(midtop=(240, 100))

thief_icon_surface = pygame.image.load('images/Icons/icon_thief.jpg').convert_alpha()
thief_icon_surface = pygame.transform.scale(thief_icon_surface, (180, 180))
thief_icon_rect = thief_icon_surface.get_rect(midtop=(240, 100))

zombie_icon_surface = pygame.image.load('images/Icons/icon_zombie.jpg').convert_alpha()
zombie_icon_surface = pygame.transform.scale(zombie_icon_surface, (180, 180))
zombie_icon_rect = zombie_icon_surface.get_rect(midtop=(240, 100))

yeti_icon_surface = pygame.image.load('images/Icons/icon_yeti.jpg').convert_alpha()
yeti_icon_surface = pygame.transform.scale(yeti_icon_surface, (180, 180))
yeti_icon_rect = yeti_icon_surface.get_rect(midtop=(240, 100))

vampire_icon_surface = pygame.image.load('images/Icons/icon_vampire.jpg').convert_alpha()
vampire_icon_surface = pygame.transform.scale(vampire_icon_surface, (180, 180))
vampire_icon_rect = vampire_icon_surface.get_rect(midtop=(240, 100))

minotaur_icon_surface = pygame.image.load('images/Icons/icon_minotaur.jpg').convert_alpha()
minotaur_icon_surface = pygame.transform.scale(minotaur_icon_surface, (180, 180))
minotaur_icon_rect = minotaur_icon_surface.get_rect(midtop=(240, 100))

dragon_icon_surface = pygame.image.load('images/Icons/icon_dragon.jpg').convert_alpha()
dragon_icon_surface = pygame.transform.scale(dragon_icon_surface, (180, 180))
dragon_icon_rect = dragon_icon_surface.get_rect(midtop=(240, 100))

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

enemy_surfaces = [mouse_icon_surface,giant_rat_icon_surface,rabid_dog_icon_surface,skeleton_icon_surface,
                  thief_icon_surface,zombie_icon_surface,yeti_icon_surface,vampire_icon_surface,
                  minotaur_icon_surface,dragon_icon_surface]
enemy_rects = [mouse_icon_rect,giant_rat_icon_rect,rabid_dog_icon_rect,skeleton_icon_rect,
                  thief_icon_rect,zombie_icon_rect,yeti_icon_rect,vampire_icon_rect,
                  minotaur_icon_rect,dragon_icon_rect]
enemy_button_rects = [enemy_mouse_rect, enemy_giant_rat_rect, enemy_rabid_dog_rect, enemy_skeleton_rect,
                      boss_thief_rect, enemy_zombie_rect, enemy_yeti_rect, enemy_vampire_rect, enemy_minotaur_rect,
                      boss_dragon_rect]
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

            # Clicking between enemy types
            for index, rect in enumerate(enemy_button_rects):
                if rect.collidepoint(pygame.mouse.get_pos()) and battle_screen:
                    for enemy in iterable_enemy_objects:
                        enemy.battling = False
                    iterable_enemy_objects[index].battling = True

            

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
        # Determine which monster is active
        # if fight_enemy_statuses['fight_mouse']:
        #     screen.blit(mouse_icon_surface, mouse_icon_rect)
        # if fight_enemy_statuses['fight_giant_rat']:
        #     screen.blit(giant_rat_icon_surface, giant_rat_icon_rect)
        for index, enemy in enumerate(iterable_enemy_objects):
            if enemy.battling:
                screen.blit(enemy_surfaces[index], enemy_rects[index])


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
