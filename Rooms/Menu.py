from GameFrame import Level, Globals
from Objects.Button import Button
from Rooms.Game import Game
from Rooms.TutorialRoom import TutorialRoom
import pygame

class Menu(Level):
    def start_room(self):
        #ok so, we find the index of the start room, we set that as the next room, then boom, we're done
        Globals.next_level = Globals.levels.index('TutorialRoom')
        self.running = False
    
    def game_room(self):
        Globals.next_level = Globals.levels.index('Game')
        self.running = False
        

    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.add_room_object(Button(self, 100, 100, 'play_button.png', 256, 128,self.game_room))
        self.set_background_image('background.png')

