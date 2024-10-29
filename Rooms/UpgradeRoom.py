from GameFrame import Level
import pygame
from GameFrame import Globals
from Objects.Button import Button

class UpgradeRoom(Level):
    """
    ok so, we need to add some buttons, some icons, and some text
    like a button to increase speed, some icons showing what level, and text of what oils we have
    """
    def __init__(self, screen, joysticks):
        self.set_background_image('background.png')
        Level.__init__(self, screen, joysticks)
        #speed demon button
        speed_button = Button(self, 100, 100, 'back.png', 64, 64,self.up_speed)
        self.add_room_object(speed_button)
        speed_button.rect.center = (150, 520/4)

        #back button
        back_button = Button(self, 300, 100, 'back.png', 64, 64,self.back)
        self.add_room_object(back_button)
        back_button.rect.center = (900, 520)
    
    def back(self):
        Globals.next_level = Globals.levels.index('Menu')
        self.running = False
    
    def up_speed(self):
        Globals.speed += 1
        