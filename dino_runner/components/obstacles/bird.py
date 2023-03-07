import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):

    def __init__(self, image,):
        self.type = 0

        super().__init__(image, self.type) #llamamos al constructor de la clase padre (Obstacle)
        #self.rect.y = 320
        self.flight = 0



    def draw(self, screen):
        if self.flight >= 10:
            self.flight = 0
        screen.blit(self.image[self.flight//5], self.rect)
        self.flight += 1

 
   


    