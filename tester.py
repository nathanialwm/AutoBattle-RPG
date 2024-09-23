import numpy as np
import random
import pygame
import player
import enemy
import equip
import gui
import main as m
from math import e


x =0 
y=0
def player_mitigation(x, y):
        mit = round((.95 * ( 1 / (1 + e**(-1.35*(x / y - 1 ))))), 3)
        return mit

for i in range(0,20):
    y = 0
    x += 5
    for i in range(0,20):
        y+=5
        print("x: " + str(x)+ " y: " + str(y) + " " + str(player_mitigation(x,y)))
