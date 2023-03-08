import pygame
from pygame import mixer

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObastaclaManager
from dino_runner.components.menu import Menu


class Game:

    GAME_SPEED = 20

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()  #tiempo para el puntaje
        self.playing = False
        self.game_speed = self.GAME_SPEED #velocidad del juego
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.music = False
        self.obstacle_manager = ObastaclaManager()
        self.menu = Menu ('press any key to start...', self.screen)
        self.running = False
        self.score = 0 #puntaje
        self.death_count = 0 #puntaje de muerte

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()
    

    def run(self):
        # Game loop: events - update - draw
        self.obstacle_manager.reset_obstacles()
        self.game_speed = self.GAME_SPEED #receteamos velocidad
        self.score = 0 #receteamos puntaje
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.soundd()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
   

    def soundd(self):
        if not self.music:
            sound = pygame.mixer.Sound('fonddino.wav')
            sound.play()
            
            self.music = True
        

    def update(self):
        user_input = pygame.key.get_pressed() #nos dice que tecla esta precionando el usuario
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()



    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) #fill para el color
        self.draw_background() # llamamos al metodo para que mueste la imagen
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
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

    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2

        if self.death_count == 0:
            self.menu.draw(self.screen) #imprimir cuando muerte = 0
        else:
            self.menu.update_message('new message')
            self.menu.draw(self.screen)

        self.screen.blit(ICON, (half_screen_width - 50, half_screen_height - 140))

        self.menu.update(self)

    def update_score(self):
        self.score += 1 # actualiza puntaje

        if self.score % 100 == 0 and self.game_speed < 500: #aumentamos velocidad
            self.game_speed += 5

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f"Score: {self.score}", True, (0, 0, 0)) #imprimir puntaje
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)


