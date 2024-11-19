from Objects.Text import Title
import pygame

class Slide(Title):
    def __init__(self, room, x, y, text, name, size):
        """
        Intialises the score object
        """         
        # include attributes and methods from TextObject
        Title.__init__(self, room, x, y, text)
        
        # set values         
        self.size = size
        self.font = 'Flux Boxes'
        self.colour = (255,255,255,255)
        self.bold = False
        self.update_text()
        
        self.created()

        self.name = name

        self.handle_key_events = True
    
    def key_pressed(self, key):
        if key[pygame.K_SPACE] and self.can_swap:
            self.can_swap = False
            self.room.current_slide += 1
            if self.room.current_slide >= len(self.room.slides):
                self.room.running = False
            else:
                next_slide = self.room.slides[self.room.current_slide]
                self.room.add_room_object(next_slide)
                next_slide.created()
                self.room.delete_object(self.room.slides[self.room.current_slide-1])
                
    
    def reset_swap(self):
        self.can_swap = True

    def created(self):
        self.can_swap = False
        self.set_timer(8,self.reset_swap)
