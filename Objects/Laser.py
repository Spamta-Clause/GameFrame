from GameFrame import RoomObject
from GameFrame import Globals

class Laser(RoomObject):
    def __init__(self, room, x, y, image, width, height, speed, angle, damage, shooter):
        RoomObject.__init__(self, room, x, y)
        
        self.image = self.load_image(image)
        self.set_image(self.image, width, height)
        self.speed = speed
        self.angle = angle
        self.damage = damage
        self.shooter = shooter
    
    def step(self):
        self.set_direction(self.angle, self.speed)
        self.keep_in_room()

    def keep_in_room(self):
        if self.y < 0:
            self.room.delete_object(self)
        elif self.y + self.height> Globals.SCREEN_HEIGHT:
            self.room.delete_object(self)

        if self.x < 0:
            self.room.delete_object(self)
        elif self.x + self.width> Globals.SCREEN_WIDTH:
            self.room.delete_object(self)