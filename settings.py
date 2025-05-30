class Settings():

    def __init__(self):
        """ Initialize the game's settings """
        # Screens settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.title = "Alien Invasion"
        
        # Ship settings
        self.ship_speed_factor = 2

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
