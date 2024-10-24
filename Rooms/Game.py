from GameFrame import Level
from Objects.Ship import Ship
from Objects.Smash import Smash
from Objects.Laser_Cruiser import Laser_Cruiser
from Objects.Unstable import Unstable
from Objects.Ship_Cruiser import Ship_Cruiser
from Objects.Asteroid import Asteroid
from GameFrame import Globals
from Objects.Wave import Wave
import random
import copy
class Game(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        #self.level = level
        self.set_background_image('background.png')

        #self.add_room_object(Unstable(self, 900, 500, 'boom.png', 32, 18, 3, ship, 150, 90,1))
        #self.add_room_object(Ship_Cruiser(self, 700, 500, 'ship.png', 29*3, 32*3, 0.75, ship, 3, 350, 75))

    def level_one(self):
        ship = Ship(self, 100, 100, 'ship.png', 58, 64, Globals.speed, Globals.armour, 30,1)
        self.add_room_object(ship)
        first_wave = Wave()
        first_wave.enemies = [Smash(self, 200, 500, 'spinny.png', 32, 18, 3, ship, 1, 1, 20, first_wave),Laser_Cruiser(self, 200, 500, 'laser_cruiser\\laser_cruiser_1.png', 48, 48, 0.75, ship, 3, 150, 30,first_wave)]
        first_wave.total_enemies = copy.deepcopy(first_wave.enemies)
        first_wave.interval = 60
        first_wave.room = self
        first_wave.spawn_next() 
        self.add_room_object(Asteroid(self,800,random.randint(200,500),1,3))
        self.add_room_object(Asteroid(self,800,random.randint(200,500),2,5))
        self.add_room_object(Asteroid(self,800,random.randint(200,500),3,100))
        

