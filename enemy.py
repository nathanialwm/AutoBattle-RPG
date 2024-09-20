import pygame.image


class Enemy:
    def __init__(self, name, dex, agi, health, temphealth, defense, attack, hitchance, evadechance, exp, drop, battling):
        self.name = name # The string version of the name of the enemy
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
    def __init__(self, name, dex, agi, health, temphealth, defense, attack, hitchance, evadechance,
                 exp, drop, battling, regen, crit):
        super().__init__(name, dex, agi, health, temphealth, defense, attack, hitchance, evadechance, exp, drop, battling)
        self.regen = regen  # Boss Enemy HP Regeneration per turn
        self.crit = crit  # Boss Enemy chance to do 1.5x damage


# Create the enemy objects
Mouse = Enemy(name="Mouse",dex=1,agi=1,health=10,temphealth=10,defense=1,attack=1,
              hitchance=1,evadechance=2,exp=1,drop=1,battling=False)

Giant_Rat = Enemy(name="Giant Rat",dex=1,agi=1,health=10,temphealth=10,defense=1,attack=1,
                  hitchance=1,evadechance=2,exp=1,drop=1,battling=False)

Rabid_Dog = Enemy(name="Rabid Dog",dex=1,agi=1,health=10,temphealth=10,defense=1,attack=1,
                  hitchance=1,evadechance=2,exp=1,drop=1,battling=False)

Skeleton = Enemy(name="Skeleton",dex=1,agi=1,health=10,temphealth=10,defense=1,attack=1,
                 hitchance=1,evadechance=2,exp=1,drop=1,battling=False)

Thief = Boss(name="Thief",dex=1,agi=1,health=10,temphealth=10,defense=1,attack=1,
             hitchance=1,evadechance=2,exp=1,drop=1,battling=False,regen=1,crit=1)

Zombie = Enemy(name="Zombie",dex=1,agi=1,health=10,temphealth=10,defense=1,attack=1,
               hitchance=1,evadechance=2,exp=1,drop=1,battling=False)

Yeti = Enemy(name="Yeti",dex=1,agi=1,health=10,temphealth=10,defense=1,attack=1,
             hitchance=1,evadechance=2,exp=1,drop=1,battling=False)

Vampire = Enemy(name="Vampire",dex=1,agi=1,health=10,temphealth=10,defense=1,attack=1,
                hitchance=1,evadechance=2,exp=1,drop=1,battling=False)

Minotaur = Enemy(name="Minotaur",dex=1,agi=1,health=10,temphealth=10,defense=1,attack=1,
                 hitchance=1,evadechance=2,exp=1,drop=1,battling=False)

Dragon = Boss(name="Dragon",dex=1,agi=1,health=10,temphealth=10,defense=1,attack=1,
              hitchance=1,evadechance=2,exp=1,drop=1,battling=False,regen=1,crit=1)
