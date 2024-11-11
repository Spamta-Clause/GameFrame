from GameFrame import RoomObject
import pygame
from GameFrame import Globals
from Objects.Laser import Laser

class Ship(RoomObject):
    def __init__(self, room, x, y, width, height, i_ticks, shoot_cooldown = 15):
        RoomObject.__init__(self, room, x, y)

        self.damage_multiplier = 1
        self.shield = 0

        self.can_take_damage = True

        match Globals.current_powerup:
            case "shield-1":
                self.shield = 1
            case "shield-2":
                self.shield = 2
            case "shield-3":
                self.shield = 3
            case "damage-1":
                self.damage_multiplier = 1.5
            case "damage-2":
                self.damage_multiplier = 2
            case "damage-3":
                self.damage_multiplier = 3
            case "immunity-1":
                self.immunity(10 * 30)
            case "immunity-2":
                self.immunity(20 * 30) 
            case "immunity-3":
                self.immunity(30 * 30)
        
        match self.shield:
            case 0:
                self.room.hearts_arrays.pop()
                

        self.image = self.load_image("ship.png")
        match self.shield:
            case 0:
                match self.damage_multiplier:
                    case 1:
                        self.image = self.load_image("ship.png")
                    case 1.5:
                        self.image = self.load_image("supercharged\\damage_1.png")
                    case 2:
                        self.image = self.load_image("supercharged\\damage_2.png")
                    case 3:
                        self.image = self.load_image("supercharged\\damage_3.png")
            case self.shield if self.shield > 0:
                self.image = self.load_image(f"supercharged\\shield_{self.shield}.png")
        if self.shield != 0 and self.damage_multiplier != 1:
            self.set_image(self.image, width + (1 * (width/29)), height (1 * (height/31)))   
        else:
            self.set_image(self.image, width, height)
        
        self.accelleration = 0.1
        self.decelleration = 0.1
        self.speed = 0

        Globals.LIVES = Globals.armour
        self.max_speed = Globals.speed
        self.drill_damage = Globals.drill
        self.damage = Globals.laser

        self.can_shoot = True
        self.shoot_cooldown = shoot_cooldown
        
        self.i_ticks = i_ticks
        

        self.handle_key_events = True
        self.register_collision_object("Laser")

        self.is_drilling = False

    def reset_can_take_damage(self):
        self.can_take_damage = True
        self.room.update_hearts("heart")
    
    def immunity(self, ticks):
        self.can_take_damage = False
        for heart in self.room.hearts:
            heart.set_value("immunity")
        self.set_timer(ticks, self.end_immunity)

    def end_immunity(self):
        self.can_take_damage = True
        for heart in self.room.hearts:
            heart.set_value("heart")

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
            laser = Laser(self, self.x + self.width/2, self.y + self.height/2, "laser.png", 8, 8, 10+self.speed, (360-self.curr_rotation)%360, self.damage, self)
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
        print("damaged")
        if self.can_take_damage:
            rotation = self.curr_rotation
            self.can_take_damage = False
            self.set_timer(self.i_ticks, self.reset_can_take_damage)
            self.shield -= damage       
                
            self.room.remove_heart(damage)

            print(self.shield)
            

            if self.shield >= 0:
                match self.shield:
                    case 1:
                        self.image = self.load_image("supercharged\\shield_1.png")
                        self.set_timer(self.i_ticks, self.reset_can_take_damage)
                        self.set_image(self.image, self.width, self.height)
                    case 2:
                        self.image = self.load_image("supercharged\\shield_2.png")
                        self.set_timer(self.i_ticks, self.reset_can_take_damage)
                        self.set_image(self.image, self.width, self.height)
            if "shield" in str(Globals.current_powerup):
                if self.shield <= 0:
                    self.shield = 0
                    self.image = self.load_image("ship.png")
                    self.set_image(self.image, self.width, self.height)
            if self.shield <= 0:
                Globals.LIVES -= damage
            
            self.image = pygame.transform.rotate(self.image_orig, self.curr_rotation)
            if Globals.LIVES <= 0:
                self.room.delete_object(self)
                Globals.next_level = Globals.levels.index("Menu")
                self.room.running = False