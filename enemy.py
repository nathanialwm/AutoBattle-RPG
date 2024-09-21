import player



class Enemy:
    #Create array for looping through all existing enemies
    all_enemies = []
    # init
    def __init__(self, name, dex, agi, health, temphealth, defense, attack, exp, drop, battling):
        self.name = name # The string version of the name of the enemy
        self.dex = dex  # Dexterity - Effects Hit Chance
        self.agi = agi  # Agility - Effects Evade Chance
        self.health = health  # Enemy Health Value
        self.temp_health = temphealth  # Enemy health value during combat
        self.defense = defense  # Enemy defense stat
        self.attack = attack # Enemy attack stat
        self.exp_award = exp # Experience awarded to player after defeating this enemy
        self.drop_strength = drop # Base number to determine strength of items dropped by this enemy
        self.battling = battling # Boolean to determine if this enemy is active
        
        # appened each created enemy to all_enemies
        Enemy.all_enemies.append(self)

    def enemy_hit_chance(self):
        h = min(100, max(0, 50+30*((self.dex - player.p1.agi) / player.p1.agi)))
        return h
    
    def player_hit_chance(self):
        h = min(100, max(0, 50+30*((player.p1.dex - self.agi) / self.agi)))
        return h
        


class Boss(Enemy):
    def __init__(self, name, dex, agi, health, temphealth, defense, attack, exp, drop, battling, regen, crit):
        super().__init__(name, dex, agi, health, temphealth, defense, attack, exp, drop, battling)
        self.regen = regen  # Boss Enemy HP Regeneration per turn
        self.crit = crit  # Boss Enemy chance to do 1.5x damage


# Create the enemy objects
Mouse = Enemy(name="Mouse",dex=4,agi=4,health=10,temphealth=10,defense=5,attack=5,
              exp=5,drop=1,battling=False)

Giant_Rat = Enemy(name="Giant Rat",dex=15,agi=13,health=45,temphealth=45,defense=12,attack=19,
                  exp=23,drop=1.1,battling=False)

Rabid_Dog = Enemy(name="Rabid Dog",dex=22,agi=33,health=80,temphealth=80,defense=14,attack=55,
                  exp=46,drop=1.15,battling=False)

Skeleton = Enemy(name="Skeleton",dex=41,agi=39,health=200,temphealth=200,defense=22,attack=47,
                 exp=99,drop=1.2,battling=False)

Thief = Boss(name="Thief",dex=66,agi=66,health=400,temphealth=400,defense=38,attack=75,
             exp=240,drop=1.3,battling=False,regen=8,crit=15)

Zombie = Enemy(name="Zombie",dex=90,agi=60,health=1000,temphealth=1000,defense=80,attack=88,
               exp=404,drop=1.35,battling=False)

Yeti = Enemy(name="Yeti",dex=120,agi=100,health=1320,temphealth=1320,defense=144,attack=135,
             exp=829,drop=1.4,battling=False)

Vampire = Enemy(name="Vampire",dex=180,agi=142,health=2200,temphealth=2200,defense=156,attack=160,
                exp=1502,drop=1.45,battling=False)

Minotaur = Enemy(name="Minotaur",dex=174,agi=168,health=4000,temphealth=4000,defense=220,attack=260,
                 exp=3360,drop=1.5,battling=False)

Dragon = Boss(name="Dragon",dex=404,agi=355,health=9999,temphealth=9999,defense=404,attack=404,
              exp=12999,drop=1.8,battling=False,regen=80,crit=33)

