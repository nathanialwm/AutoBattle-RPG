class Player:
  def __init__(self, vit, str, fort, dex, agi, health, temphealth, defense, attack,
               hitchance, evadechance, inventorysize, statpoints, level, exp):
    self.vit = vit # Vitality - Effects Health Points
    self.str = str # Strength - Effects Damage
    self.fort = fort # Fortitude - Effects Defense
    self.dex = dex # Dexterity - Effects Hit Chance
    self.agi = agi # Agility - Effects Evade Chance
    self.health = health # Players Health Value
    self.temp_health = temphealth # Players health value during combat
    self.defense = defense # Players base defense stat
    self.attack = attack # player base attack stat
    self.hit = hitchance # Players chance to hit
    self.evade = evadechance # Players chance to evade an attack
    self.inventory_size = inventorysize # The amount of empty inventory slots
    self.stat_points = statpoints # Stat points available to spend. Player gets 5 per level
    self.level = level # Players character level
    self.exp = exp # Experience the player has earned
