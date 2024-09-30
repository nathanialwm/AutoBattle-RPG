import equip
import random

class Player:
  def __init__(self, vit, str, fort, dex, agi, inventorysize, num_items, statpoints, level, exp, exp_needed):
    self.vit = vit # Vitality - Effects Health Points
    self.str = str # Strength - Effects Damage
    self.fort = fort # Fortitude - Effects Defense
    self.dex = dex # Dexterity - Effects Hit Chance
    self.agi = agi # Agility - Effects Evade Chance
    self.inventory_size = inventorysize # The amount of inventory player can have
    self.num_items = num_items # the amount of items the player currently has
    self.stat_points = statpoints # Stat points available to spend. Player gets 5 per level
    self.level = level # Players character level
    self.exp = exp # Experience the player has earned
    self.exp_needed = exp_needed # Expereince required to level

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

  def player_this_attack(self):
          this_attack = random.randint(self.min_attack, self.max_attack)
          return this_attack

  def level_up(self):
      self.exp = self.exp - self.exp_needed
      self.level += 1
      self.stat_points += 3
      self.exp_needed = round((self.level *3) + self.exp_needed ** 1.005)
      if self.level % 2 == 0:
         self.vit += 1; self.str += 1; self.fort += 1; self.dex += 1; self.agi += 1

  def spend_stat_points(self):
    pass

  def change_equip(self):
    pass

p1 = Player(vit=5, str=5, fort=5, dex=5, agi=5, inventorysize=20, num_items=0, statpoints=0, level=1, exp=0, exp_needed=5)

