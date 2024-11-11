from GameFrame import Globals, RoomObject

class Boss(RoomObject):
    def __init__(self, room, x, y, width, height, health, damage_one, damage_two, image, wave):
        RoomObject.__init__(self, room, x, y)
        self.image = self.load_image(image)
        self.set_image(self.image, width, height)
        self.health = health
        self.damage_one = damage_one
        self.damage_two = damage_two
        self.wave = wave

    def attack(self):
        pass

    def tick(self):
        pass

