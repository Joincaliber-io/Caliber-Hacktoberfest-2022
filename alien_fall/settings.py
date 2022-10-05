class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1080
        self.screen_height = 680
        self.bg_color = (150,150,245)

        #ship settings
        self.ship_speed_factor = 0.3 # real 1.3

        # Bullet settings
        self.bullet_speed_factor = 2.6 # real 1.6 
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        #Alien settings
        self.alien_speed_factor = 0.2 # real 1
        self.alien_default_speed = 0.2 # default 
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.aliens_defeted = False
        
        #Game State settings
        self.paused = False

