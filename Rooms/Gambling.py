from Objects.Button import Button
from Objects.Text import Title
from GameFrame import Level, Globals, RoomObject
from Objects.Roulette_Manager import Roulette_Manager
from Objects.Selector import Selector
from Objects.Button import Button
import random

class Gambling(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        self.title = Title(self, 
                           Globals.SCREEN_WIDTH/2, 20, 
                           "GAMBLING")
        self.title.x = Globals.SCREEN_WIDTH/2 - self.title.width/2
        self.add_room_object(self.title)
        
        self.button = Button(self, 50, 90, "gambling.png", 96, 96, self.gamble)
        self.add_room_object(self.button)
        
        self.set_background_image('background.png')
        self.roulette_manager = Roulette_Manager(self, 30, 50)
        self.add_room_object(self.roulette_manager)
        
        self.arrow = Selector(self, Globals.SCREEN_WIDTH/2-225, 360, "selector.png")
        self.arrow.rect.center = (Globals.SCREEN_WIDTH/2-225, 360)
        self.add_room_object(self.arrow)

        self.other_arrow = Selector(self, Globals.SCREEN_WIDTH/2+200, 360, "other_selector.png")
        self.other_arrow.rect.center = (Globals.SCREEN_WIDTH/2+200, 360)
        self.add_room_object(self.other_arrow)

        self.back_button = Button(self, 1164, 602, "back.png", 96, 96, self.back)
        self.add_room_object(self.back_button)

    def gamble(self):
        if self.roulette_manager.is_gambling == False:
            print("Gamble")
            self.roulette_manager.set_speed(random.randint(4,10))

    def back(self):
        Globals.next_level = Globals.levels.index('Menu')
        self.running = False
