
from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE


class Hammer(PowerUp):

    def __init__(self):
        #self.rotate = 0
        #self.rotate += 1
        
        #Hammer_throw = pygame.transform.rotate(HAMMER, self.rotate)
        #self.rect = Hammer_throw.get_rect()
        super().__init__(HAMMER, HAMMER_TYPE)
        #self.rotate += 1
    
            #self.rect.center = HAMMER.center

    #def draw(self, screen): 
        #HAMMERr = pygame.transform.rotate(HAMMER, 90)
       
        #self.rect = HAMMERr.get_rect()
        #hamm = pygame.transform.rotate(HAMMER, self.rotate)
        #self.rect = hamm.get_rect()
        #screen.blit(HAMMERr, (180, 100))
        #pygame.display.update()

    


        
