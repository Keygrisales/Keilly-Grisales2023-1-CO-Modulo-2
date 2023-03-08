import pygame
from dino_runner.utils.constants import FONT_STYLE

class Score:
    
    max_score = []
    

    def __init__(self):
       self.score_counter = 0
        

    def update_score(self, game):
        self.score_counter += 1
        self.max_score.append(self.score_counter)
        if self.score_counter % 100 == 0 and game.game_speed < 500: #aumentamos velocidad
            game.game_speed += 5



    def draw(self, screen):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f"Score: {self.score_counter}", True, (0, 0, 0)) #imprimir puntaje
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        screen.blit(text, text_rect)

    def reset_score(self):
        self.score_counter = 0 #receteamos puntaje

   


