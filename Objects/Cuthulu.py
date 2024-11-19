from Objects.Boss import Boss
from GameFrame import Globals, RoomObject
from Objects.Fading_Text import Fading_Text
import pygame, math, random

class Fake_Eye(RoomObject):
    def __init__(self, room, x, y, width, height, image):
        RoomObject.__init__(self, room, 0, 0)
        self.center_x, self.center_y = x, y
        self.image_name = image
        self.image = self.load_image(image)
        self.radius = 200
        self.set_image(self.image, width, height)
        self.register_collision_object("Laser")

    def handle_collision(self, other, other_type):
        if other_type == "Laser":
            pygame.mixer.Sound.play(pygame.mixer.Sound("Sounds\\cuthulu_hit.mp3"))
            for x in range(Globals.difficulty):
                self.set_timer(30 * x, self.spawn_teeth)
                self.room.delete_object(other)

    def spawn_teeth(self):
        pygame.mixer.Sound.play(pygame.mixer.Sound("Sounds\\cuthulu_shoot.mp3"))
        self.room.add_room_object(Teeth(self.room, self.x, self.y, 30, 38, "bosses/tooth.png", 5, 1))

    
    def step(self):
        self.current_heading += random.uniform(0.01, 0.05)
        self.x = self.radius * math.cos(self.current_heading) - self.width/2 + self.center_x
        self.y = self.radius * math.sin(self.current_heading) - self.height/2 + self.center_y

class Bossbar(RoomObject):
    def __init__(self, room, x, y, width, height, boss, pos):
        if pos == 1:
            RoomObject.__init__(self, room, Globals.SCREEN_WIDTH/3 - width/2, Globals.SCREEN_HEIGHT - 20)
        elif pos == 2:
            RoomObject.__init__(self, room, Globals.SCREEN_WIDTH/2 - width/2, Globals.SCREEN_HEIGHT - 20)
        elif pos == 3:
            RoomObject.__init__(self, room, Globals.SCREEN_WIDTH/3 * 2 - width/2, Globals.SCREEN_HEIGHT - 20)
        self.boss = boss
        self.width = width
        self.max_width = width
        self.height = height
        self.health = boss.health
        self.max_health = boss.health
        self.image = self.load_image("bosses\\cuthulu_health_bar.png")
        self.set_image(self.image, width, height)
        self.set_timer(15, self.update_width)
        self.depth = 1

        self.room.add_room_object(Bossbar_background(self.room, self.x - 4 , self.y - 4, width / 56 * 58, height / 4 * 6))
    
    def update_width(self):
        self.health = self.boss.health
        self.width = self.max_width * (self.health/self.max_health)
        if self.width < 0:
            self.width = 0
        self.set_image(self.load_image("bosses\\cuthulu_health_bar.png"), self.width, self.height)
        self.set_timer(15, self.update_width)

class Bossbar_background(RoomObject):
    def __init__(self, room, x, y, width, height):
        RoomObject.__init__(self, room, x, y)
        self.width = width
        self.height = height
        self.image = self.load_image("bosses\\bossbar_back.png")
        self.set_image(self.image, width, height)

class Eye(RoomObject):
    def __init__(self, room, x, y, width, height, image, health, amalgamation = False):
        RoomObject.__init__(self, room, 0, 0)
        self.image_name = image
        self.image = self.load_image(image)
        self.set_image(self.image, width, height)
        self.radius = 200
        self.current_heading = 0
        self.center_x, self.center_y = x, y

        self.health = health * Globals.difficulty
        self.max_health = health * Globals.difficulty
        bossbar = Bossbar(self.room, 0, 0, 56*4, 16, self, 1)
        self.room.add_room_object(bossbar)

        self.register_collision_object("Laser")

        self.set_timer(120, self.spawn_teeth)

        self.amalgamation = amalgamation
        self.fake_eyes = []
    
    def step(self):
        self.current_heading += random.uniform(0.01, 0.075)
        self.x = self.radius * math.cos(self.current_heading) - self.width/2 + self.center_x
        self.y = self.radius * math.sin(self.current_heading) - self.height/2 + self.center_y
    
    def spawn_teeth(self):
        for x in range(Globals.difficulty):
            self.set_timer(30 * x, self.spawn_tooth)
        self.set_timer(120, self.spawn_teeth)
        #bruh this naming is wack

    def spawn_tooth(self):
        pygame.mixer.Sound.play(pygame.mixer.Sound("Sounds\\cuthulu_shoot.mp3"))
        self.room.add_room_object(Teeth(self.room, self.x, self.y, 30, 38, "bosses/tooth.png", 5, 1))
    
    def handle_collision(self, other, other_type):
        if other_type == "Laser":
            pygame.mixer.Sound.play(pygame.mixer.Sound("Sounds\\cuthulu_hit.mp3"))
            self.health -= other.damage
            self.room.delete_object(other)
            if self.health <= 0:
                for eye in self.fake_eyes:
                    self.room.delete_object(eye)
                self.room.delete_object(self)
                if self.amalgamation:
                    self.room.amalgamation_amount -= 1
                    if self.room.amalgamation_amount == 0:
                        Globals.next_level = Globals.levels.index('VictoryRoom')
                        self.room.running = False
                else:
                    Globals.next_level = Globals.levels.index('VictoryRoom')
                    self.room.running = False

