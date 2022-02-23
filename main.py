import pygame, sys



class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_caption("3d engine")

    def update(self):
        pygame.display.update()
        self.screen.fill((0, 0, 0))
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()

    def run(self):
        while True:
            self.update()
            self.events()


if __name__ == "__main__":
    app = App()
    app.run()