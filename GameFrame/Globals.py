
class Globals:

    running = True
    FRAMES_PER_SECOND = 30

    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    # - Set the Window display name - #
    window_name = 'Galactic Oil Harvesters'

    # - Set the order of the rooms - #
    levels = ["UpgradeRoom", "TutorialRoom","Menu","Gambling","Game"]

    LIVES = 0
    # - Set the starting level - #
    start_level = 0

    # - Set this number to the level you want to jump to when the game ends - #
    end_game_level = 4

    # - This variable keeps track of the room that will follow the current room - #
    # - Change this value to move through rooms in a non-sequential manner - #
    next_level = 0

    # - Change variable to True to exit the program - #
    exiting = False


# ############################################################# #
# ###### User Defined Global Variables below this line ######## #
# ############################################################# #

    speed = 5
    laser = 1
    armour = 3
    drill = 1

    current_powerup = "immunity-1"

    diamond_oil = 999
    gold_oil = 999
    emerald_oil = 999
    ruby_oil = 999