class Teeth(RoomObject):
    def __init__(self, room, x, y, width, height, image, speed, damage):
        RoomObject.__init__(self, room, x, y)
        self.image_name = image
        self.image = self.load_image(image)
        self.set_image(self.image, width, height)
        self.speed = speed
        self.damage = damage
        self.target = self.room.ship

        self.register_collision_object("Ship")
    
    def step(self):
        target_x, target_y = self.target.rect.center
        x, y = self.rect.center
        dx = target_x - x
        dy = target_y - y
        angle = (math.atan2(dy, dx) * 180 / math.pi)%360
        
        self.set_direction(angle, self.speed)
        
        # Rotate the image to point towards the player
        self.rotate_to_coordinate(target_x, target_y)

    def handle_collision(self, other, other_type):
        if other_type == "Ship":
            other.take_damage(self.damage)
            self.room.delete_object(self)

class Maw(RoomObject):
    def __init__(self, room, x, y, width, height, image, health, amalgamation = False):
        RoomObject.__init__(self, room, x, y)
        self.image_name = image
        self.image = self.load_image(image)
        self.set_image(self.image, width, height)
        self.health = health * Globals.difficulty
        self.max_health = health * Globals.difficulty
        self.register_collision_object("Laser")
        self.set_timer(30, self.spawn_spit)
        self.angle = 140

        bossbar = Bossbar(self.room, 0, 0, 56*4, 16, self, 2)
        self.room.add_room_object(bossbar)
        self.target = Target(self.room, 0, 0)
        self.room.add_room_object(self.target)

        self.amalgamation = amalgamation

    
    def handle_collision(self, other, other_type):
        if other_type == "Laser":
            self.health -= other.damage
            self.room.delete_object(other)
            if self.health <= 0:
                self.room.delete_object(self)
                if self.amalgamation:
                    self.room.amalgamation_amount -= 1
                    if self.room.amalgamation_amount == 0:
                        Globals.next_level = Globals.levels.index('VictoryRoom')
                        self.room.running = False
                else:
                    Globals.next_level = Globals.levels.index('VictoryRoom')
                    self.room.running = False
            pygame.mixer.Sound.play(pygame.mixer.Sound("Sounds\\cuthulu_hit.mp3"))

    def spawn_spit(self):
        for x in range(Globals.difficulty):
            self.set_timer(4 * x, self.spawn_shot)
        self.set_timer(20, self.spawn_spit)
    
    def spawn_shot(self):
        pygame.mixer.Sound.play(pygame.mixer.Sound("Sounds\\cuthulu_shoot.mp3"))
        self.room.add_room_object(Spit(self.room, Globals.SCREEN_WIDTH, self.y + self.height/2, 14, 30, "bosses\\cuthulu_shot.png", 15, 1, self.target))

