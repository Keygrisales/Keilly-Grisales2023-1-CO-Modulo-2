import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

class Dinosaur(Sprite):

    X_POS = 80
    Y_POS = 310
    JUMP_SPEED = 8.5
    DUCK_SPEED = -8.5

    def __init__(self):
        self.image = RUNNING [0]
        self.dino_rect = self.image.get_rect() # pposiciones imag
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0 # contador
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_speed = self.JUMP_SPEED
        self.duck_speed = self.DUCK_SPEED
        sound_jump = False

   

    def update(self, user_input):
        if self.dino_run:
            self.run()

        elif self.dino_jump:
            self.jump()
        
        if self.dino_duck:
            self.duck()

        
        if user_input[pygame.K_UP] and not self.dino_jump:
            sound_jump = pygame.mixer.Sound('jump.wav')
            sound_jump.play()
            sound_jump = True
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        if self.step_index >= 10: #para que siga cambiando de imag el dino 
            self.step_index = 0

        if user_input[pygame.K_DOWN] and not self.dino_duck:
            self.dino_duck = True
            self.dino_jump = False
            self.dino_run = False
        if self.step_index >= 10: #para que siga cambiando de imag el dino 
            self.step_index = 0

        elif not self.dino_duck and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False


       
    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.Y_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMPING
        self.dino_rect.y -= self.jump_speed * 4
        self.jump_speed -= 0.8

        if self.jump_speed < -self.JUMP_SPEED: #controlar que no salte al infinito
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_speed = self.JUMP_SPEED

    def duck(self):
        self.image = DUCKING
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.y = 340
        self.step_index += 1

        if self.DUCK_SPEED < -self.DUCK_SPEED: #controla que no quede agachado por siempre
            self.dino_rect.x = self.Y_POS #310
            self.dino_duck = False


    def draw(self, screen): #dibujar en pantalla
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

        
        

