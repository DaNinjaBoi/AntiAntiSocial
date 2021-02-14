
import pygame


class Profile:

    def __init__(self, screen, image, content, position, velocity):
        self.screen = screen
        self.image = image
        self.position = position
        self.content = content
        self.velocity = velocity
        self.rect = pygame.Rect(self.position[0], self.position[1], 319, 36)
        self.drop_down = False

    def draw_profile(self):
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect)
        self.screen.blit(self.image, self.rect)

    def move_profile(self, velocity):
        self.velocity = velocity
        self.rect = self.rect.move(self.velocity, 0)

    def get_rect(self):
        return self.rect

    def set_image(self, image):
        self.image = image

    def get_drop_down(self):
        return self.drop_down

    def switch_drop_down(self):
        self.drop_down = not self.drop_down


class SocialMedia:

    def __init__(self, screen, image, content, position, velocity):
        self.screen = screen
        self.image = image
        self.content = content
        self.position = position
        self.velocity = velocity
        self.rect = pygame.Rect(self.position[0], self.position[1], 319, 36)
        self.drop_down = False

    def draw_social_media(self):
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect)
        self.screen.blit(self.image, self.rect)

    def move_social_media(self, velocity):
        self.velocity = velocity
        self.rect = self.rect.move(self.velocity, 0)

    def get_rect(self):
        return self.rect

    def set_image(self, image):
        self.image = image

    def get_drop_down(self):
        return self.drop_down

    def switch_drop_down(self):
        self.drop_down = not self.drop_down




class SuggestedFriends:

    def __init__(self, screen, image, content, position, velocity):
        self.screen = screen
        self.image = image
        self.content = content
        self.position = position
        self.velocity = velocity
        self.rect = pygame.Rect(self.position[0], self.position[1], 319, 36)
        self.drop_down = False

    def draw_friends(self):
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect)
        self.screen.blit(self.image, self.rect)

    def move_friends(self, velocity):
        self.velocity = velocity
        self.rect = self.rect.move(self.velocity, 0)

    def get_rect(self):
        return self.rect

    def set_image(self, image):
        self.image = image

    def get_drop_down(self):
        return self.drop_down

    def switch_drop_down(self):
        self.drop_down = not self.drop_down


class Sidebar:

    def __init__(self, screen, image, position, size, velocity):
        self.position = position
        self.screen = screen
        self.image = image
        self.size = size
        self.velocity = velocity
        self.color = (0, 0, 0)
        self.profile_tab = Profile(self.screen, pygame.image.load("profileWithTriangle.png"), "", (1925, 55), 10)
        self.social_media_tab = SocialMedia(self.screen, pygame.image.load("socialMediaWithTriangle.png"), "", (1925, 111), 10)
        self.suggested_friends_tab = SuggestedFriends(self.screen, pygame.image.load("suggestedfriendsWithTriangle.png"), "", (1925, 167), 10)
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])

    def draw_sidebar(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)
        self.profile_tab.draw_profile()
        self.social_media_tab.draw_social_media()
        self.suggested_friends_tab.draw_friends()

    def move_sidebar(self, velocity):
        self.velocity = velocity
        self.rect = self.rect.move(self.velocity, 0)
        self.profile_tab.move_profile(self.velocity)
        self.social_media_tab.move_social_media(self.velocity)
        self.suggested_friends_tab.move_friends(self.velocity)


    def return_pos(self):
        return self.rect[0]

    def get_profile(self):
        return self.profile_tab

    def get_social(self):
        return self.social_media_tab

    def get_friends(self):
        return self.suggested_friends_tab


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
        self.sidebar = Sidebar(self.screen, pygame.image.load("sidebarAllGray.png"), self.sidebar_position, (291, 776), self.velocity)
        self.scroll = pygame.image.load("scroll.png")
        self.sidebar_location = "closed"
        self.sidebar_move_left = False
        self.sidebar_move_right = False

        self.app_clock = pygame.time.Clock()
        self.FPS = 60

    def update(self):
        if self.sidebar_move_left:
            if self.sidebar.return_pos() > 1600:
                self.sidebar.move_sidebar(self.velocity)
            else:
                self.sidebar_move_left = False
                self.sidebar_location = "open"
        if self.sidebar_move_right:
            if self.sidebar.return_pos() < 1920:
                self.sidebar.move_sidebar(-self.velocity)
            else:
                self.sidebar_move_right = False
                self.sidebar_location = "closed"

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close_app = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_up()

    def mouse_up(self):

        self.pos = pygame.mouse.get_pos()

        if self.pos[0] > 1710 and self.pos[0] < 1730 and self.pos[1] < 35 and self.pos[1] > 5:
            if self.sidebar_location == "closed":
                self.sidebar_move_left = True
            if self.sidebar_location == "open":
                self.sidebar_move_right = True

        if self.sidebar.get_profile().get_rect().collidepoint(self.pos) and not self.sidebar.get_profile().get_drop_down():
            self.sidebar.get_profile().set_image(pygame.image.load("profile.png"))
            self.sidebar.get_profile().switch_drop_down()
        elif self.sidebar.get_profile().get_rect().collidepoint(self.pos) and self.sidebar.get_profile().get_drop_down():
            self.sidebar.get_profile().set_image(pygame.image.load("profileWithTriangle.png"))
            self.sidebar.get_profile().switch_drop_down()
        if self.sidebar.get_social().get_rect().collidepoint(self.pos) and not self.sidebar.get_social().get_drop_down():
            self.sidebar.get_social().set_image(pygame.image.load("socialmedia.png"))
            self.sidebar.get_social().switch_drop_down()
        elif self.sidebar.get_social().get_rect().collidepoint(self.pos) and self.sidebar.get_social().get_drop_down():
            self.sidebar.get_social().set_image(pygame.image.load("socialMediaWithTriangle.png"))
            self.sidebar.get_social().switch_drop_down()
        if self.sidebar.get_friends().get_rect().collidepoint(self.pos) and not self.sidebar.get_friends().get_drop_down():
            self.sidebar.get_friends().set_image(pygame.image.load("suggestedfriends.png"))
            self.sidebar.get_friends().switch_drop_down()
        elif self.sidebar.get_friends().get_rect().collidepoint(self.pos) and self.sidebar.get_friends().get_drop_down():
            self.sidebar.get_friends().set_image(pygame.image.load("suggestedfriendsWithTriangle.png"))
            self.sidebar.get_friends().switch_drop_down()


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

