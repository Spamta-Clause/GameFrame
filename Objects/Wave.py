from GameFrame import RoomObject
class Wave(RoomObject):
    def __init__(self, enemies = [], interval = 30, room = None):
        RoomObject.__init__(self,room,0,0)
        self.total_enemies = enemies
        self.enemies = enemies
        print(self.total_enemies)
        self.interval = interval
        self.room = room
        self.index = 0
        self.enemies_slain = 0

    def spawn_next(self):
        self.room.add_room_object(self.total_enemies[self.index])
        self.set_timer(self.interval,self.spawn_next)
        self.index += 1
        if self.index >= len(self.total_enemies):
            self.room.delete_object(self)

    def enemy_dead(self, enemy):
        print(self.enemies)
        self.enemies_slain += 1

        if len(self.total_enemies) == self.enemies_slain:
            print('wave killed')