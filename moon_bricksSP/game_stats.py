class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings

        # Game stats
        self.game_active = False
        self.game_end = False
        self.p1_score = 0
        self.p2_score = 0
        self.max_score = 11
        
