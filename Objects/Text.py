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
        self.font = 'Neon Future 2.0 Demo'
        self.colour = (255,255,255)
        self.bold = False
        self.update_text()