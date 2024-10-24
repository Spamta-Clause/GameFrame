from GameFrame import Level, Globals
from Objects.Text import Title
from Objects.Slide import Slide

class TutorialRoom(Level):
    """
    Intial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.title = Title(self, 
                           Globals.SCREEN_WIDTH/2, 20, 
                           "Galactic Oil Harvesters")
        self.title.x = Globals.SCREEN_WIDTH/2 - self.title.width/2
        self.add_room_object(self.title)

        # TODO
        # Add the actual slides and make them use the centering code with added vertical support

        slide_one = Slide(self, Globals.SCREEN_WIDTH/2, Globals.SCREEN_HEIGHT/2, "Welcome to Galactic Oil Harvesters","1")
        slide_two = Slide(self, 0, Globals.SCREEN_HEIGHT/2, "Use the arrow keys to move","2")
        self.slides = [slide_one, slide_two]
        self.current_slide = 0
        self.add_room_object(slide_one)

        self.set_background_image('background.png')
        