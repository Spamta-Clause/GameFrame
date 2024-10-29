from GameFrame import Level
from Objects.Ship import Ship
from Objects.Smash import Smash
from Objects.Laser_Cruiser import Laser_Cruiser
from Objects.Unstable import Unstable
from Objects.Ship_Cruiser import Ship_Cruiser
from Objects.Asteroid import Asteroid
from GameFrame import Globals
from Objects.Wave import Wave
from Objects.Heart import Heart
import random

class Game(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        #self.level = level
        self.set_background_image('background.png')

        
        

        #self.add_room_object(Unstable(self, 900, 500, 'boom.png', 32, 18, 3, ship, 150, 90,1))
        #self.add_room_object(Ship_Cruiser(self, 700, 500, 'ship.png', 29*3, 32*3, 0.75, ship, 3, 350, 75))
        self.basic_startup()
        self.level_one()
    
    def basic_startup(self):
        match Globals.current_powerup:
            case "shield-1":
                self.shield = 1
            case "shield-2":
                self.shield = 2
            case "shield-3":
                self.shield = 3
            case _:
                self.shield = 0

        self.hearts = []
        print(self.shield)
        for i in range(Globals.armour):
            self.hearts.append(Heart(self, 20 + (i * 50), 20))
            self.add_room_object(self.hearts[i])
        self.shield_hearts = []

        for i in range(self.shield):
            new_heart = Heart(self, 20 + (i * 50), 50)
            self.shield_hearts.append(new_heart)
            new_heart.set_value('shield')
            self.add_room_object(self.shield_hearts[i])
        self.hearts_arrays = [self.hearts, self.shield_hearts]

        self.ship = Ship(self, 100, Globals.SCREEN_HEIGHT/2, 58, 64, 45, 1)
        self.add_room_object(self.ship)

    def remove_heart(self, damage):
        for i in range(damage):
            final_array = self.hearts_arrays[-1]
            if len(final_array) == 0 or final_array == None:
                self.hearts_arrays.pop()
                final_array = self.hearts_arrays[-1]
            print(final_array)
            print(len(final_array))
            final_heart = final_array[-1]
            
            final_array.pop(-1)
            if final_heart.value == 'shield':
                self.delete_object(final_heart)
            else:
                final_heart.set_value('empty')
            if len(self.hearts) == 0:
                Globals.next_level = Globals.levels.index('Menu')
                self.running = False

    def update_hearts(self, type):
        for heart in self.hearts:
            heart.set_value(type)
    def shield_hearts(self, amount):
        for heart in range(amount):
            self.hearts[heart].set_value('shield')

    def level_one(self):
        first_wave = Wave()
        smash_1 = Smash(self, 200, 500, 'spinny.png', 32, 18, 3, self.ship, 1, 1, 20, first_wave)
        laser_cruiser_1 = Laser_Cruiser(self, 200, 500, 'laser_cruiser\\laser_cruiser_1.png', 48, 48, 0.75, self.ship, 3, 150, 30,first_wave)
        first_wave.enemies = [smash_1,laser_cruiser_1]
        first_wave.total_enemies = [smash_1,laser_cruiser_1]
        first_wave.interval = 120
        first_wave.room = self
        first_wave.spawn_next() 
        self.add_room_object(Asteroid(self,800,random.randint(200,500),1))
        self.add_room_object(Asteroid(self,800,random.randint(200,500),2))
        self.add_room_object(Asteroid(self,800,random.randint(200,500),3))
        

