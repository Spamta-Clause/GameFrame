from GameFrame import Level, Globals
from Objects.Button import Button
from Rooms.Game import Game
from Rooms.TutorialRoom import TutorialRoom
import pygame

class Menu(Level):
    def gamble_room(self):
        Globals.next_level = Globals.levels.index('Gambling')
        self.running = False

    
    def game_room(self):
        Globals.next_level = Globals.levels.index('Game')
        self.running = False
        

    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.add_room_object(Button(self, 100, 100, 'play_button.png', 256, 128,self.game_room))
        self.add_room_object(Button(self, 100, 300, 'gamble_button.png', 138*2, 48*2,self.gamble_room))
        self.set_background_image('background.png')
        self.add_room_object(Button(self, 100, 500, 'upgrade_button.png', 138*2, 48*2, self.upgrade_room))
    
    def upgrade_room(self):
        Globals.next_level = Globals.levels.index('UpgradeRoom')
        self.running = False

