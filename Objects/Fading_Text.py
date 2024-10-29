from GameFrame import TextObject

class Fading_Text(TextObject):
    """
    A class for displaying the current score
    """
    def __init__(self, room, x: int, y: int, text=None, time=60, colour = (255,255,255,255)):
        """
        Intialises the score object
        """         
        # include attributes and methods from TextObject
        TextObject.__init__(self, room, x, y, text)
        
        # set values         
        self.size = 25
        self.font = 'Flux Boxes'
        self.colour = colour  # RGBA: white with full opacity
        self.bold = False
        self.update_text()
        self.ticks = 0
        self.time = time
    
    def step(self):
        self.set_opacity(255 - (255 * self.ticks / self.time))
        if self.ticks >= self.time:
            self.room.delete_object(self)
        self.ticks += 1
    
    def set_opacity(self, alpha: int):
        """
        Sets the opacity of the text.
        :param alpha: Opacity value (0-255)
        """
        r, g, b, _ = self.colour
        self.colour = (r, g, b, alpha)
        self.update_text()