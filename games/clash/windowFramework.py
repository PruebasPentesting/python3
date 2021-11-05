#manage all window from the game
import pygame

class window:
    def __init__(self):
        self.width, self.height = 1200, 800
        self.window = pygame.display.set_mode((self.width, self.height))
        self.color = (255, 255, 255)

    def endFrame(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True


    def fillWindow(self):
        self.window.fill(self.color)
        

    def updateFrame(self):
        pygame.display.flip()

