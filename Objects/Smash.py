from GameFrame import Globals
from Objects.Enemy_Base import Enemy_Base

class Smash(Enemy_Base):
    def __init__(self, room, x, y, image, width, height, speed, target, health, damage, spin_speed, wave):
        Enemy_Base.__init__(self, room, x, y, image, width, height, speed, target, health, False, wave)
        
        self.spin_speed = spin_speed
        self.damage = damage

    def step(self):
        #painful trigonometry but in a function so i dont have to look at it and reminisce about the pain it caused me
        self.move_to_target()
        self.rotate(self.spin_speed)
        

    def handle_collision(self, other, other_type):
        if self.wave != None:
            self.wave.enemy_dead(self)
        self.room.delete_object(self)
        if other_type == "Ship":
            other.take_damage(self.damage)
