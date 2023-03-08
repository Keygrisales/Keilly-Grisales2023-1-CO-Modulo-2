import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD



class Bird(Obstacle):

    BIRD_HEIGHTS = [320, 250, 230]

    def __init__(self):
        self.type = 0
        super().__init__(BIRD, self.type) #llamamos al constructor de la clase padre (Obstacle)
        self.rect.y = self.BIRD_HEIGHTS[random.randint(0,2)]
        self.flight = 0



    def draw(self, screen):
        if self.flight >= 9:
            self.flight = 0
        screen.blit(BIRD[self.flight//5], self.rect)
        self.flight += 1

 
   


    
