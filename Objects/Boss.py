from GameFrame import Globals, RoomObject

class Boss(RoomObject):
    def __init__(self, room, x, y, width, height, health, damage_one, damage_two, image):
        RoomObject.__init__(self, room, x, y)
        self.image = self.load_image(image)
        self.set_image(self.image, width, height)
        self.health = health * Globals.difficulty
        self.damage_one = damage_one
        self.damage_two = damage_two

    def attack(self):
        pass

    def tick(self):
        pass

