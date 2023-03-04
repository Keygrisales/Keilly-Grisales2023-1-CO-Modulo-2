import random

from dino_runner.components.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS 

class Cactus(Obstacle):

    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type) #llamamos al constructor de la clase padre (Obstacle)
        self.rect.y = 325
        self.rect.x = 80
        self.image = SMALL_CACTUS


