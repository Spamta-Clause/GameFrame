from Objects.Enemy_Base import Enemy_Base
from GameFrame import Globals
from Objects.Laser import Laser
from Objects.Smash import Smash
from Objects.Unstable import Unstable
import random, copy

class Ship_Cruiser(Enemy_Base):
    def __init__(self, room, x, y, image, width, height, speed, target, health, too_close_for_comfort, spawn_rate, wave):
        Enemy_Base.__init__(self, room, x, y, image, width, height, speed, target, health, too_close_for_comfort, wave)
        
        self.spawn_rate = spawn_rate
        self.fire_timer = 0

        smash_ship = Smash(self, self.rect.centerx, self.rect.centery, 'spinny.png', 32, 18, 3, self.target, 1, 1, 20, None)
        unstable_ship = Unstable(self, self.rect.centerx, self.rect.centery, 'boom.png', 32, 18, 3, self.target, 150, 90,1,None)
    
    def step(self):
        self.move_to_target()

        target_x, target_y = self.target.rect.center
        if target_x < self.rect.centerx:
            angle = self.rotate_to_coordinate(target_x, target_y)
        else:
            angle = self.rotate_to_coordinate(target_x, target_y)
            self.rotate(2 * angle)
        self.rotate(90)

        
        
        self.fire_timer += 1
        if self.fire_timer >= self.spawn_rate:
            self.fire_timer = 0
            self.fire()
        #could just do it with timer but that'd require another function and i am lazy also just copied this code from the laser cruiser because they're basically the same thing just one shoots ships the other shoot slasers
    
    def fire(self):
        new_ship = Smash(self, self.x + self.width/2, self.y + self.height/2, 'spinny.png', 32, 18, 3, self.target, 1, 1, 20,None)
        self.room.add_room_object(new_ship)
        new_ship.curr_rotation = self.curr_rotation