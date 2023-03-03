import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING 

class Dinosaur(Sprite):

    def __init__(self):
        self.image = RUNNING [0]
        self.dino_rect = self.image.get_rect() # pposiciones imag
        self.dino_rect.x = 80
        self.dino_rect.y = 310

    def update(self):
        pass

    def draw(self, screen): #dibujar en pantalla
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        
