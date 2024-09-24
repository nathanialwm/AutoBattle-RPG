import equip
import random

class Player:
  def __init__(self, vit, str, fort, dex, agi, health, temphealth, defense, min_attack, max_attack,
                inventorysize, num_items, statpoints, level, exp, exp_needed):
    self.vit = vit # Vitality - Effects Health Points
    self.str = str # Strength - Effects Damage
    self.fort = fort # Fortitude - Effects Defense
    self.dex = dex # Dexterity - Effects Hit Chance
    self.agi = agi # Agility - Effects Evade Chance
    self.health = self.vit * 4 # Players Health = vit * 4 plus any from equips
    self.temp_health = self.health # Players health value during combat
    self.defense = self.fort * 2 # Players defense = fort * 2 plus any from equips
    self.min_attack = round(self.str * 1.5) # player attack = strength *2 + any from equips
    self.max_attack = round(self.str * 3)
    self.inventory_size = inventorysize # The amount of inventory player can have
    self.num_items = num_items # the amount of items the player currently has
    self.stat_points = statpoints # Stat points available to spend. Player gets 5 per level
    self.level = level # Players character level
    self.exp = exp # Experience the player has earned
    self.exp_needed = exp_needed # Expereince required to level

  def player_this_attack(self):
          this_attack = random.randint(self.min_attack, self.max_attack)
          return this_attack

  def level_up(self):
      self.exp = self.exp - self.exp_needed
      self.level += 1
      self.stat_points += 3
      self.exp_needed = round((self.level *3) + self.exp_needed ** 1.005)

  def spend_stat_points(self):
    pass

  def change_equip(self):
    pass

p1 = Player(vit=5, str=5, fort=5, dex=5, agi=5, health=20, temphealth=20, defense=5, min_attack=8, max_attack=15,
            inventorysize=10, num_items=0, statpoints=0, level=1, exp=0, exp_needed=5)

