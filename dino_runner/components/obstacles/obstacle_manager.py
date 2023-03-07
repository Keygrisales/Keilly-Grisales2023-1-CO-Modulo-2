import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObastaclaManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            type = random.randint(0,2)
            
            if type == 0:
                cactus = Cactus(SMALL_CACTUS)
                cactus.rect.y = 325
                self.obstacles.append(cactus)
            elif type == 1:
                cactus = Cactus(LARGE_CACTUS)
                cactus.rect.y = 300
                self.obstacles.append(cactus)
            
            else:
                bird = Bird(BIRD)
                fly = random.randint(0,2)
                if fly == 0:
                    bird.rect.y = 320
                elif fly == 1:
                    bird.rect.y = 250
                elif fly == 2:
                    bird.rect.y = 230
                self.obstacles.append(bird)
        
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break

    def draw(self, screen):
        for obastacle in self.obstacles:
            obastacle.draw(screen)