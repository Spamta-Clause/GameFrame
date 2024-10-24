from Objects.Enemy_Base import Enemy_Base
from Objects.Laser import Laser

class Laser_Cruiser(Enemy_Base):
    def __init__(self, room, x, y, image, width, height, speed, target, health, too_close_for_comfort, fire_rate, wave):
        Enemy_Base.__init__(self, room, x, y, image, width, height, speed, target, health, too_close_for_comfort, wave)
        
        self.fire_rate = fire_rate
        self.fire_timer = 0
        self.curr_angle = 0
        self.frame = 0
        
        # self.frames = []
        # for x in range(1,16,5):
        #     print(x)
        #     self.frames.append(self.load_image(f"laser_cruiser\\laser_cruiser_{x}.png"))
    
    def step(self):
        super().step()

        # print(self.frame)
        # print(self.frames)
        # if self.frame == 2:
        #     self.frame = 0
        #     print("frame reset")
        # else:
        #     self.frame += 1
        # self.set_image(self.frames[self.frame], self.width, self.height)

        self.move_to_target()

        target_x, target_y = self.target.rect.center
        if target_x < self.rect.centerx:
            angle = self.rotate_to_coordinate(target_x, target_y)
            self.rotate(90)
        else:
            angle = self.rotate_to_coordinate(target_x, target_y)
            self.rotate(2 * angle)
            self.rotate(90)

        
        
        self.fire_timer += 1
        if self.fire_timer >= self.fire_rate:
            self.fire_timer = 0
            self.fire()
        #could just do it with timer but idc
    
    def fire(self):
        laser = Laser(self.room, self.x + self.width/2, self.y + self.height/2, "laser.png", 8, 8, 10, (360-self.angle)%360, 1, self)
        self.room.add_room_object(laser)