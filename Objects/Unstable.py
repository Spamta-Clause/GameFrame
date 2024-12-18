from Objects.Enemy_Base import Enemy_Base

class Unstable(Enemy_Base):
    def __init__(self, room, x, y, image, width, height, speed, target, unstable_duration, explosion_size, damage, wave):
        Enemy_Base.__init__(self, room, x, y, image, width, height, speed, target, False, False, wave)
        
        self.unstable_duration = unstable_duration
        self.explosion_size = explosion_size
        self.is_exploding = False
        self.damage = damage

        self.set_timer(unstable_duration, self.explode)
    
    def explode(self):
        print("exploding")
        self.is_exploding = True
        self.width = self.explosion_size
        self.height = self.explosion_size
        self.set_timer(5, self.die)

    def die(self):
        print("die")
        self.room.delete_object(self)
        if self.wave != None:
            self.wave.enemy_dead(self)



    def step(self):
        #painful trigonometry but in a function so i dont have to look at it and reminisce about the pain it caused me
        self.move_to_target()

        target_x, target_y = self.target.rect.center
        if target_x < self.rect.centerx:
            angle = self.rotate_to_coordinate(target_x, target_y)
            self.rotate(90)
        else:
            angle = self.rotate_to_coordinate(target_x, target_y)
            self.rotate(2 * angle)
            self.rotate(90)
        
    def handle_collision(self, other, other_type):
        if not self.is_exploding:
            self.explode()
        else:
            if other_type != "Laser":
                other.take_damage(self.damage)