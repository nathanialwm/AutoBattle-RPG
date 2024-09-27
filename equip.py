import random

class Equipment:
    def __init__(self, vit, str, fort, dex, agi, health, eqtype, rarity):
        self.vit = vit  # Vitality - Effects Health Points
        self.str = str  # Strength - Effects Damage
        self.fort = fort  # Fortitude - Effects Defense
        self.dex = dex  # Dexterity - Effects Hit Chance
        self.agi = agi  # Agility - Effects Evade Chance
        self.health = health  # Health Value
        self.eq_type = eqtype  # Type of equipment
        self.rarity = rarity # Rarity of the item

    def item_strength(self, active_enemy):
        return active_enemy.drop
    
    def roll_rarity(self):
        #get random float
        roll = random.Random()
        #determine rarity based on roll
        if roll >= 0.99:
            self.rarity = 'legendary'
            # roll for easter egg item
            secret_roll = random.Random()
            if secret_roll > 0.99:
                self.eq_type = 'gat'
        elif roll >= .85:
            self.rarity = 'epic'
        elif roll >= .65:
            self.rarity = 'rare'
        elif roll >= .35:
            self.rarity = 'uncommon'
        elif roll < .35:
            self.rarity = 'common'

class Armor(Equipment):
    def __init__(self, defense, vit, str, fort, dex, agi, health, eqtype):
        super().__init__(vit, str, fort, dex, agi, health, eqtype)
        self.defense = defense  # Base Defense Value on Equip

        @property
        def item_score(self):
            return round(self.vit + self.str + self.fort + self.dex + self.agi + (self.health/4) + (self.defense/2))

class Weapon(Equipment):
    def __init__(self, attack, vit, str, fort, dex, agi, eqtype):
        super().__init__(vit, str, fort, dex, agi, eqtype)
        self.attack = attack  # Base Defense Value on Equip

        @property
        def item_score(self):
            return round(self.vit + self.str + self.fort + self.dex + self.agi + (self.attack/2.5))

class Jewelry(Equipment):
    def __init__(self, attack, defense, drop, vit, str, fort, dex, agi, health, eqtype):
        super().__init__(vit, str, fort, dex, agi, health, eqtype)
        self.attack = attack
        self.defense = defense  # Base Defense Value on Equip
        self.drop_chance = drop

        @property
        def item_score(self):
            return round(self.vit + self.str + self.fort + self.dex + self.agi + (self.health/4) + (self.defense/2) +
                         (self.attack/2.5) + (self.drop_chance*2))
