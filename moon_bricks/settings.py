class Settings():
    """A class to store all settings for Bricks."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen Settings
        self.screen_width = 970
        self.screen_height = 620
        self.bg_color = (0,0,0)

        # Player Settings
        self.player_speed_factor = 0.8
        
        # Ball settings
        self.ball_speed_factor = 0.1


    def reset_ball_speed(self):
        self.ball_speed_factor = 0.1
