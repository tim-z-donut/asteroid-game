from constants import *
import pygame

# SCORE_INCREMENT


class HUD(pygame.sprite.Sprite):
    def __init__(self):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        
        self.color = 'green'
        self.background_color = None
        self.font_size = 50
        self.init_font()
        

    def init_font(self):
        default = pygame.font.get_default_font()
        location = pygame.font.match_font(default)
        self.font = pygame.font.Font(location, self.font_size)

    def update(self, dt):
        # sub-classes must override
        pass

    def draw(self):
        # sub-classes must override
        pass


class score(HUD):
    def __init__(self):
        super().__init__()
        self.score = 0

    def text(self):
        return f"Score: {self.score}" 

    def add_points(self):
        self.score+=SCORE_INCREMENT

    def draw(self):
        self.render = self.font.render(self.text(), 1, self.color, self.background_color)

class lives(HUD):
    def __init__(self):
        super().__init__()
        pass