import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.score import Score

from dino_runner.utils.constants import SMALL_CACTUS


class ObastaclaManager:
    def __init__(self):
        self.obstacles = []

    def generete_obstacle(self, obstacle_type):
        if obstacle_type == 0:
            cactus_type = 'SMALL'
            obstacle = Cactus(cactus_type)
        elif  obstacle_type == 1:
            cactus_type = 'LARGE'
            obstacle = Cactus(cactus_type)
        else:
            obstacle = Bird()
        return obstacle
        

    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle_type = random.randint(0,2)
            obstacle = self.generete_obstacle(obstacle_type)
            self.obstacles.append(obstacle)

        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.death_count += 1
                game.playing = False
                break

    def draw(self, screen):
        for obastacle in self.obstacles:
            obastacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []