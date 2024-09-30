import random
import pygame

class Item:
    # List for iteration
    all_items = []
    # Dictionary for stat names
    stat_names = {
        0: 'vit',
        1: 'str',
        2: 'fort',
        3: 'dex',
        4: 'agi',
        5: 'health',
        6: 'defense',
        7: 'attack',
        8: 'drop_chance'
    }
    def __init__(self, image_path):
        # Item stats
        self.vit = 0  # Vitality - Effects Health Points
        self.str = 0  # Strength - Effects Damage
        self.fort = 0  # Fortitude - Effects Defense
        self.dex = 0  # Dexterity - Effects Hit Chance
        self.agi = 0  # Agility - Effects Evade Chance
        self.health = 0  # Health Value
        self.defense = 0  # Defense Value
        self.attack = 0  # Attack Value
        self.drop_chance = 0    # Drop chance
        self.base_range = [2,7]
        
        # Item type
        self.eq_type = ''  # Type of equipment

        # item rarity
        self.rarity = '' # Rarity of the item
        self.rarity_value = 0
        self.rarity_color = '#bdbdbd'
        self.stats_rollable = 0

        # Item image
        self.surface = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.pos = None

        Item.all_items.append(self)

    @property
    def item_score(self):
        return round(self.vit + self.str + self.fort + self.dex + self.agi + (self.health/4) + (self.defense/2) +
                        (self.attack/2.5) + (self.drop_chance*2))

    def resize(self,size):
        return pygame.transform.scale(self.surface,(size,size))
    def item_strength(self, active_enemy):
        return active_enemy.drop
    
    def roll_item(self, active_enemy):
  
        def roll_rarity(self):
            #get random float
            roll = random.random()
            #determine rarity based on roll
            if roll > 0.99:
                self.rarity = 'legendary'
                # multiplier value based on rarity
                self.rarity_value = 2.5
                # Number of different stats that can be rolled on an item
                self.stats_rollable = [4,6]
                # change item background color based on rarity
                self.rarity_color = (255, 178, 0)
                # roll for easter egg item
                secret_roll = random.random()
                if secret_roll > 0.99:
                    self.eq_type = 'gat'
                    self.rarity_value = 4
                    self.stats_rollable = [4,6]
                    self.rarity_color = (243, 107, 0)
            elif roll > .90:
                self.rarity = 'epic'
                self.rarity_value = 1.8
                self.stats_rollable = [3,5]
                self.rarity_color = (175, 0, 236)
            elif roll > .70:
                self.rarity = 'rare'
                self.rarity_value = 1.4
                self.stats_rollable = [3,4]
                self.rarity_color = (41, 158, 255)
            elif roll > .40:
                self.rarity = 'uncommon'
                self.rarity_value = 1.2
                self.stats_rollable = [2,3]
                self.rarity_color = (13, 255, 50)
            elif roll <= .40:
                self.rarity = 'common'
                self.rarity_value = 1
                self.stats_rollable = [1,3]
                self.rarity_color = (248, 248, 248)
                
        roll_rarity(self)

        if self.eq_type == 'gat':
            pass
        else:
            eq_num = random.randint(1,5)
            num_stats = random.randint(self.stats_rollable[0], self.stats_rollable[1])
            match eq_num:
                case 1:
                    self.eq_type = 'armor'
                    stats = [0,1,2,3,4,5,6]
                case 2:
                    self.eq_type = 'weapon'
                    stats = [0,1,2,3,4,7]
                case 3:
                    self.eq_type = 'jewelry'
                    stats = [0,1,2,3,4,5,6,7,8]
                case 4:
                    self.eq_type = 'helm'
                    stats = [0,1,2,3,4,5,6]
                case 5:
                    self.eq_type = 'boot'
                    stats = [0,1,2,3,4,5,6]

            num_item_stats = random.sample(stats, num_stats)
            print(str(num_item_stats))
            for x in num_item_stats:
                value = random.randint(self.base_range[0], self.base_range[1])
                calc_value = round(value * self.rarity_value * active_enemy.drop_strength)
                stat_name = self.stat_names[x]
                setattr(self, stat_name, calc_value)  # assign the rolled value to the stat attribute

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
        # Draw grid
        for x in range(self.col):
            for y in range(self.rows):
                rect = (self.x + (self.box_size + self.border)*x + self.border, self.y + (self.box_size + self.border)*y + self.border, self.box_size, self.box_size)
                # Change color of square based on rarity
                if self.items[x][y]:
                    color = self.items[x][y].rarity_color
                else:
                    color = '#bdbdbd'  # default color
                pygame.draw.rect(screen,color,rect)
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

