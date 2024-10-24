from GameFrame import RoomObject
import pygame
from GameFrame import Globals
from Objects.Laser import Laser

class Ship(RoomObject):
    def __init__(self, room, x, y, image, width, height, max_speed, health, i_ticks, shoot_cooldown = 15):
        RoomObject.__init__(self, room, x, y)
        self.image = self.load_image(image)
        self.set_image(self.image, width, height)
        self.max_speed = max_speed
        self.accelleration = 0.1
        self.decelleration = 0.1
        self.speed = 0

        self.can_shoot = True
        self.shoot_cooldown = shoot_cooldown
        
        self.i_ticks = i_ticks
        self.can_take_damage = True

        Globals.LIVES = health

        self.handle_key_events = True
        self.register_collision_object("Laser")

        self.is_drilling = False

    def reset_can_take_damage(self):
        self.can_take_damage = True

    def step(self):
        #Called every frame which is set in globals
        self.keep_in_room()

        if Globals.LIVES <= 0:
            self.room.delete_object(self)
            Globals.next_level = Globals.levels.index("Menu")

    def keep_in_room(self):
        #I wonder where I got this code from
        if self.y < 0:
            self.y = 0
            print("outside")
        elif self.y + self.height> Globals.SCREEN_HEIGHT:
            self.y = Globals.SCREEN_HEIGHT - self.height
            print("outside")

        if self.x < 0:
            self.x = 0
            print("outside")
        elif self.x + self.width> Globals.SCREEN_WIDTH:
            self.x = Globals.SCREEN_WIDTH - self.width
            print("outside")

    def key_pressed(self, key):
        #MOVING FORWARD AND BACKWARD
        if key[pygame.K_w]:
            self.speed += self.accelleration
            self.speed = min(self.speed, self.max_speed)
            self.set_direction((360-self.curr_rotation), self.speed)
            
        elif key[pygame.K_s]:
            self.speed -= self.accelleration
            self.speed = max(self.speed, -self.max_speed)
            self.set_direction((360-self.curr_rotation), self.speed)

        else:
            if self.speed > 0:
                self.speed -= self.decelleration
                self.speed = max(self.speed, 0)
                self.set_direction((360-self.curr_rotation), self.speed)
            elif self.speed < 0:
                self.speed += self.decelleration
                self.speed = min(self.speed, 0)
                self.set_direction((360-self.curr_rotation), self.speed)

        #TURNING
        if key[pygame.K_a]:
            self.rotate(12)
        if key[pygame.K_d]:
            self.rotate(-12)

        #LASER
        pygame.event.get()
        #should check for left click
        # Adjust the laser creation coordinates to the center of the ship
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            self.can_shoot = False
            laser = Laser(self, self.x + self.width/2, self.y + self.height/2, "laser.png", 8, 8, 10, (360-self.curr_rotation)%360, 1, self)
            self.room.add_room_object(laser)
            self.set_timer(self.shoot_cooldown, self.shot_reset)
        
        if pygame.mouse.get_pressed()[2]:
            self.is_drilling = True
        if not pygame.mouse.get_pressed()[2]:
            self.is_drilling = False
    
    def shot_reset(self):
        self.can_shoot = True

    def handle_collision(self, other, other_type):
        if other_type == "Laser":
            if other.shooter != self:
                self.take_damage(other.damage)
                self.room.delete_object(other)

    def take_damage(self, damage):
        if self.can_take_damage:
            Globals.LIVES -= damage
            print('took damage')
            if Globals.LIVES <= 0:
                self.room.delete_object(self)
                Globals.next_level = Globals.levels.index("Menu")
                self.room.running = False
            self.can_take_damage = False
            self.set_timer(self.i_ticks, self.reset_can_take_damage)