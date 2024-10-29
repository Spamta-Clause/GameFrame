from GameFrame import RoomObject, Globals
import math

class Enemy_Base(RoomObject):
    def __init__(self, room, x, y, image, width, height, speed, target, health, too_close_for_comfort = False, wave = None):
        RoomObject.__init__(self, room, x, y)
       
        self.image = self.load_image(image)
        self.set_image(self.image, width, height)

        self.speed = speed
        self.target = target

        self.health = health

        self.register_collision_object("Laser")
        self.register_collision_object("Ship")

        self.too_close_for_comfort = too_close_for_comfort

        self.wave = wave
    
    def move_to_target(self):
        target_x, target_y = self.target.rect.center
        x, y = self.rect.center
        dx = target_x - x
        dy = target_y - y
        self.angle = (math.atan2(dy, dx) * 180 / math.pi)%360
        #finds distance, checks if within social distancing requirements

        if self.too_close_for_comfort == True:
            if abs(math.sqrt(dx**2 + dy**2)) < self.too_close_for_comfort:
                self.set_direction(self.angle, -self.speed)
                #should back away
            elif abs(math.sqrt(dx**2 + dy**2)) < self.too_close_for_comfort+100:
                self.set_direction(self.angle, 0)
        else:
            self.set_direction(self.angle, self.speed)

    def face_target_angle(self):
        player_x, player_y = self.target.rect.center
        dx = player_x - self.x
        dy = player_y - self.y
        angle_to_player = math.degrees(math.atan2(dy, dx))

        self.curr_rotation =  angle_to_player
        return angle_to_player

    def take_damage(self, damage):
        if self.health != False:
            self.health -= damage
            if self.health <= 0:
                self.wave.enemy_dead(self)
                self.room.delete_object(self)

    def handle_collision(self, other, other_type):
        if other_type == "Laser":
            if other.shooter != self:
                self.take_damage(other.damage)
                self.room.delete_object(other)
                print("hit")

    def step(self):
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