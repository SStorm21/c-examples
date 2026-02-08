
import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((600, 400))
        pygame.display.set_caption("storm game")
        self.clock = pygame.time.Clock()
        self.img = pygame.image.load('1.png')
        self.img_pos = [160, 260]
        self.move = [False, False]

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.move[0] = True
                    if event.key == pygame.K_DOWN:
                        self.move[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.move[0] = False
                    if event.key == pygame.K_DOWN:
                        self.move[1] = False

            self.img_pos[1] += (self.move[1] - self.move[0]) * 5
            self.window.fill((0, 0, 0))  # Clear the screen
            self.window.blit(self.img, self.img_pos)
            pygame.display.update()
            self.clock.tick(60)

game = Game()
game.run()