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

    
    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.draw()
        pygame.quit()

    def draw(self, screen): #dibujar en pantalla
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        """
        if  RUNNING [0] %2 == 0 :
            self.image.draw(self.screen)
            pygame.display.update()
        else:
            self.image = RUNNING [1]
            self.image.draw(self.screen)
            pygame.display.update()
            self.screen.blit(self.image, (RUNNING[1] + self.x_pos_bg, self.y_pos_bg))
            self.dino_rect.x = 0
            self.dino_rect.x.dino_rect.x -= self.game_speed
        
        """

