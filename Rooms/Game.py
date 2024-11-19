from GameFrame import Level
from Objects.Ship import Ship
from Objects.Smash import Smash
from Objects.Laser_Cruiser import Laser_Cruiser
from Objects.Unstable import Unstable
from Objects.Ship_Cruiser import Ship_Cruiser
from Objects.Asteroid import Asteroid
from GameFrame import Globals
from Objects.Wave import Wave
from Objects.Heart import Heart
from Objects.Cuthulu import Fake_Eye, Eye, Maw, Spit, Better_Tentacle
from Objects.Fading_Text import Fading_Text
import random, time, pygame

class Game(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        #self.level = level
        self.set_background_image('background.png')
        self.background_scrolling = True
        self.background_scroll_speed = 1

        pygame.mixer.init()
        pygame.mixer.music.load('Sounds\\main_theme.mp3')
        pygame.mixer.music.play(-1)
        

        #self.add_room_object(Unstable(self, 900, 500, 'boom.png', 32, 18, 3, ship, 150, 90,1))
        #self.add_room_object(Ship_Cruiser(self, 700, 500, 'ship.png', 29*3, 32*3, 0.75, ship, 3, 350, 75))
        self.basic_startup()
        match Globals.level:
            case 1:
                self.level_one()
            case 2:
                self.level_two()
            case 3:
                self.level_three()
            case 4:
                self.level_four()
        
    
    def basic_startup(self):
        match Globals.current_powerup:
            case "shield-1":
                self.shield = 1
            case "shield-2":
                self.shield = 2
            case "shield-3":
                self.shield = 3
            case _:
                self.shield = 0

        self.hearts = []
        print(self.shield)
        for i in range(Globals.armour):
            self.hearts.append(Heart(self, 20 + (i * 50), 20))
            self.add_room_object(self.hearts[i])
        self.shield_hearts = []

        for i in range(self.shield):
            new_heart = Heart(self, 20 + (i * 50), 50)
            self.shield_hearts.append(new_heart)
            new_heart.set_value('shield')
            self.add_room_object(self.shield_hearts[i])
        self.hearts_arrays = [self.hearts, self.shield_hearts]

        self.ship = Ship(self, 100, Globals.SCREEN_HEIGHT/2, 58, 64, 45)
        self.add_room_object(self.ship)

        self.set_timer(150, self.spawn_asteroid)

    def remove_heart(self, damage):
        for i in range(damage):
            final_array = self.hearts_arrays[-1]
            if len(final_array) == 0 or final_array == None:
                self.hearts_arrays.pop()
                final_array = self.hearts_arrays[-1]
            print(final_array)
            print(len(final_array))
            final_heart = final_array[-1]
            
            final_array.pop(-1)
            if final_heart.value == 'shield':
                self.delete_object(final_heart)
            else:
                final_heart.set_value('empty')
            if len(self.hearts) == 0:
                Globals.next_level = Globals.levels.index('Menu')
                self.running = False
                break

    def update_hearts(self, type):
        for heart in self.hearts:
            heart.set_value(type)
    def shield_hearts(self, amount):
        for heart in range(amount):
            self.hearts[heart].set_value('shield')

    def let_forth_the_maw(self):
        maw = Maw(self, 200, 500, 26*3, 115*3, 'bosses\\cuthulu.png', 40)
        maw.x = Globals.SCREEN_WIDTH - maw.width
        maw.y = Globals.SCREEN_HEIGHT/2 - maw.height/2
        self.add_room_object(maw)

        pygame.mixer.music.stop()
        pygame.mixer.music.load('Sounds\\boss_theme.mp3')
        pygame.mixer.music.play(-1)
    
    def let_forth_the_eyes(self):
        fake_eye_positions = {
            1: [0, 180],
            2: [0, 120, 240],
            3: [0, 120, 180, 270]
        }

        for heading in fake_eye_positions.get(Globals.difficulty, []):
            if heading != 0:
                fake_eye = Fake_Eye(self, Globals.SCREEN_WIDTH/2, Globals.SCREEN_HEIGHT/2, 32*2, 32*2, 'fake_weakspot.png')
                self.add_room_object(fake_eye)
                fake_eye.current_heading = heading
            else:
                eye = Eye(self, Globals.SCREEN_WIDTH/2, Globals.SCREEN_HEIGHT/2, 32*2, 32*2, 'bosses\\weakspot.png', 30)
                self.add_room_object(eye)
                eye.current_heading = heading
    
    def let_forth_the_grasping_tentacles(self):
        better_tentacle = Better_Tentacle(self, Globals.SCREEN_WIDTH, 0, 476*4, 32*4, 'bosses\\tentacle.png', 50)
        self.add_room_object(better_tentacle)
        

    def level_one(self):
        self.set_timer(30 * 45, self.let_forth_the_maw)

        first_wave = Wave(self)
        smash_1 = Smash(self, 1200, random.randint(120, 600), 'spinny.png', 32, 18, 3, self.ship, 1, 1, 20, first_wave)
        first_wave.enemies = [smash_1]
        first_wave.total_enemies = [smash_1]
        first_wave.interval = 1
        
        second_wave = Wave(self)
        smash_2 = Smash(self, 1200, random.randint(120, 600), 'spinny.png', 32, 18, 3, self.ship, 1, 1, 20, second_wave)
        smash_3 = Smash(self, 1200, random.randint(120, 600), 'spinny.png', 32, 18, 3, self.ship, 1, 1, 20, second_wave)
        second_wave.enemies = [smash_2, smash_3]
        second_wave.total_enemies = [smash_2, smash_3]
        second_wave.interval = 30

        third_wave = Wave(self)
        laser_cruiser_1 = Laser_Cruiser(self, 1200, random.randint(120, 600), 'laser_cruiser\\laser_cruiser_1.png', 29*3, 32*3, 0.75, self.ship, 3, 350, 75, third_wave)
        smash_4 = Smash(self, 1200, random.randint(120, 600), 'spinny.png', 32, 18, 3, self.ship, 1, 1, 20, third_wave)
        third_wave.enemies = [laser_cruiser_1, smash_4]
        third_wave.total_enemies = [laser_cruiser_1, smash_4]
        third_wave.interval = 45

        fourth_wave = Wave(self)
        ship_cruiser_1 = Ship_Cruiser(self, 1200, random.randint(120, 600), 'ship_cruiser.png', 29*3, 32*3, 0.75, self.ship, 3, 350, 75, fourth_wave)
        smash_5 = Smash(self, 1200, random.randint(120, 600), 'spinny.png', 32, 18, 3, self.ship, 1, 1, 20, fourth_wave)
        laser_cruiser_2 = Laser_Cruiser(self, 1200, random.randint(120, 600), 'laser_cruiser\\laser_cruiser_1.png', 29*3, 32*3, 0.75, self.ship, 3, 350, 75, fourth_wave)
        fourth_wave.enemies = [ship_cruiser_1, smash_5, laser_cruiser_2]
        fourth_wave.total_enemies = [ship_cruiser_1, smash_5, laser_cruiser_2]
        fourth_wave.interval = 60

        first_wave.next_wave = second_wave
        second_wave.next_wave = third_wave
        third_wave.next_wave = fourth_wave

        first_wave.spawn_next()
    
    def level_two(self):
        self.set_timer(30 * 45, self.let_forth_the_eyes)

        first_wave = Wave(self)
        smash_1 = Smash(self, 1200, random.randint(120, 600), 'spinny.png', 32, 18, 3, self.ship, 1, 1, 20, first_wave)
        smash_2 = Smash(self, 1200, random.randint(120, 600), 'spinny.png', 32, 18, 3, self.ship, 1, 1, 20, first_wave)
        smash_3 = Smash(self, 1200, random.randint(120, 600), 'spinny.png', 32, 18, 3, self.ship, 1, 1, 20, first_wave)
        first_wave.enemies = [smash_1, smash_2, smash_3]
        first_wave.total_enemies = [smash_1, smash_2, smash_3]
        first_wave.interval = 1

        second_wave = Wave(self)
        smash_4 = Smash(self, 1200, random.randint(120, 600), 'spinny.png', 32, 18, 3, self.ship, 1, 1, 20, second_wave)
        ship_cruiser_1 = Ship_Cruiser(self, 1200, random.randint(120, 600), 'ship_cruiser.png', 29*3, 32*3, 0.75, self.ship, 3, 350, 75, second_wave)
        smash_5 = Smash(self, 1200, random.randint(120, 600), 'spinny.png', 32, 18, 3, self.ship, 1, 1, 20, second_wave)
        second_wave.enemies = [smash_4, ship_cruiser_1, smash_5]
        second_wave.total_enemies = [smash_4, ship_cruiser_1, smash_5]
        second_wave.interval = 20

        third_wave = Wave(self)
        ship_cruiser_2 = Ship_Cruiser(self, 1200, random.randint(120, 600), 'ship_cruiser.png', 29*3, 32*3, 0.75, self.ship, 3, 350, 75, third_wave)
        smash_6 = Smash(self, 1200, random.randint(120, 600), 'spinny.png', 32, 18, 3, self.ship, 1, 1, 20, third_wave)
        smash_7 = Smash(self, 1200, random.randint(120, 600), 'spinny.png', 32, 18, 3, self.ship, 1, 1, 20, third_wave)
        smash_8 = Smash(self, 1200, random.randint(120, 600), 'spinny.png', 32, 18, 3, self.ship, 1, 1, 20, third_wave)
        laser_cruiser_1 = Laser_Cruiser(self, 1200, random.randint(120, 600), 'laser_cruiser\\laser_cruiser_1.png', 29*3, 32*3, 0.75, self.ship, 3, 350, 75, third_wave)
        third_wave.enemies = [ship_cruiser_2, smash_6, smash_7, smash_8, laser_cruiser_1]
        third_wave.total_enemies = [ship_cruiser_2, smash_6, smash_7, smash_8, laser_cruiser_1]
        third_wave.interval = 30

        fourth_wave = Wave(self)
        laser_cruiser_2 = Laser_Cruiser(self, 1200, random.randint(120, 600), 'laser_cruiser\\laser_cruiser_1.png', 29*3, 32*3, 0.75, self.ship, 3, 350, 75, fourth_wave)
        laser_cruiser_3 = Laser_Cruiser(self, 1200, random.randint(120, 600), 'laser_cruiser\\laser_cruiser_1.png', 29*3, 32*3, 0.75, self.ship, 3, 350, 75, fourth_wave)
        ship_cruiser_3 = Ship_Cruiser(self, 1200, random.randint(120, 600), 'ship_cruiser.png', 29*3, 32*3, 0.75, self.ship, 3, 350, 75, fourth_wave)
        ship_cruiser_4 = Ship_Cruiser(self, 1200, random.randint(120, 600), 'ship_cruiser.png', 29*3, 32*3, 0.75, self.ship, 3, 350, 75, fourth_wave)
        fourth_wave.enemies = [laser_cruiser_2, laser_cruiser_3, ship_cruiser_3, ship_cruiser_4]
        fourth_wave.total_enemies = [laser_cruiser_2, laser_cruiser_3, ship_cruiser_3, ship_cruiser_4]
        fourth_wave.interval = 40

        first_wave.next_wave = second_wave
        second_wave.next_wave = third_wave
        third_wave.next_wave = fourth_wave

        first_wave.spawn_next()
    
    def level_three(self):
        self.set_timer(30 * 45, self.let_forth_the_grasping_tentacles)

        first_wave = Wave(self)
        laser_cruiser_1 = Laser_Cruiser(self, 1200, random.randint(120, 600), 'laser_cruiser\\laser_cruiser_1.png', 29*3, 32*3, 0.75, self.ship, 3, 350, 75, first_wave)
        first_wave.enemies = [laser_cruiser_1]
        first_wave.total_enemies = [laser_cruiser_1]
        first_wave.interval = 1

        second_wave = Wave(self)
        laser_cruiser_2 = Laser_Cruiser(self, 1200, random.randint(120, 600), 'laser_cruiser\\laser_cruiser_1.png', 29*3, 32*3, 0.75, self.ship, 3, 350, 75, second_wave)
        ship_cruiser_1 = Ship_Cruiser(self, 1200, random.randint(120, 600), 'ship_cruiser.png', 29*3, 32*3, 0.75, self.ship, 3, 350, 75, second_wave)
        second_wave.enemies = [laser_cruiser_2, ship_cruiser_1]
        second_wave.total_enemies = [laser_cruiser_2, ship_cruiser_1]
        second_wave.interval = 20

        third_wave = Wave(self)
        laser_cruiser_3 = Laser_Cruiser(self, 1200, random.randint(120, 600), 'laser_cruiser\\laser_cruiser_1.png', 29*3, 32*3, 0.75, self.ship, 3, 350, 75, third_wave)
        laser_cruiser_4 = Laser_Cruiser(self, 1200, random.randint(120, 600), 'laser_cruiser\\laser_cruiser_1.png', 29*3, 32*3, 0.75, self.ship, 3, 350, 75, third_wave)
        laser_cruiser_5 = Laser_Cruiser(self, 1200, random.randint(120, 600), 'laser_cruiser\\laser_cruiser_1.png', 29*3, 32*3, 0.75, self.ship, 3, 350, 75, third_wave)
        smash_1 = Smash(self, 1200, random.randint(120, 600), 'spinny.png', 32, 18, 3, self.ship, 1, 1, 20, third_wave)
        smash_2 = Smash(self, 1200, random.randint(120, 600), 'spinny.png', 32, 18, 3, self.ship, 1, 1, 20, third_wave)
        smash_3 = Smash(self, 1200, random.randint(120, 600), 'spinny.png', 32, 18, 3, self.ship, 1, 1, 20, third_wave)
        smash_4 = Smash(self, 1200, random.randint(120, 600), 'spinny.png', 32, 18, 3, self.ship, 1, 1, 20, third_wave)
        third_wave.enemies = [laser_cruiser_3, laser_cruiser_4, laser_cruiser_5, smash_1, smash_2, smash_3, smash_4]
        third_wave.total_enemies = [laser_cruiser_3, laser_cruiser_4, laser_cruiser_5, smash_1, smash_2, smash_3, smash_4]
        third_wave.interval = 30

        first_wave.next_wave = second_wave
        second_wave.next_wave = third_wave

        first_wave.spawn_next()
    
    def text_one(self):
        fading_text = Fading_Text(self, Globals.SCREEN_WIDTH/2, Globals.SCREEN_HEIGHT/2, 'Prepare for the final battle!', 60, (255,255,255,255))
        fading_text.x = Globals.SCREEN_WIDTH/2 - fading_text.width/2
        fading_text.y = Globals.SCREEN_HEIGHT/2 - fading_text.height/2
        self.add_room_object(fading_text)

    def text_two(self):
        fading_text = Fading_Text(self, Globals.SCREEN_WIDTH/2, Globals.SCREEN_HEIGHT/2, 'It will be hard.', 60, (255,255,255,255))
        fading_text.x = Globals.SCREEN_WIDTH/2 - fading_text.width/2
        fading_text.y = Globals.SCREEN_HEIGHT/2 - fading_text.height/2
        self.add_room_object(fading_text)

    def text_three(self):
        fading_text = Fading_Text(self, Globals.SCREEN_WIDTH/2, Globals.SCREEN_HEIGHT/2, 'Maybe even impossible.', 60, (255,255,255,255))
        fading_text.x = Globals.SCREEN_WIDTH/2 - fading_text.width/2
        fading_text.y = Globals.SCREEN_HEIGHT/2 - fading_text.height/2
        self.add_room_object(fading_text)
    

        

    def level_four(self):
        self.set_timer(0, self.text_one)
        self.set_timer(60, self.text_two)
        self.set_timer(120, self.text_three)

        self.amalgamation_amount = 3
        better_tentacle = Better_Tentacle(self, Globals.SCREEN_WIDTH, 0, 476*4, 32*4, 'bosses\\tentacle.png', 5, True)
        self.add_room_object(better_tentacle)
        
        maw = Maw(self, 200, 500, 26*3, 115*3, 'bosses\\cuthulu.png', 10, True)
        maw.x = Globals.SCREEN_WIDTH - maw.width
        maw.y = Globals.SCREEN_HEIGHT/2 - maw.height/2
        self.add_room_object(maw)

        fake_eye_positions = {
            1: [0, 180],
            2: [0, 120, 240],
            3: [0, 90, 180, 270]
        }
        eye = Eye(self, Globals.SCREEN_WIDTH/2, Globals.SCREEN_HEIGHT/2, 32*2, 32*2, 'bosses\\weakspot.png', 1, True)
        self.add_room_object(eye)
        eye.current_heading = 0


        for heading in fake_eye_positions.get(Globals.difficulty, []):
            if heading != 0:
                fake_eye = Fake_Eye(self, Globals.SCREEN_WIDTH/2, Globals.SCREEN_HEIGHT/2, 32*2, 32*2, 'fake_weakspot.png')
                self.add_room_object(fake_eye)
                fake_eye.current_heading = heading
                eye.fake_eyes.append(fake_eye)
                


    def spawn_asteroid(self):
        speed = random.choice([1 ,2,2 ,3,3,3 ,4,4 ,5])
            
        self.add_room_object(Asteroid(self,Globals.SCREEN_WIDTH,random.randint(0,Globals.SCREEN_WIDTH),speed))
        self.set_timer(150, self.spawn_asteroid)

