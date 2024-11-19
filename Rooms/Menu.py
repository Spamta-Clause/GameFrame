from GameFrame import Level, Globals
from Objects.Button import Button
from Rooms.Game import Game
from Rooms.TutorialRoom import TutorialRoom
from Objects.Text import Default
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

        play_button = Button(self, 100, 100, 'play_button.png', 256, 128, self.game_room)
        self.add_room_object(play_button)
        level_text = Default(self, play_button.x + play_button.width/2, play_button.y + play_button.height/2, f"Level {Globals.level}")
        level_text.depth = 3
        level_text.x = play_button.x + play_button.width/2 - level_text.width/2
        level_text.y = play_button.y + play_button.height/2 - level_text.height/2 + 52
        self.add_room_object(level_text)
    

        self.add_room_object(Button(self, 100, 300, 'gamble_button.png', 138*2, 48*2,self.gamble_room))
        self.set_background_image('background.png')
        self.add_room_object(Button(self, 100, 500, 'upgrade_button.png', 138*2, 48*2, self.upgrade_room))

        self.easy_button = Button(self, 400, 100, 'easy_button_not_selected.png', 97*2, 48*2, self.set_easy)
        self.medium_button = Button(self, 400, 200, 'medium_button_not_selected.png', 138*2, 48*2, self.set_medium)
        self.hard_button = Button(self, 400, 300, 'hard_button_not_selected.png', 97*2, 48*2, self.set_hard)

        self.set_easy()

        self.easy_button.x = Globals.SCREEN_WIDTH/3 * 2 - self.easy_button.width/2
        self.medium_button.x = Globals.SCREEN_WIDTH/3 * 2 - self.medium_button.width/2
        self.hard_button.x = Globals.SCREEN_WIDTH/3 * 2 - self.hard_button.width/2

        self.easy_button.y = Globals.SCREEN_HEIGHT/4 - self.easy_button.height/2
        self.medium_button.y = Globals.SCREEN_HEIGHT/2 - self.medium_button.height/2
        self.hard_button.y = Globals.SCREEN_HEIGHT/4 * 3 - self.hard_button.height/2
        
        self.add_room_object(self.easy_button)
        self.add_room_object(self.medium_button)
        self.add_room_object(self.hard_button)
    
    def upgrade_room(self):
        Globals.next_level = Globals.levels.index('UpgradeRoom')
        self.running = False

    def set_easy(self):
        Globals.difficulty = 1
        self.easy_button.set_image(self.easy_button.load_image('easy_button.png'), 97*2, 48*2)
        self.medium_button.set_image(self.medium_button.load_image('medium_button_not_selected.png'), 138*2, 48*2)
        self.hard_button.set_image(self.hard_button.load_image('hard_button_not_selected.png'), 97*2, 48*2)

    def set_medium(self):
        Globals.difficulty = 2
        self.easy_button.set_image(self.easy_button.load_image('easy_button_not_selected.png'), 97*2, 48*2)
        self.medium_button.set_image(self.medium_button.load_image('medium_button.png'), 138*2, 48*2)
        self.hard_button.set_image(self.hard_button.load_image('hard_button_not_selected.png'), 97*2, 48*2)

    def set_hard(self):
        Globals.difficulty = 3
        self.easy_button.set_image(self.easy_button.load_image('easy_button_not_selected.png'), 97*2, 48*2)
        self.medium_button.set_image(self.medium_button.load_image('medium_button_not_selected.png'), 138*2, 48*2)
        self.hard_button.set_image(self.hard_button.load_image('hard_button.png'), 97*2, 48*2)

