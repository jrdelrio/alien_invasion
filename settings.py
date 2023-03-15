class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Inizialize the game's settings"""
        # screen settings
        self.screen_width = 1100
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        self.ship_speed = 3
        
        # bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)