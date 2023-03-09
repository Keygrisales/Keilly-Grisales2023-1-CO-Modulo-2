import random
from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH

class Cloud:

    def __init__(self):
        self.image = CLOUD
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(180, 250)
        self.width = self.image.get_width()

    def update(self, game_speed):
        self.rect.x -= game_speed
        if self.rect.x < -self.width:
            self.rect.x = SCREEN_WIDTH
            

    def draw(self, screen):
        screen.blit(CLOUD, (self.rect.x, self.rect.y))
        
        

