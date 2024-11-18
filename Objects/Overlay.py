from GameFrame import RoomObject, Globals
import pygame

class Overlay(RoomObject):
    def __init__(self, room, image, length):
        RoomObject.__init__(self, room, 0, 0)
        self.image = self.load_image(image)
        self.set_image(self.image, Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT)
        self.length = length
        self.room = room
        self.room.add_room_object(self)
        print("created")
        self.alpha = 100
        self.fade_speed = (self.alpha / self.length)

    def step(self):
        print(self.alpha)
        if self.alpha > 0:
            self.alpha -= self.fade_speed
            self.image.set_alpha(self.alpha)
        else:
            self.destroy_overlay()

    def destroy_overlay(self):
        self.room.delete_object(self)
        print("destroyed")