class Target(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.direction = "forward"
        self.set_image(self.load_image("transparent.png"), 30, 30)
    
    def step(self):
        print(self.x, self.y)
        if self.direction == "forward":
            if self.x <= 0 and self.y <= 0:
                print("top left")
                self.set_direction(0, 14)
            elif self.x <= 0 and self.y >= Globals.SCREEN_HEIGHT:
                print("bottom left")
                self.set_direction(270, 14)
            elif self.x >= Globals.SCREEN_WIDTH and self.y <= 0:
                print("top right")
                self.set_direction(180, 14)
                self.direction = "backward"
        else:
            if self.x <= 0 and self.y <= 0:
                print("top left")
                self.set_direction(90, 14)
            elif self.x <= 0 and self.y >= Globals.SCREEN_HEIGHT:
                print("bottom left")
                self.set_direction(0, 14)
            elif self.x >= Globals.SCREEN_WIDTH and self.y >= Globals.SCREEN_HEIGHT:
                print("bottom right")
                self.set_direction(180, 14)
                self.direction = "forward"



class Spit(RoomObject):
    def __init__(self, room, x, y, width, height, image, speed, damage, target):
        RoomObject.__init__(self, room, x, y)
        self.image_name = image
        self.image = self.load_image(image)
        self.set_image(self.image, width, height)
        self.speed = speed
        self.damage = damage
        self.target = target

        self.register_collision_object("Ship")
    
        target_x, target_y = self.target.rect.center
        x, y = self.rect.center
        dx = target_x - x
        dy = target_y - y
        angle = (math.atan2(dy, dx) * 180 / math.pi)%360
        
        self.set_direction(angle, self.speed)
        
        # Rotate the image to point towards the player
        self.rotate_to_coordinate(target_x, target_y)

    def handle_collision(self, other, other_type):
        if other_type == "Ship":
            other.take_damage(self.damage)
            self.room.delete_object(self)
    
    def step(self):
        #check if the spit is outside
        if self.x < 0 or self.x > Globals.SCREEN_WIDTH or self.y < 0 or self.y > Globals.SCREEN_HEIGHT:
            self.room.delete_object(self)

class Better_Tentacle(RoomObject):
    def __init__(self, room, x, y, width, height, image, health, amalgamation = False):
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
        self.can_damage = True
        self.damage = 2 

        self.health = health * Globals.difficulty
        self.max_health = health * Globals.difficulty
        bossbar = Bossbar(self.room, 0, 0, 56*4, 16, self, 3)
        self.room.add_room_object(bossbar)

        self.register_collision_object("Laser")

        self.amalgamation = amalgamation

    def handle_collision(self, other, other_type):
        if other_type == "Laser":
            self.health -= other.damage
            self.room.delete_object(other)
            if self.health <= 0:
                self.room.delete_object(self)
                if self.amalgamation:
                    self.room.amalgamation_amount -= 1
                    if self.room.amalgamation_amount == 0:
                        Globals.next_level = Globals.levels.index('VictoryRoom')
                        self.room.running = False
                else:
                    Globals.next_level = Globals.levels.index('VictoryRoom')
                    self.room.running = False
            pygame.mixer.Sound.play(pygame.mixer.Sound("Sounds\\cuthulu_hit.mp3"))


    def step(self):
        self.attack()

    def key_pressed(self, key):
        if (key[pygame.K_w] or key[pygame.K_a] or key[pygame.K_s] or key[pygame.K_d] or key[pygame.K_SPACE]) and key != self.last_pressed:
            self.last_pressed = key
            self.spam_keys.append(key)

    #function for tip to gradually move to player
    def move_to_player(self):
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
                spam_text = Fading_Text(self.room, self.x, self.y, "Spam W, A, S, and D", 60)
                self.room.add_room_object(spam_text)

    def pull(self):
        if len(self.spam_keys) > 30:
            if self.x < Globals.SCREEN_WIDTH - 100:
                self.set_direction(0, self.speed * 5)
            else:
                self.set_direction(0, 0)
                self.going_to_player = True
        else:
            if self.can_damage:
                pygame.mixer.Sound.play(pygame.mixer.Sound("Sounds\\cuthulu_shoot.mp3"))
                self.room.ship.take_damage(self.damage)
                self.can_damage = False
                self.set_timer(45, self.can_damage_timer)
            self.set_direction(0, self.speed)
            self.room.ship.set_direction(0, self.speed)
            self.y = self.room.ship.y + self.room.ship.height/2 - self.height/3
            self.x = self.room.ship.x + self.room.ship.width/2
    
    def can_damage_timer(self):
        self.can_damage = True
    

    def update_image(self):
        self.set_image(self.load_image(self.image_name), self.width, self.height)
