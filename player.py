import random
import equip

class Player:
   def __init__(self):

      self.base_vit = 5 # base_vitality - Effects Health Points
      self.base_str = 5 # base_strength - Effects Damage
      self.base_fort = 5 # base_fortitude - Effects Defense
      self.base_dex = 5 # base_dexterity - Effects Hit Chance
      self.base_agi = 5 # base_agility - Effects Evade Chance

      self.equip_vit = 0 # Vitality gained from equipment
      self.equip_str = 0 # Strength gained from equipment
      self.equip_fort = 0 # Fortitude gained from equipment
      self.equip_dex = 0 # Dexterity gained from equipment
      self.equip_agi = 0 # Agility gained from equipment
      self.attack = 0 # attack gained from equipment
      self.defense = 0 # defense gained from equipment
      self.health = 0 # health gained from equipment
      self.drop_chance = 0 # drop chance gained from equipment

      self.inventory_size = 20 # The amount of inventory player can have
      self.num_items = 0 # the amount of items the player currently has

      self.stat_points = 0 # Stat points available to spend. Player gets 5 per level
      self.level = 1 # Players character level
      self.exp = 0 # Experience the player has earned
      self.exp_needed = 5 # Expereince required to level

   @property
   def vit(self):
      return self.base_vit + self.equip_vit # Full Vit Stat
   
   @vit.setter
   def vit(self, value):
        self.base_vit = value
   @property
   def str(self):
      return self.base_str + self.equip_str # Full Str Stat
   
   @str.setter
   def str(self, value):
        self.base_str = value

   @property
   def fort(self):   
      return self.base_fort + self.equip_fort # Full Fort Stat
   
   @fort.setter
   def fort(self, value):
        self.base_fort = value

   @property
   def dex(self):
      return self.base_dex + self.equip_dex # Full Dex Stat

   @dex.setter
   def dex(self, value):
        self.base_dex = value

   @property
   def agi(self):
      return self.base_agi + self.equip_agi # Full Agi Stat

   @agi.setter
   def agi(self, value):
        self.base_agi = value

   # dependant properties
   @property
   def real_health(self):
      return ((self.base_vit + self.equip_vit) * 4) + self.health

   def temp_health(self):
      return self.real_health

   @property
   def real_defense(self):
      return ((self.base_fort + self.equip_fort) * 2) + self.defense

   @property
   def min_attack(self):
      return round((self.base_str + self.equip_str) * 1.5) + self.attack

   @property
   def max_attack(self):
      return round((self.base_str + self.equip_str)* 3) + self.attack
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
         self.base_vit += 1; self.base_str += 1; self.base_fort += 1; self.base_dex += 1; self.base_agi += 1

   def update_equip_stats(self, inventory):
      self.equip_vit = 0
      self.equip_str = 0
      self.equip_fort = 0
      self.equip_dex = 0
      self.equip_agi = 0
      for item in inventory.equipment.values():
        if item is not None:
            self.equip_vit += item.vit
            self.equip_str += item.str
            self.equip_fort += item.fort
            self.equip_dex += item.dex
            self.equip_agi += item.agi
            self.attack += item.attack
            self.defense += item.defense
            self.health += item.health
            self.drop_chance += item.drop_chance

   def save_game(self):
      pass

   def load_game(self):
      pass
   
   def print_stats(self):
      print("Vitality: " + str(self.vit) + " Strength: " + str(self.str) + " Fortitude: " + str(self.fort) + " Dexterity: " + str(self.dex) + " Agility: " + str(self.agi))

p1 = Player()

