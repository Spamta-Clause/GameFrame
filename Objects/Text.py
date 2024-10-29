from GameFrame import TextObject

class Title(TextObject):
    """
    A class for displaying the current score
    """
    def __init__(self, room, x: int, y: int, text=None):
        """
        Intialises the score object
        """         
        # include attributes and methods from TextObject
        TextObject.__init__(self, room, x, y, text)
        
        # set values         
        self.size = 60
        self.font = 'Flux Boxes'
        self.colour = (255,255,255,255)
        self.bold = False
        self.update_text()
class Default(TextObject):
    def __init__(self, room, x: int, y: int, text=None):
        """
        Intialises the score object
        """         
        # include attributes and methods from TextObject
        TextObject.__init__(self, room, x, y, text)
        
        # set values         
        self.size = 30
        self.font = 'Flux Boxes'
        self.colour = (255,255,255,255)
        self.bold = False
        self.update_text()
    def set_opacity(self, alpha: int):
        """
        Sets the opacity of the text.
        :param alpha: Opacity value (0-255)
        """
        r, g, b, _ = self.colour
        self.colour = (r, g, b, alpha)
        self.update_text()
    def set_colour(self, colour: tuple):
        """
        Sets the colour of the text.
        :param colour: RGB colour tuple
        """
        _, _, _, a = self.colour
        self.colour = colour + (a,)
        self.update_text()