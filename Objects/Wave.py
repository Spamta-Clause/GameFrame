from GameFrame import RoomObject
class Wave(RoomObject):
    def __init__(self, room, enemies = [], interval = 30, next_wave = None):
        RoomObject.__init__(self,room,0,0)
        self.total_enemies = enemies
        self.enemies = enemies
        self.interval = interval
        self.room = room
        self.index = 0
        self.enemies_slain = 0
        self.next_wave = next_wave

    def spawn_next(self):
        self.room.add_room_object(self.total_enemies[self.index])
        self.set_timer(self.interval,self.spawn_next)
        self.index += 1
        if self.index >= len(self.total_enemies):
            self.room.delete_object(self)

    def enemy_dead(self, enemy):
        # print(self.total_enemies)
        # self.enemies_slain += 1

        # if len(self.total_enemies) == self.enemies_slain:
        #     if self.next_wave != None:
        #         print("spawn next")
        #         self.next_wave.spawn_next()
        #     print('wave killed')
        self.enemies_slain += 1

        if self.enemies_slain == len(self.total_enemies):
            if self.next_wave is not None:
                self.next_wave.spawn_next()