import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()  #tiempo para el puntaje
        self.playing = False
        self.game_speed = 20 #velocidad del juego
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        pass

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) #fill para el color
        self.draw_background() # llamamos al metodo para que mueste la imagen
        self.player.draw(self.screen)
        pygame.display.update() # update o flip actualiza (permite que se muestre el dibj en pantalla)
        #pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg)) #blit dibujar y en que posicion 
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg)) # colocar las dos imagenes de seguido
        if self.x_pos_bg <= -image_width:  #mover imagen
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
