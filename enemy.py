import pygame.image


class Enemy:
    def __init__(self, dex, agi, health, temphealth, defense, attack, hitchance, evadechance, exp, drop, battling):
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
        self.battling = battling # Boolean to determine if this enemy is active


class Boss(Enemy):
    def __init__(self, dex, agi, health, temphealth, defense, attack, hitchance, evadechance,
                 exp, drop, battling, regen, crit):
        super().__init__(dex, agi, health, temphealth, defense, attack, hitchance, evadechance, exp, drop, battling)
        self.regen = regen  # Boss Enemy HP Regeneration per turn
        self.crit = crit  # Boss Enemy chance to do 1.5x damage


# Create the enemy objects
Mouse = Enemy(dex=1,agi=1,health=10,temphealth=10,defense=1,attack=1,
              hitchance=1,evadechance=2,exp=1,drop=1,battling=False)

Giant_Rat = Enemy(dex=1,agi=1,health=10,temphealth=10,defense=1,attack=1,
                  hitchance=1,evadechance=2,exp=1,drop=1,battling=False)

Rabid_Dog = Enemy(dex=1,agi=1,health=10,temphealth=10,defense=1,attack=1,
                  hitchance=1,evadechance=2,exp=1,drop=1,battling=False)

Skeleton = Enemy(dex=1,agi=1,health=10,temphealth=10,defense=1,attack=1,
                 hitchance=1,evadechance=2,exp=1,drop=1,battling=False)

Thief = Boss(dex=1,agi=1,health=10,temphealth=10,defense=1,attack=1,
             hitchance=1,evadechance=2,exp=1,drop=1,battling=False,regen=1,crit=1)

Zombie = Enemy(dex=1,agi=1,health=10,temphealth=10,defense=1,attack=1,
               hitchance=1,evadechance=2,exp=1,drop=1,battling=False)

Yeti = Enemy(dex=1,agi=1,health=10,temphealth=10,defense=1,attack=1,
             hitchance=1,evadechance=2,exp=1,drop=1,battling=False)

Vampire = Enemy(dex=1,agi=1,health=10,temphealth=10,defense=1,attack=1,
                hitchance=1,evadechance=2,exp=1,drop=1,battling=False)

Minotaur = Enemy(dex=1,agi=1,health=10,temphealth=10,defense=1,attack=1,
                 hitchance=1,evadechance=2,exp=1,drop=1,battling=False)

Dragon = Boss(dex=1,agi=1,health=10,temphealth=10,defense=1,attack=1,
              hitchance=1,evadechance=2,exp=1,drop=1,battling=False,regen=1,crit=1)
