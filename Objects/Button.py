from GameFrame import RoomObject
import pygame


class Button(RoomObject):
    def __init__(self, room, x, y, image, width, height, function):
        RoomObject.__init__(self, room, x, y)
        self.pressed = False
        image = self.load_image(image)
        self.set_image(image, width, height+9)
        
        self.function = function
        #Turns out handle mouse events only works when clicking on the image, no need for hard to code crap!!!

        self.handle_mouse_events = True
    
    def clicked(self, button_number):
        if button_number == 1:
            self.function()
