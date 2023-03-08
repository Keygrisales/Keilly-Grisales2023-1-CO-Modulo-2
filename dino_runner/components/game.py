import pygame
from pygame import mixer

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObastaclaManager
from dino_runner.components.menu import Menu
from dino_runner.components.score import Score


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
        self.score = Score() #puntaje
        self.death_count = 0 #puntaje de muerte
        self.max_score = 0 #puntaje max
        self.list_score = Score.max_score

       
      

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
        self.score.reset_score()
        self.game_speed = self.GAME_SPEED #receteamos velocidad 
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
        self.score.update_score(self)
    



    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) #fill para el color
        self.draw_background() # llamamos al metodo para que mueste la imagen
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
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
        self.score_counter = 0
        
        if self.death_count == 0:
            self.menu.draw(self.screen) 
        else:
            self.menu.update_message('Game over, press any key to restart.')
            self.menu.score_message(f' Your score: {self.list_score[-1]}', self.screen)
            self.menu.max_message(f' Max score: {max(self.list_score)}', self.screen)
            self.menu.death_message(f' Death: {self.death_count}', self.screen)
            self.menu.draw(self.screen) 
            

        self.screen.blit(ICON, (half_screen_width - 50, half_screen_height - 140)) #icono

        self.menu.update(self)

   



        


