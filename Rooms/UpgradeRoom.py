from GameFrame import Level
import pygame
from GameFrame import Globals
from Objects.Button import Button
from Objects.Text import Default
from GameFrame import RoomObject
from Fibbonaci import fibbonaci

class UpgradeRoom(Level):
    """
    ok so, we need to add some buttons, some icons, and some text
    like a button to increase speed, some icons showing what level, and text of what oils we have
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image('background.png')

        #speed demon button
        speed_button = Button(self, 150-32, (520/4)-32, 'speed_up.png', 64, 64,self.up_speed)
        self.add_room_object(speed_button)

        #laser button
        laser_button = Button(self, 150-32, ((520/4)*2)-32, 'laser_up.png', 64, 64,self.up_laser)
        self.add_room_object(laser_button)

        #shield button
        shield_button = Button(self, 150-32, ((520/4)*3)-32, 'shield_up.png', 64, 64, self.up_shield)
        self.add_room_object(shield_button)

        #drill button
        drill_button = Button(self, 150-32, ((520/4)*4)-32, 'drill_up.png', 64, 64, self.up_drill)
        self.add_room_object(drill_button)

        #back button
        back_button = Button(self, 600, 600, 'back.png', 64, 64,self.back)
        self.add_room_object(back_button)
        

        #text
        self.speed_text = Default(self, 550, (520/4), f"Speed: {Globals.speed}")
        self.speed_text.y = (520/4 - self.speed_text.height/2)

        self.laser_text = Default(self, 550, ((520/4)*2), f"Laser: {Globals.laser}")
        self.laser_text.y = ((520/4)*2 - self.speed_text.height/2)

        self.shield_text = Default(self, 550, ((520/4)*3), f"Shield: {Globals.armour}")
        self.shield_text.y = ((520/4)*3 - self.speed_text.height/2)

        self.drill_text = Default(self, 550, ((520/4)*4), f"Drill: {Globals.drill}")
        self.drill_text.y = ((520/4)*4 - self.speed_text.height/2)

        #cost
        self.speed_cost = Default(self, 250, (520/4), "Cost : " + str(fibbonaci(Globals.speed)).replace(".0", ""))
        self.speed_cost.y = (520/4 - self.speed_text.height/2)

        self.emerald_oil_icon = RoomObject(self, 450, (520/4))
        self.emerald_oil_icon.set_image(self.load_image('oils/emerald_oil_1.png'), 32, 32)
        self.emerald_oil_icon.y = (520/4 - self.speed_text.height/2) 

        self.add_room_object(self.emerald_oil_icon)
        self.add_room_object(self.speed_cost)
        self.add_room_object(self.speed_text)

        self.laser_cost = Default(self, 250, ((520/4)*2), "Cost : " + str(fibbonaci(Globals.laser)).replace(".0", ""))
        self.laser_cost.y = ((520/4)*2 - self.speed_text.height/2)

        self.gold_oil_icon = RoomObject(self, 450, ((520/4)*2))
        self.gold_oil_icon.set_image(self.load_image('oils/gold_oil_1.png'), 32, 32)
        self.gold_oil_icon.y = ((520/4)*2 - self.speed_text.height/2)

        self.add_room_object(self.gold_oil_icon)
        self.add_room_object(self.laser_cost)
        self.add_room_object(self.laser_text)

        self.shield_cost = Default(self, 250, ((520/4)*3), "Cost : " + str(fibbonaci(Globals.armour)).replace(".0", ""))
        self.shield_cost.y = ((520/4)*3 - self.speed_text.height/2)

        self.diamond_oil_icon = RoomObject(self, 450, ((520/4)*3))
        self.diamond_oil_icon.set_image(self.load_image('oils/diamond_oil_1.png'), 32, 32)
        self.diamond_oil_icon.y = ((520/4)*3 - self.speed_text.height/2)

        self.add_room_object(self.diamond_oil_icon)
        self.add_room_object(self.shield_cost)
        self.add_room_object(self.shield_text)

        self.drill_cost = Default(self, 250, ((520/4)*4), "Cost : " + str(fibbonaci(Globals.drill)).replace(".0", ""))
        self.drill_cost.y = ((520/4)*4 - self.speed_text.height/2)

        self.ruby_oil_icon = RoomObject(self, 450, ((520/4)*4))
        self.ruby_oil_icon.set_image(self.load_image('oils/ruby_oil_1.png'), 32, 32)
        self.ruby_oil_icon.y = ((520/4)*4 - self.speed_text.height/2)

        self.add_room_object(self.ruby_oil_icon)
        self.add_room_object(self.drill_cost)
        self.add_room_object(self.drill_text)

        #current materials
        self.emerald_oil_text = Default(self, 20, 20, str(Globals.emerald_oil).replace(".0", ""))
        self.current_emerald_oil_icon = RoomObject(self, 20, 50)
        self.current_emerald_oil_icon.set_image(self.load_image('oils/emerald_oil_1.png'), 32, 32)
        self.add_room_object(self.current_emerald_oil_icon)
        self.add_room_object(self.emerald_oil_text)

        self.gold_oil_text = Default(self, 20, 100, str(Globals.gold_oil).replace(".0", ""))
        self.current_gold_oil_icon = RoomObject(self, 20, 130)
        self.current_gold_oil_icon.set_image(self.load_image('oils/gold_oil_1.png'), 32, 32)
        self.add_room_object(self.current_gold_oil_icon)
        self.add_room_object(self.gold_oil_text)

        self.diamond_oil_text = Default(self, 20, 180, str(Globals.diamond_oil).replace(".0", ""))
        self.current_diamond_oil_icon = RoomObject(self, 20, 210)
        self.current_diamond_oil_icon.set_image(self.load_image('oils/diamond_oil_1.png'), 32, 32)
        self.add_room_object(self.current_diamond_oil_icon)
        self.add_room_object(self.diamond_oil_text)

        self.ruby_oil_text = Default(self, 20, 260, str(Globals.ruby_oil).replace(".0", ""))
        self.current_ruby_oil_icon = RoomObject(self, 20, 290)
        self.current_ruby_oil_icon.set_image(self.load_image('oils/ruby_oil_1.png'), 32, 32)
        self.add_room_object(self.current_ruby_oil_icon)
        self.add_room_object(self.ruby_oil_text)

    def update_text(self):
        self.drill_cost.text = "Cost : " + str(fibbonaci(Globals.drill)).replace(".0", "")
        self.shield_cost.text = "Cost : " + str(fibbonaci(Globals.armour)).replace(".0", "")
        self.laser_cost.text = "Cost : " + str(fibbonaci(Globals.laser)).replace(".0", "")
        self.speed_cost.text = "Cost : " + str(fibbonaci(Globals.speed)).replace(".0", "")

        self.speed_text.text = f"Speed: {Globals.speed}"
        self.laser_text.text = f"Laser: {Globals.laser}"
        self.shield_text.text = f"Shield: {Globals.armour}"
        self.drill_text.text = f"Drill: {Globals.drill}"

        self.emerald_oil_text.text = str(Globals.emerald_oil).replace(".0", "")
        self.gold_oil_text.text = str(Globals.gold_oil).replace(".0", "")
        self.diamond_oil_text.text = str(Globals.diamond_oil).replace(".0", "")
        self.ruby_oil_text.text = str(Globals.ruby_oil).replace(".0", "")

        need_updating = [self.drill_cost, self.shield_cost, self.laser_cost, self.speed_cost, self.speed_text, self.laser_text, self.shield_text, self.drill_text, self.emerald_oil_text, self.gold_oil_text, self.diamond_oil_text, self.ruby_oil_text]

        for x in need_updating:
            x.update_text()
        print("updated")




        
    
    def back(self):
        Globals.next_level = Globals.levels.index('Menu')
        self.running = False
    
    def up_speed(self):
        if Globals.emerald_oil >= (fibbonaci(Globals.speed)):
            Globals.emerald_oil -= (fibbonaci(Globals.speed))
            Globals.speed += 1
            self.update_text()

    def up_laser(self):
        if Globals.gold_oil >= (fibbonaci(Globals.laser)):
            Globals.gold_oil -= (fibbonaci(Globals.laser))
            Globals.laser += 1
            self.update_text()

    def up_shield(self):
        if Globals.diamond_oil >= (fibbonaci(Globals.armour)):
            Globals.diamond_oil -= (fibbonaci(Globals.armour))
            Globals.armour += 1
            self.update_text()

    def up_drill(self):
        if Globals.ruby_oil >= fibbonaci(Globals.drill):
            Globals.ruby_oil -= (fibbonaci(Globals.drill))
            Globals.drill += 1
            self.update_text()
        