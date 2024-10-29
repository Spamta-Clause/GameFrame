from GameFrame import RoomObject
class Selector(RoomObject):
    def __init__(self, room, x, y, image):
        RoomObject.__init__(self, room, x, y)
        self.image = self.load_image(image)
        self.set_image(self.image, 30, 20)