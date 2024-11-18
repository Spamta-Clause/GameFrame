from Objects.Text import Default
from GameFrame import RoomObject, Globals
import random

class Roulette_Manager(RoomObject):
    def __init__(self,room,x,y):
        RoomObject.__init__(self, room, x, y)
        self.image = self.load_image("transparent.png")
        self.set_image(self.image, 96, 96)
        self.room = room

        self.bottom_threshold = 690
        self.top_threshold = 30
        self.total_range = self.bottom_threshold - self.top_threshold
        
        self.speed = 0
        self.deceleration = 0.025
        
        # List of tier names
        self.tier_names = []
        for y in range(3):
            self.tier_names.append("LVL 1 - Ship Shield")
            self.tier_names.append("LVL 1 - Damage Boost")
            self.tier_names.append("10s - Immunity")
        for y in range(2):
            self.tier_names.append("LVL 2 - Ship Shield")
            self.tier_names.append("LVL 2 - Damage Boost")
            self.tier_names.append("20s - Immunity")
        self.tier_names.append("LVL 3 - Ship Shield")
        self.tier_names.append("LVL 3 - Damage Boost") 
        self.tier_names.append("30s - Immunity")
        random.shuffle(self.tier_names)

        # Create text objects for each tier
        self.tier_texts = []
        for i, name in enumerate(self.tier_names):
            text = Default(self.room, Globals.SCREEN_WIDTH/2, Globals.SCREEN_HEIGHT/2 + i * 60, name)
            text.x = Globals.SCREEN_WIDTH/2 - text.width/2 
            match text.text:
                case "LVL 1 - Ship Shield":
                    text.set_colour((36, 159, 222))
                case "LVL 2 - Ship Shield":
                    text.set_colour((40, 92, 196))
                case "LVL 3 - Ship Shield":
                    text.set_colour((20, 52, 100))
                case "LVL 1 - Damage Boost":
                    text.set_colour((250, 106, 10))
                case "LVL 2 - Damage Boost":
                    text.set_colour((223, 62, 35))
                case "LVL 3 - Damage Boost":
                    text.set_colour((180, 32, 42))
                case "10s - Immunity":
                    text.set_colour((255, 224, 130))
                case "20s - Immunity":
                    text.set_colour((255, 193, 7))
                case "30s - Immunity":
                    text.set_colour((255, 111, 0))
            self.room.add_room_object(text)
            self.tier_texts.append(text)
        
        self.tier = None
    
        # Flag to control movement
        self.is_gambling = False
        
    def calculate_opacity(self, text):
        distance_from_center = abs(text.y - self.top_threshold - (self.total_range / 2))
                
        # Calculate transparency based on distance from center
        max_distance = self.total_range
        alpha = max(0, 255 - int((distance_from_center / max_distance) * (255*4)))
        text.set_opacity(alpha)

    def step(self):
        if self.is_gambling:
            # Update positions and transparency of tier texts
            for text in self.tier_texts:
                text.y -= self.speed  # Move up
                if text.y < self.top_threshold - text.height:  # If it goes off the top, move to the bottom
                    text.y = self.bottom_threshold
                
                self.calculate_opacity(text)
            
            
            self.speed -= self.deceleration * self.speed  # Decelerate
            if self.speed <= 0.2:
                self.is_gambling = False
                self.speed = 0
                # Round y positions to the nearest multiple of 50
                tiers_positions = set()
                # Sort texts by distance from center
                self.tier_texts.sort(key=lambda text: abs(text.y - (self.top_threshold + self.bottom_threshold) / 2))
                for text in self.tier_texts:
                    rounded_y = 60 * round(text.y / 60)
                    while rounded_y in tiers_positions:
                        rounded_y += 60  # Adjust to avoid overlap
                    tiers_positions.add(rounded_y)
                    text.y = rounded_y
                    if text.y == 360:
                        self.tier = text.text
                
                print(self.tier)
                match self.tier:
                    case "LVL 1 - Ship Shield":
                        Globals.current_powerup = "shield-1"
                    case "LVL 1 - Damage Boost":
                        Globals.current_powerup = "damage-1"
                    case "LVL 2 - Ship Shield":
                        Globals.current_powerup = "shield-2"
                    case "LVL 2 - Damage Boost":
                        Globals.current_powerup = "damage-2"
                    case "LVL 3 - Ship Shield":
                        Globals.current_powerup = "shield-3"
                    case "LVL 3 - Damage Boost":
                        Globals.current_powerup = "damage-3"
                    case "10s - Immunity":
                        Globals.current_powerup = "immunity-1"
                    case "20s - Immunity":
                        Globals.current_powerup = "immunity-2"
                    case "30s - Immunity":
                        Globals.current_powerup = "immunity-3"

    def set_speed(self, speed):
        self.speed = speed
        self.is_gambling = True
