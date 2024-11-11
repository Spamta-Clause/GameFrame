from Objects.Boss import Boss
from GameFrame import Globals, RoomObject
import pygame, math, random

class Cuthulu(Boss):
    def __init__(self, room, x, y, width, height, health, damage_one, damage_two, image, wave):
        Boss.__init__(self, room, x, y, width, height, health, damage_one, damage_two, image, wave)

        
        self.weakspot = Weakspot(self.room, self.x, self.y, 100, 100, "bosses/weakspot.png")
        self.weakspot.boss = self

        self.room.add_room_object(self.weakspot)

        self.tentacle = Tentacle(self.room, self.x, self.y, 476*4, 32*4, "bosses/tentacle.png")

        self.room.add_room_object(self.tentacle)

        self.can_take_damage = True
        self.set_timer(30, self.attack)

    def attack(self):
        # if random.randint(0, 3) == 1 and not self.tentacle.going_to_player:
        #     self.tentacle.going_to_player = True
        # self.set_timer(30, self.attack)
        pass

    def step(self):
        self.attack()

    def can_take_damage_timer(self):
        self.can_take_damage = True

    def take_damage(self, damage):
        if self.can_take_damage:
            print("took damage")
            self.health -= damage
            if self.health <= 0:
                self.wave.enemy_dead(self)
                self.room.remove_object(self)
                self.room.remove_object(self.weakspot)
            self.can_take_damage = False
            self.set_timer(30, self.can_take_damage_timer)

class Tentacle(RoomObject):
    def __init__(self, room, x, y, width, height, image):
        RoomObject.__init__(self, room, x, y)
        self.image_name = image
        self.image = self.load_image(image)
        self.set_image(self.image, width, height)
        self.speed = 4.5
        self.spam_keys = []
        self.handle_key_events = True
        self.last_pressed = None
        self.attacking = True
        self.going_to_player = True


    def step(self):
        self.attack()

    def key_pressed(self, key):
        if (key[pygame.K_w] or key[pygame.K_a] or key[pygame.K_s] or key[pygame.K_d] or key[pygame.K_SPACE]) and key != self.last_pressed:
            self.last_pressed = key
            self.spam_keys.append(key)

    #function for tip to gradually move to player
    def move_to_player(self):
        print("moving to player")
        ship = self.room.ship
        direction_x = ship.x - self.x
        direction_y = ship.y - self.y
        angle = math.atan2(direction_y, direction_x)
        self.x += self.speed * math.cos(angle)
        self.y += self.speed * math.sin(angle)
    
    def attack(self):
        if not self.going_to_player:
            self.pull()
        if self.going_to_player:
            self.move_to_player()
            distance = math.sqrt((self.room.ship.x - self.x)**2 + (self.room.ship.y - self.y)**2)
            if distance < 5:
                self.spam_keys = []
                self.going_to_player = False

    def pull(self):
        if len(self.spam_keys) > 30:
            if self.x < Globals.SCREEN_WIDTH - 100:
                self.set_direction(0, self.speed * 5)
            else:
                print("reached end")
                self.set_direction(0, 0)
                self.going_to_player = True
        else:
            self.set_direction(0, self.speed)
            self.room.ship.set_direction(0, self.speed)
            self.y = self.room.ship.y + self.room.ship.height/2 - self.height/3
            self.x = self.room.ship.x + self.room.ship.width/2
    

    def update_image(self):
        self.set_image(self.load_image(self.image_name), self.width, self.height)

class Weakspot(RoomObject):
    def __init__(self, room, x, y, width, height, image):
        RoomObject.__init__(self, room, x, y)
        self.image_name = image
        self.image = self.load_image(image)
        self.set_image(self.image, width, height)

        self.register_collision_object("Laser")
    
    def handle_collision(self, other, other_type):
        if other_type == "Laser":
            print("hit")
            self.boss.take_damage(other.damage)
