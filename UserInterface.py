
import pygame

class dropdown:

    def __init__(self, dimensions, color, position):
        self.dimensions = dimensions
        self.color = color
        self.position = position


class background:

    def __init__(self, image):
        self.image = image


class app:

    def __init__(self, screen, size):
        self.screen = screen
        self.size = size
        self.close_app = False

        self.app_clock = pygame.time.Clock()
        self.FPS = 60

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close_app = True

    def run(self):

        while not self.close_app:

            self.handle_events()

            self.game_clock.tick(self.FPS)

def main():
    pygame.init()





"""
1. initial click sidebar appears

2. when sidebar appears all of the dropdowns should be hidden

3. when clicked onto the dropdowns, they should be opened up and animated the dropdown.

4. now we need to make sure that clicking a specific dropdown will hide all of the other ones

"""