import pygame

from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu:
    half_screen_height = SCREEN_HEIGHT // 2
    half_screen_width = SCREEN_WIDTH // 2

    def __init__(self, message, screen):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect() 
        self.text_rect.center = (self.half_screen_width, self.half_screen_height) 


    def update(self, game):
        pygame.display.update() #actualiza pantalla
        self.handle_events_on_menu(game)

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)
        

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.playing = False
            elif event.type == pygame.KEYDOWN: #presionar tecla para correr
                game.run()

    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))


    def update_message(self, message):
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.half_screen_height)

    def score_message(self, message_score, screen):
        self.text = self.font.render(message_score, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (500, 350)
        screen.blit(self.text, self.text_rect)
        

    
    def max_message(self, message_max, screen):
        self.text = self.font.render(message_max, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (500, 400)
        screen.blit(self.text, self.text_rect)
        

    def death_message(self, message_death, screen):
        self.text = self.font.render(message_death, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (500, 450)
        screen.blit(self.text, self.text_rect)



