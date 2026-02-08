import pygame
import sys
class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((600, 400))
        pygame.display.set_caption("storm game")
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.exit()
                    sys.exit()
    
            pygame.display.update()
            self.clock.tick(60)

Game().run()