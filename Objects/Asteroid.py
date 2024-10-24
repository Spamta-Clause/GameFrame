from GameFrame import RoomObject, Globals
import random

class Asteroid(RoomObject):
    """
    A class for Zorks danerous obstacles
    """
    
    def __init__(self, room, x, y,speed, health):
        """
        Initialise the Asteroid object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self,room, x, y)
        
        # set image
        image = self.load_image("play_button.png")
        self.set_image(image,20,20)
        
        # set travel direction
        angle = random.randint(135,225)
        self.set_direction(angle, speed)

        self.health = health
        self.can_take_damage = True

        self.register_collision_object("Ship")
        
    def step(self):
        """
        Determines what happens to the asteroid on each tick of the game clock
        """
        self.keep_in_room()
        self.outside_of_room()
        
    def handle_collision(self, other, other_type):
        if other_type == "Ship" and other.is_drilling and self.can_take_damage:
            print("getting drilled")
            self.damage(1)


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
        self.health -= 1
        self.can_take_damage = False
        self.set_timer(5, self.reset_damage)
        if self.health <= 0:
            self.room.delete_object(self)

    def reset_damage(self):
        self.can_take_damage = True


    def outside_of_room(self):
        """
        removes asteroid that have exited the room
        """
        if self.x + self.width < 0:
            print("asteroid left")
            self.room.delete_object(self)