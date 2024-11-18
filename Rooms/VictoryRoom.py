from GameFrame import Level, Globals
from Objects.Text import Title


class VictoryRoom(Level):
    """
    Victory screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.title = Title(self, 
                           Globals.SCREEN_WIDTH/2, 20, 
                           "Congratulations! You Won!")
        self.title.x = Globals.SCREEN_WIDTH/2 - self.title.width/2
        self.add_room_object(self.title)

        # TODO
        # Add the actual slides and make them use the centering code with added vertical support


        self.set_background_image('background.png')