from GameFrame import RoomObject, Globals
import random
from Objects.Fading_Text import Fading_Text

class Asteroid(RoomObject):
    """
    A class for Zorks danerous obstacles
    """
    
    def __init__(self, room, x, y,speed,):
        """
        Initialise the Asteroid object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self,room, x, y)
        
        # set travel direction
        angle = random.randint(135,225)
        self.set_direction(angle, speed)
        self.can_take_damage = True

        self.register_collision_object("Ship")

        self.size = random.randint(1,3)

        self.type_num = random.randint(1,10)
        if self.type_num == 10:
            self.type = "Diamond"
            self.health = 16
        elif self.type_num >= 7:
            self.type = "Gold"
            self.health = 8
        elif self.type_num >= 4:
            self.type = "Emerald"
            self.health = 4
        else:
            self.type = "Ruby"
            self.health = 2
        self.max_health = self.health
        image = self.load_image(f"{self.type.lower()}_Asteroid.png")
        self.set_image(image,20*self.size,20*self.size)
            
        
    def step(self):
        """
        Determines what happens to the asteroid on each tick of the game clock
        """
        self.keep_in_room()
        self.outside_of_room()
        
    def handle_collision(self, other, other_type):
        if other_type == "Ship" and other.is_drilling and self.can_take_damage:
            print("getting drilled")
            self.damage(other.drill_damage)


    def keep_in_room(self):
        """
        Keeps the asteroid inside the top and bottom room limits
        """
        if self.y < 0:
            self.y = 0
            self.y_speed *= -1
        elif self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y = Globals.SCREEN_HEIGHT - self.height
            self.y_speed *= -1
    
    def damage(self,damage):
        self.health -= damage
        self.can_take_damage = False
        self.set_timer(5, self.reset_damage)
        if self.health <= 0:
            match self.type:
                case "Diamond":
                    Globals.diamond_oil += 1
                case "Gold":
                    Globals.gold_oil += 1
                case "Emerald":
                    Globals.emerald_oil += 1
                case "Ruby":
                    Globals.ruby_oil += 1
                #now we want to show a little text box that will fade saying how much oil was collected
            plus_oil_text = Fading_Text(self.room, self.x, self.y, f"+1 {self.type} Oil", 30, (255,255,255,255))
            plus_oil_text.x = self.x - plus_oil_text.width/2
            plus_oil_text.y = self.y - plus_oil_text.height/2
            self.room.add_room_object(plus_oil_text)

            self.size -= 1
            if self.size == 0:
                self.room.delete_object(self)
            else:
                self.health = self.max_health
                image = self.load_image(f"{self.type.lower()}_Asteroid.png")
                self.set_image(image,20*self.size,20*self.size)


    def reset_damage(self):
        self.can_take_damage = True


    def outside_of_room(self):
        """
        removes asteroid that have exited the room
        """
        if self.x + self.width < 0:
            self.room.delete_object(self)