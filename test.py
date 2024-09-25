import numpy as np
import random
import player
import enemy
import equip
import gui
from math import e

########################################################################################################################
#           BATTLE SIMULATOR            BATTLE SIMULATOR            BATTLE SIMULATOR            BATTLE SIMULATOR
########################################################################################################################

player.p1.vit = 10
player.p1.str = 10
player.p1.fort = 10
player.p1.dex = 10
player.p1.agi = 10
wins = 0
loss = 0
active_enemy = enemy.Enemy.all_enemies[1]

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
        global wins, loss
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
            wins += 1
            player_total_attacks = player_hits + player_misses
            enemy_total_attacks = enemy_hits + enemy_misses
            exp_gained = active_enemy.exp_award
            player.p1.exp += exp_gained
            # if player exp causes a level up
            while player.p1.exp >= player.p1.exp_needed:
                player.p1.level_up()
                level_gained += 1
            break

        # if player loses
        if player.p1.temp_health <= 0:
            loss += 1
            player_total_attacks = player_hits + player_misses
            enemy_total_attacks = enemy_hits + enemy_misses
            break
        
for i in range(0,10000):
    player.p1.temp_health = player.p1.health
    active_enemy.temp_health = active_enemy.health
    # Call main loop
    battle_instance()

print("Wins:" +str(wins))
print("Losses: " +str(loss))

########################################################################################################################
#           BATTLE SIMULATOR            BATTLE SIMULATOR            BATTLE SIMULATOR            BATTLE SIMULATOR
########################################################################################################################


# Testing defense mitigation
# x =0 
# y=0
# def player_mitigation(x, y):
#         mit = round((.95 * ( 1 / (1 + e**(-1.35*(x / y - 1 ))))), 3)
#         return mit

# for i in range(0,20):
#     y = 0
#     x += 5
#     for i in range(0,20):
#         y+=5
#         print("x: " + str(x)+ " y: " + str(y) + " " + str(player_mitigation(x,y)))


# Testing damage dealt after mitigation
# for i in range(0,20):
#     player_damage = round(player.p1.player_this_attack() * (1 - m.active_enemy.enemy_mitigation()))
#     print(player_damage)

# a = 0
# for x in range(0,1000):
#     t = enemy.Mouse.enemy_hit_chance()
#     if t:
#         a += 1
#     else:
#         pass
# print(a)



