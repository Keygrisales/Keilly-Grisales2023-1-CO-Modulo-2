import pygame

from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2

    def __init__(self, screen):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 30)


    def update(self, game):
        pygame.display.update() #actualiza pantalla
        self.handle_events_on_menu(game)
        

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.playing = False
            elif event.type == pygame.KEYDOWN: #presionar tecla para correr
                game.run()

    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))


    def draw(self, screen, message, x = HALF_SCREEN_HEIGHT, y = HALF_SCREEN_WIDTH):
        text = self.font.render(message, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        screen.blit(text, text_rect)

