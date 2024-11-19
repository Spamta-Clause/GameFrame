class Globals:

    running = True
    FRAMES_PER_SECOND = 30

    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    # - Set the Window display name - #
    window_name = 'Aspects of Cuthulu'

    # - Set the order of the rooms - #
    levels = ["TutorialRoom","Menu","Gambling","Game","VictoryRoom","UpgradeRoom"]

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

    current_powerup = ""

    diamond_oil = 0
    gold_oil = 0
    emerald_oil = 0
    ruby_oil = 0

    difficulty = 3

    level = 4
    max_level = 4 
