class Equipment:
    def __init__(self, vit, str, fort, dex, agi, health, eqtype):
        self.vit = vit  # Vitality - Effects Health Points
        self.str = str  # Strength - Effects Damage
        self.fort = fort  # Fortitude - Effects Defense
        self.dex = dex  # Dexterity - Effects Hit Chance
        self.agi = agi  # Agility - Effects Evade Chance
        self.health = health  # Health Value
        self.eq_type = eqtype  # Type of equipment


class Armor(Equipment):
    def __init__(self, defense, vit, str, fort, dex, agi, health, eqtype):
        super().__init__(vit, str, fort, dex, agi, health, eqtype)
        self.defense = defense  # Base Defense Value on Equip


class Weapon(Equipment):
    def __init__(self, attack, vit, str, fort, dex, agi, health, eqtype):
        super().__init__(vit, str, fort, dex, agi, health, eqtype)
        self.attack = attack  # Base Defense Value on Equip


class Jewelry(Equipment):
    def __init__(self, attack, defense, drop, vit, str, fort, dex, agi, health, eqtype):
        super().__init__(vit, str, fort, dex, agi, health, eqtype)
        self.attack = attack
        self.defense = defense  # Base Defense Value on Equip
        self.drop_chance = drop
