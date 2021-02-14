
import pygame

class Dropdown:

    def __init__(self, dimensions, color, position):
        self.dimensions = dimensions
        self.color = color
        self.position = position


class Background:

    def __init__(self, image, screen):
        self.image = image
        self.screen = screen

    def draw_background(self):
        self.screen.blit(self.image, (0, 0))


class App:

    def __init__(self, screen, size):
        self.screen = screen
        self.size = size
        self.close_app = False

        self.background = Background(pygame.image.load("background.JPEG"), self.screen)

        self.app_clock = pygame.time.Clock()
        self.FPS = 60

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close_app = True

    def run(self):

        while not self.close_app:

            self.handle_events()

            self.app_clock.tick(self.FPS)

            self.draw()

    def draw(self):

        self.screen.fill((255, 255, 255))

        self.background.draw_background()

        pygame.display.flip()


def main():

    pygame.init()

    size = (1920, 910)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Anti-Anti Social")

    app = App(screen, size)

    app.run()




main()





"""
1. initial click sidebar appears

2. when sidebar appears all of the dropdowns should be hidden

3. when clicked onto the dropdowns, they should be opened up and animated the dropdown.

4. now we need to make sure that clicking a specific dropdown will hide all of the other ones

"""