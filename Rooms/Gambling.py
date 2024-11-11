from Objects.Button import Button
from Objects.Text import Title
from GameFrame import Level, Globals, RoomObject
from Objects.Roulette_Manager import Roulette_Manager
from Objects.Selector import Selector
from Objects.Button import Button
from Objects.Text import Default
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

        self.ruby_oil_cost_text = Default(self, 30, 200, f"2")
        self.emerald_oil_cost_text = Default(self, 30, 250, f"2")
        self.diamond_oil_cost_text = Default(self, 30, 300, f"2")
        self.gold_oil_cost_text = Default(self, 30, 350, f"2")
        self.add_room_object(self.ruby_oil_cost_text)
        self.add_room_object(self.emerald_oil_cost_text)
        self.add_room_object(self.diamond_oil_cost_text)
        self.add_room_object(self.gold_oil_cost_text)

        self.ruby_oil_cost_icon = RoomObject(self, 60, 200)
        self.ruby_oil_cost_icon.set_image(self.load_image('oils/ruby_oil_1.png'), 32, 32)
        self.add_room_object(self.ruby_oil_cost_icon)
        self.emerald_oil_cost_icon = RoomObject(self, 60, 250)
        self.emerald_oil_cost_icon.set_image(self.load_image('oils/emerald_oil_1.png'), 32, 32)
        self.add_room_object(self.emerald_oil_cost_icon)
        self.diamond_oil_cost_icon = RoomObject(self, 60, 300)
        self.diamond_oil_cost_icon.set_image(self.load_image('oils/diamond_oil_1.png'), 32, 32)
        self.add_room_object(self.diamond_oil_cost_icon)
        self.gold_oil_cost_icon = RoomObject(self, 60, 350)
        self.gold_oil_cost_icon.set_image(self.load_image('oils/gold_oil_1.png'), 32, 32)
        self.add_room_object(self.gold_oil_cost_icon)

        #current materials
        self.ruby_oil_text = Default(self, 1200, 50, str(Globals.ruby_oil).replace(".0", ""))
        self.ruby_oil_cost_icon = RoomObject(self, 1200, 80)
        self.ruby_oil_cost_icon.set_image(self.load_image('oils/ruby_oil_1.png'), 32, 32)
        self.add_room_object(self.ruby_oil_cost_icon)
        self.add_room_object(self.ruby_oil_text)

        self.emerald_oil_text = Default(self, 1200, 100, str(Globals.emerald_oil).replace(".0", ""))
        self.emerald_oil_cost_icon = RoomObject(self, 1200, 130)
        self.emerald_oil_cost_icon.set_image(self.load_image('oils/emerald_oil_1.png'), 32, 32)
        self.add_room_object(self.emerald_oil_cost_icon)
        self.add_room_object(self.emerald_oil_text)

        self.diamond_oil_text = Default(self, 1200, 150, str(Globals.diamond_oil).replace(".0", ""))
        self.diamond_oil_cost_icon = RoomObject(self, 1200, 180)
        self.diamond_oil_cost_icon.set_image(self.load_image('oils/diamond_oil_1.png'), 32, 32)
        self.add_room_object(self.diamond_oil_cost_icon)
        self.add_room_object(self.diamond_oil_text)

        self.gold_oil_text = Default(self, 1200, 210, str(Globals.gold_oil).replace(".0", ""))
        self.gold_oil_cost_icon = RoomObject(self, 1200, 240)
        self.gold_oil_cost_icon.set_image(self.load_image('oils/gold_oil_1.png'), 32, 32)
        self.add_room_object(self.gold_oil_cost_icon)
        self.add_room_object(self.gold_oil_text)
        
        
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

    def update_text(self):
        self.ruby_oil_text.text = str(Globals.ruby_oil).replace(".0", "")
        self.emerald_oil_text.text = str(Globals.emerald_oil).replace(".0", "")
        self.diamond_oil_text.text = str(Globals.diamond_oil).replace(".0", "")
        self.gold_oil_text.text = str(Globals.gold_oil).replace(".0", "")

        self.ruby_oil_text.update_text()
        self.emerald_oil_text.update_text()
        self.diamond_oil_text.update_text()
        self.gold_oil_text.update_text()


    def gamble(self):
        #make sure the player has enough oil -- 2 of each
        if Globals.emerald_oil >= 2 and Globals.ruby_oil >= 2 and Globals.diamond_oil >= 2 and Globals.gold_oil >= 2 and self.roulette_manager.is_gambling == False:
            Globals.emerald_oil -= 2
            Globals.ruby_oil -= 2
            Globals.diamond_oil -= 2
            Globals.gold_oil -= 2
            self.roulette_manager.is_gambling = True
            self.roulette_manager.set_speed(random.randint(4,10))
            self.update_text()
            

    def back(self):
        Globals.next_level = Globals.levels.index('Menu')
        self.running = False
