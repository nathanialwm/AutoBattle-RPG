import random
import pygame

class Item:
    all_items = []
    def __init__(self, image_path):
        
        # self.vit = vit  # Vitality - Effects Health Points
        # self.str = str  # Strength - Effects Damage
        # self.fort = fort  # Fortitude - Effects Defense
        # self.dex = dex  # Dexterity - Effects Hit Chance
        # self.agi = agi  # Agility - Effects Evade Chance
        # self.health = health  # Health Value
        # self.eq_type = eqtype  # Type of equipment
        # self.rarity = rarity # Rarity of the item
        self.image = pygame.image.load(image_path).convert_alpha()
        self.surface = self.image
        self.pos = None

        Item.all_items.append(self)

    def resize(self,size):
        return pygame.transform.scale(self.surface,(size,size))
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

class Armor(Item):
    def __init__(self, defense, vit, str, fort, dex, agi, health, eqtype):
        super().__init__(vit, str, fort, dex, agi, health, eqtype)
        self.defense = defense  # Base Defense Value on Equip

        @property
        def item_score(self):
            return round(self.vit + self.str + self.fort + self.dex + self.agi + (self.health/4) + (self.defense/2))

class Weapon(Item):
    def __init__(self, attack, vit, str, fort, dex, agi, eqtype):
        super().__init__(vit, str, fort, dex, agi, eqtype)
        self.attack = attack  # Base Defense Value on Equip

        @property
        def item_score(self):
            return round(self.vit + self.str + self.fort + self.dex + self.agi + (self.attack/2.5))

class Jewelry(Item):
    def __init__(self, attack, defense, drop, vit, str, fort, dex, agi, health, eqtype):
        super().__init__(vit, str, fort, dex, agi, health, eqtype)
        self.attack = attack
        self.defense = defense  # Base Defense Value on Equip
        self.drop_chance = drop

        @property
        def item_score(self):
            return round(self.vit + self.str + self.fort + self.dex + self.agi + (self.health/4) + (self.defense/2) +
                         (self.attack/2.5) + (self.drop_chance*2))

class Inventory:
    def __init__(self):
        self.rows = 2
        self.col = 10
        self.items = [[None for _ in range(self.rows)] for _ in range(self.col)]
        self.box_size = 65
        self.x = 124
        self.y = 470
        self.border = 3
    
    #draw everything
    def draw(self, screen):
        #draw background
        pygame.draw.rect(screen,(60,60,60),
                         (self.x,self.y,(self.box_size + self.border)*self.col + self.border,(self.box_size + self.border)*self.rows + self.border))
        for x in range(self.col):
            for y in range(self.rows):
                rect = (self.x + (self.box_size + self.border)*x + self.border, self.y + (self.box_size + self.border)*y + self.border, self.box_size, self.box_size)
                pygame.draw.rect(screen,('#bdbdbd'),rect)
                if self.items[x][y]:
                    screen.blit(self.items[x][y].resize(55), (rect[0] +5, rect[1] +5, rect[2], rect[3]))
                    
    #get the square that the mouse is over
    def Get_pos(self):
        mouse = pygame.mouse.get_pos()
        
        x = mouse[0] - self.x
        y = mouse[1] - self.y
        x = x//(self.box_size + self.border)
        y = y//(self.box_size + self.border)
        return (x,y)
    
    #add an item/s
    def get_next_available_space(self, item):
        for y in range(len(self.items[0])):
            for x in range(len(self.items)):
                if not self.items[x][y]:
                    self.items[x][y] = item
                    return (x, y)
        return None