class Enemy:
    def __init__(self, dex, agi, health, temphealth, defense, attack, hitchance, evadechance, exp, drop):
        self.dex = dex  # Dexterity - Effects Hit Chance
        self.agi = agi  # Agility - Effects Evade Chance
        self.health = health  # Enemy Health Value
        self.temp_health = temphealth  # Enemy health value during combat
        self.defense = defense  # Enemy defense stat
        self.attack = attack # Enemy attack stat
        self.hit = hitchance  # Enemy chance to hit
        self.evade = evadechance  # Enemy chance to evade an attack
        self.exp_award = exp # Experience awarded to player after defeating this enemy
        self.drop_strength = drop # Base number to determine strength of items dropped by this enemy


class Boss(Enemy):
    def __init__(self, dex, agi, health, temphealth, defense, attack, hitchance, evadechance, exp, drop, regen, crit):
        super().__init__(dex, agi, health, temphealth, defense, attack, hitchance, evadechance, exp, drop)
        self.regen = regen  # Boss Enemy HP Regeneration per turn
        self.crit = crit  # Boss Enemy chance to do 1.5x damage


Mouse = Enemy(1,1,10,10,1,1,1,2,1)
Giant_Rat = Enemy(1,1,10,10,1,1,1,2,1)
Rabid_Dog = Enemy(1,1,10,10,1,1,1,2,1)
Skeleton = Enemy(1,1,10,10,1,1,1,2,1)
Thief = Boss(1,1,10,10,1,1,1,2,1,1,1)
Zombie = Enemy(1,1,10,10,1,1,1,2,1)
Yeti = Enemy(1,1,10,10,1,1,1,2,1)
Vampire = Enemy(1,1,10,10,1,1,1,2,1)
Minotaur = Enemy(1,1,10,10,1,1,1,2,1)
Dragon = Boss(1,1,10,10,1,1,1,2,1,1,1)
