from GameFrame import Level, Globals
from Objects.Text import Title, Default
from Objects.Button import Button


class VictoryRoom(Level):
    """
    Victory screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.title = Title(self, 
                           Globals.SCREEN_WIDTH/2, 20, 
                           "Congratulations!")
        self.title.x = Globals.SCREEN_WIDTH/2 - self.title.width/2
        self.add_room_object(self.title)

        # TODO
        # Add the actual slides and make them use the centering code with added vertical support


        self.set_background_image('background.png')
        back_button = Button(self, 600, 600, 'back.png', 64, 64,self.back)
        self.add_room_object(back_button)

        self.text = Default(self, 100, 100, f"You have beaten this level! Have {30 * Globals.difficulty * Globals.level} of each oil!")
        self.text.x = Globals.SCREEN_WIDTH/2 - self.text.width/2
        self.add_room_object(self.text)
        Globals.diamond_oil += 30 * Globals.difficulty * Globals.level
        Globals.gold_oil += 30 * Globals.difficulty * Globals.level
        Globals.emerald_oil += 30 * Globals.difficulty * Globals.level
        Globals.ruby_oil += 30 * Globals.difficulty * Globals.level
        if Globals.level < Globals.max_level:
            Globals.level += 1

    def back(self):
        Globals.next_level = Globals.levels.index('Menu')
        self.running = False
