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
                           "Aspects of Cuthulu")
        self.title.x = Globals.SCREEN_WIDTH/2 - self.title.width/2
        self.add_room_object(self.title)

        # TODO
        # Add the actual slides and make them use the centering code with added vertical support

        slide_one = Slide(self, Globals.SCREEN_WIDTH/2, Globals.SCREEN_HEIGHT/2, "Welcome to Aspects of Cuthulu! Press space to go to the next slide!","1",30)
        slide_two = Slide(self, Globals.SCREEN_WIDTH/2, Globals.SCREEN_HEIGHT/2, "Use W and S to move, press A and D to rotate your ship.","2",30)
        slide_three = Slide(self, Globals.SCREEN_WIDTH/2, Globals.SCREEN_HEIGHT/2, "Press left-click to shoot. And press right-click to drill.","3",30)
        slide_four = Slide(self, Globals.SCREEN_WIDTH/2, Globals.SCREEN_HEIGHT/2, "But some asteroids are tougher than others, so make sure to upgrade your drill.","4",30)
        slide_one.x = Globals.SCREEN_WIDTH/2 - slide_one.width/2
        slide_two.x = Globals.SCREEN_WIDTH/2 - slide_two.width/2
        slide_three.x = Globals.SCREEN_WIDTH/2 - slide_three.width/2
        slide_four.x = Globals.SCREEN_WIDTH/2 - slide_four.width/2
        self.slides = [slide_one, slide_two, slide_three, slide_four]
        self.current_slide = 0
        self.add_room_object(slide_one)

        self.set_background_image('background.png')
        