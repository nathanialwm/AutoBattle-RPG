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
    def __init__(self):
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
        self.image = None
        self.rect = None
        self.pos = None

        Item.all_items.append(self)

    @property
    def item_score(self):
        return (round(self.vit + self.str + self.fort + self.dex + self.agi + (self.health/4) + (self.defense/2) +
                        (self.attack/2.5) + (self.drop_chance*2)))*5

    def resize(self,size):
        return pygame.transform.scale(self.image,(size,size))
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
                self.rarity_color = '#ffb12b'
                # roll for easter egg item
                secret_roll = random.random()
                if secret_roll > 0.99:
                    self.eq_type = 'gat'
                    self.rarity_value = 4
                    self.stats_rollable = [4,6]
                    self.rarity_color = '#fa7000'
            elif roll > .90:
                self.rarity = 'epic'
                self.rarity_value = 1.8
                self.stats_rollable = [3,5]
                self.rarity_color = '#a92de3'
            elif roll > .70:
                self.rarity = 'rare'
                self.rarity_value = 1.4
                self.stats_rollable = [3,4]
                self.rarity_color = '#5b83f0'
            elif roll > .40:
                self.rarity = 'uncommon'
                self.rarity_value = 1.2
                self.stats_rollable = [2,3]
                self.rarity_color = '#45ed61'
            elif roll <= .40:
                self.rarity = 'common'
                self.rarity_value = 1
                self.stats_rollable = [1,3]
                self.rarity_color = '#ebebeb'
                
        roll_rarity(self)

        if self.eq_type == 'gat':
            self.image = pygame.image.load('images/Equipment/gun.png')
        else:
            # roll for number of stats on item
            eq_num = random.randint(1,5)
            num_stats = random.randint(self.stats_rollable[0], self.stats_rollable[1])
            # set lists for equipment images
            armors = [pygame.image.load('images/Equipment/armor1.png'),pygame.image.load('images/Equipment/armor2.png'),
                      pygame.image.load('images/Equipment/armor3.png')]
            helms = [pygame.image.load('images/Equipment/helm1.png'),pygame.image.load('images/Equipment/helm2.png'),
                      pygame.image.load('images/Equipment/helm3.png')]
            boots = [pygame.image.load('images/Equipment/boot1.png'),pygame.image.load('images/Equipment/boot2.png'),
                      pygame.image.load('images/Equipment/boot3.png')]
            necks =  [pygame.image.load('images/Equipment/neck1.png'),pygame.image.load('images/Equipment/neck2.png')]
            weps = [pygame.image.load('images/Equipment/axe1.png'),pygame.image.load('images/Equipment/axe2.png'),
                      pygame.image.load('images/Equipment/axe3.png'), pygame.image.load('images/Equipment/sword1.png'),
                      pygame.image.load('images/Equipment/sword2.png'), pygame.image.load('images/Equipment/sword3.png'),
                      pygame.image.load('images/Equipment/bow1.png'), pygame.image.load('images/Equipment/bow2.png'),
                      pygame.image.load('images/Equipment/bow3.png')]
            # determine stats available and images used based on type
            match eq_num:
                case 1:
                    self.eq_type = 'armor'
                    self.image = armors[random.randint(0,2)]
                    stats = [0,1,2,3,4,5,6]
                case 2:
                    self.eq_type = 'weapon'
                    self.image = weps[random.randint(0,8)]
                    stats = [0,1,2,3,4,7]
                case 3:
                    self.eq_type = 'jewelry'
                    self.image = necks[random.randint(0,1)]
                    stats = [0,1,2,3,4,5,6,7,8]
                case 4:
                    self.eq_type = 'helm'
                    self.image = helms[random.randint(0,2)]
                    stats = [0,1,2,3,4,5,6]
                case 5:
                    self.eq_type = 'boot'
                    self.image = boots[random.randint(0,2)]
                    stats = [0,1,2,3,4,5,6]
            self.rect = self.image.get_rect()

            num_item_stats = random.sample(stats, num_stats)
            print(str(num_item_stats))
            for x in num_item_stats:
                value = random.randint(self.base_range[0], self.base_range[1])
                calc_value = round(value * self.rarity_value * active_enemy.drop_strength)
                stat_name = self.stat_names[x]
                setattr(self, stat_name, calc_value)  # assign the rolled value to the stat attribute

class Inventory:
    def __init__(self):
        self.equipment = {
            'helm': None,
            'armor': None,
            'boot': None,
            'neck': None,
            'weapon': None
        }
        self.rows = 2
        self.col = 10
        self.items = [[None for _ in range(self.rows)] for _ in range(self.col)]
        self.box_size = 65
        self.x = 124
        self.y = 470
        self.border = 3
    
    #draw everything
    def draw(self, screen):

        equipment_positions = {
            'helm': (625, 165),
            'armor': (625, 265),
            'boot': (625, 365),
            'neck': (725, 215),
            'weapon': (525, 265)
        }
        for eq_type, item in self.equipment.items():
            if item:
                screen.blit(item.image.resize(55), equipment_positions[eq_type])
        #draw background
        pygame.draw.rect(screen,(60,60,60),
                         (self.x,self.y,(self.box_size + self.border)*self.col + self.border,(self.box_size + self.border)*self.rows + self.border))
        # Draw grid
        for x in range(self.col):
            for y in range(self.rows):
                rect = pygame.Rect(self.x + (self.box_size + self.border)*x + self.border, self.y + (self.box_size + self.border)*y + self.border, self.box_size, self.box_size)
                item = self.items[x][y]
                if item:
                    item.rect = rect
                # Change color of square based on rarity
                if self.items[x][y]:
                    color = self.items[x][y].rarity_color
                else:
                    color = '#bdbdbd'  # default color
                pygame.draw.rect(screen,color,rect)
                if self.items[x][y]:
                    screen.blit(self.items[x][y].resize(55), (rect[0] +5, rect[1] +5, rect[2], rect[3]))

    def remove_item_image(self, item):
    # Remove the item's image from the grid
        for x in range(self.col):
            for y in range(self.rows):
                if self.items[x][y] == item:
                    self.items[x][y] = None
                    return

    def move_item_image(self, screen, item):
    # Remove the item's image from the grid
        for x in range(self.col):
            for y in range(self.rows):
                if self.items[x][y] == item:
                    self.items[x][y] = None
                    self.equipment[item.eq_type] = item
                    return
   
    
    #add an item/s
    def get_next_available_space(self, item):
        for y in range(len(self.items[0])):
            for x in range(len(self.items)):
                if not self.items[x][y]:
                    self.items[x][y] = item
                    return (x, y)
        return None

