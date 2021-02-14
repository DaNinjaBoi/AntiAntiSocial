
import pygame

class Sidebar:

    def __init__(self, screen, image, position, size, velocity):
        self.position = position
        self.screen = screen
        self.image = image
        self.size = size
        self.velocity = velocity
        self.color = (0, 0, 0)
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])

    def draw_sidebar(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)

    def move_sidebar(self, velocity):
        self.velocity = velocity
        if self.rect[0] > 1600:
            self.rect = self.rect.move(self.velocity, 0)

    def return_pos(self):
        return self.rect[0]



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
        self.pos = (0, 0)
        self.sidebar_position = (1920, 52)
        self.velocity = -25

        self.background = Background(pygame.image.load("background.JPEG"), self.screen)
        self.sidebar = Sidebar(self.screen, pygame.image.load("sidebar.PNG"), self.sidebar_position, (291, 776), self.velocity)
        self.scroll = pygame.image.load("scroll.png")
        self.sidebar_location = "right"
        self.sidebar_move_left = False
        self.sidebar_move_right = True

        self.app_clock = pygame.time.Clock()
        self.FPS = 60

    def update(self):
        if self.sidebar_moved_left:
            if self.sidebar.return_pos() > 1640:
                self.sidebar.move_sidebar(self.velocity)
            else:
                self.sidebar_moved_left = True
                self.sidebar_moved_right = False
        if self.sidebar_moved_right:
            if self.sidebar.return_pos() < 1920:
                self.sidebar.move_sidebar(-self.velocity)
            else:
                self.sidebar_moved_right = True
                self.sidebar_moved_left = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close_app = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_up()

    def mouse_up(self):

        self.pos = pygame.mouse.get_pos()

        if self.pos[0] > 1710 and self.pos[0] < 1730 and self.pos[1] < 35 and self.pos[1] > 5:
            if self.sidebar_location == "right":
                self.sidebar_move_left = True
            if self.sidebar_location == "left":
                self.sidebar_move_right = True


    def run(self):

        while not self.close_app:

            self.handle_events()

            self.app_clock.tick(self.FPS)

            self.draw()

    def draw(self):

        self.screen.fill((255, 255, 255))

        self.background.draw_background()

        self.sidebar.draw_sidebar()

        self.update()

        self.screen.blit(self.scroll, (1903, 0))

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