
import pygame

class Dropdown:

    def __init__(self, dimensions, color, position):
        self.dimensions = dimensions
        self.color = color
        self.position = position


class Background:

    def __init__(self, image):
        self.image = image




class App:

    def __init__(self, screen, size):
        self.screen = screen
        self.size = size
        self.close_app = False


        self.background = pygame.image.load("")

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

    def draw(self):



        pygame.display.flip()

def main():

    pygame.init()

    size = (1920, 1080)
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