from GameFrame import RoomObject
class Heart(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.image = self.load_image("heart.png")
        self.set_image(self.image, 16, 16)
        self.value = "heart"
    def set_value(self, value):
        self.value = value
        self.image = self.load_image(f"{value}.png")
        self.set_image(self.image, 16, 16)