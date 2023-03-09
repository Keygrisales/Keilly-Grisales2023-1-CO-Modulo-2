import pygame
from pygame import mixer

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObastaclaManager
from dino_runner.components.menu import Menu
from dino_runner.components.counter import Counter
from dino_runner.components.power_ups.power_up_manager import PowerUpManager



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
        self.menu = Menu (self.screen)
        self.running = False
        self.score = Counter() #puntaje
        self.death_count = Counter()  #puntaje de muerte
        self.highest_score = Counter() #puntaje max
        self.power_up_manager = PowerUpManager()

       

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()
    

    def run(self):
        self.reset_game()
        # Game loop: events - update - draw
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
        self.power_up_manager.update(self)
        self.score.update()
        self.update_game_speed()
    


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) #fill para el color
        self.draw_background() # llamamos al metodo para que mueste la imagen
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
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
        
        
        if self.death_count.count == 0:
            self.menu.draw(self.screen, "Press any key to start...") 
        else:
            self.update_highest_score()
            self.menu.draw(self.screen, 'Game over, press any key to restart.')
            self.menu.draw(self.screen, f' Your score: {self.score.count}', half_screen_width, 350, )
            self.menu.draw(self.screen, f' Max score: {self.highest_score.count}', half_screen_width, 400, )
            self.menu.draw(self.screen, f' Total death: {self.death_count.count}', half_screen_width, 450, )
    

        self.screen.blit(ICON, (half_screen_width - 50, half_screen_height - 140)) #icono

        self.menu.update(self)

    def update_game_speed(self):
        if self.score.count % 100 == 0 and self.game_speed < 500:
            self.game_speed += 5
            
    def update_highest_score(self):
        if self.score.count > self.highest_score.count:
            self.highest_score.set_count(self.score.count)

    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.score.reset()
        self.game_speed = self.GAME_SPEED
        self.player.reset()

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                self.menu.draw(self.screen, f'{self.player.type.capitalize} enabled for {time_to_show} segundos', 500, 50)
            else:
                self.has_power_up = False
                self.player.type = DEFAULT_TYPE






        


