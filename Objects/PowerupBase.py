from GameFrame import RoomObject
from GameFrame import Globals
class PowerupBase():
    def __init__(self,speed_bonus,laser_bonus,armour_bonus,drill_bonus):
        self.speed_bonus = speed_bonus
        self.laser_bonus = laser_bonus
        self.armour_bonus = armour_bonus
        self.drill_bonus = drill_bonus