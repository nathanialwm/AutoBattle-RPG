import equip
import random

class Player:
  def __init__(self):
    self.vit = 5 # Vitality - Effects Health Points
    self.str = 5 # Strength - Effects Damage
    self.fort = 5 # Fortitude - Effects Defense
    self.dex = 5 # Dexterity - Effects Hit Chance
    self.agi = 5 # Agility - Effects Evade Chance
    self.inventory_size = 20 # The amount of inventory player can have
    self.num_items = 0 # the amount of items the player currently has
    self.stat_points = 0 # Stat points available to spend. Player gets 5 per level
    self.level = 1 # Players character level
    self.exp = 0 # Experience the player has earned
    self.exp_needed = 5 # Expereince required to level

# dependant properties
  @property
  def health(self):
    return self.vit * 4
  
  def temp_health(self):
     return self.health
  
  @property
  def defense(self):
     return self.fort * 2
  
  @property
  def min_attack(self):
     return round(self.str * 1.5)
  
  @property
  def max_attack(self):
     return round(self.str * 3)
   # Roll for player attack turn
  def player_this_attack(self):
          this_attack = random.randint(self.min_attack, self.max_attack)
          return this_attack
   #Player level up
  def level_up(self):
      self.exp = self.exp - self.exp_needed
      self.level += 1
      self.stat_points += 3
      self.exp_needed = round((self.level *3) + self.exp_needed ** 1.005)
      if self.level % 2 == 0:
         self.vit += 1; self.str += 1; self.fort += 1; self.dex += 1; self.agi += 1

  def change_equip(self):
    pass
  
  def save_game(self):
     pass
  
  def load_game(self):
     pass
  

p1 = Player()

