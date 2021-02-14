import AI
import AAS_IO
import pygame


class Profile:

    def __init__(self, screen, image, content, profile_name, profile_interests, profile_major,position, velocity, size1, size2, text_color, text_string, text_font, text_position):
        self.screen = screen
        self.image = image
        self.position = position
        self.content = content
        self.velocity = velocity
        self.size1 = size1
        self.size2 = size2
        self.rect = pygame.Rect(self.position[0], self.position[1], 319, 36)
        self.content_rect = pygame.Rect(self.position[0], self.position[1]-333, size1, size2)
        self.drop_down = False
        self.text_color = text_color
        self.text_string = text_string
        self.text_font = text_font
        self.text_image = self.text_font.render(self.text_string, True, self.text_color)
        self.text_position = text_position
        self.profile_name = profile_name
        self.profile_interests = profile_interests
        self.profile_major = profile_major


    def draw_profile(self):
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect)
        self.screen.blit(self.image, self.rect)

    def show_content(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.content_rect)

    def move_profile(self, velocity):
        self.velocity = velocity
        self.rect = self.rect.move(self.velocity, 0)
        self.content_rect = self.content_rect.move(self.velocity, 0)

    def draw_content(self):
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1600, 94, 319, 370))


    def display_text(self, output, pos, text_size):
        text_color = pygame.Color("Black")
        text_font = pygame.font.SysFont("Verdana", text_size)
        text_image = text_font.render(output, True, text_color)
        self.screen.blit(text_image, pos)



    def draw_text(self):
        self.screen.blit(self.text_image, self.text_position)

    def shape_shift(self, number):
        self.size2 = self.size2+number

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

    def move_down(self, velocity):
        self.velocity = velocity
        self.rect = self.rect.move(0, self.velocity)

    def move_up(self, velocity):
        self.velocity = velocity
        self.rect = self.rect.move(0, -self.velocity)

    def draw_content(self):
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1600, 149, 319, 240))

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

    def move_down(self, velocity):
        self.velocity = velocity
        self.rect = self.rect.move(0, self.velocity)

    def move_up(self, velocity):
        self.velocity = velocity
        self.rect = self.rect.move(0, -self.velocity)

    def draw_content(self):
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1600, 205, 319, 600))

    def get_rect(self):
        return self.rect

    def set_image(self, image):
        self.image = image

    def get_drop_down(self):
        return self.drop_down

    def switch_drop_down(self):
        self.drop_down = not self.drop_down


class Sidebar:

    def __init__(self, screen, image, position, size, velocity, student):
        self.position = position
        self.screen = screen
        self.image = image
        self.size = size
        self.student = student
        self.velocity = velocity
        self.color = (0, 0, 0)
        self.profile_tab = Profile(self.screen, pygame.image.load("profileWithTriangle.png"), pygame.image.load("profileSpace.png"), self.student.get_name, self.student.get_interests(), self.student.get_major(), (1925, 55), 10, 319, 0, pygame.Color("white"), self.student.get_name(),
                                   pygame.font.SysFont('DINPro', 21), (1741, 15))

        self.social_media_tab = SocialMedia(self.screen, pygame.image.load("socialMediaWithTriangle.png"), "", (1925, 111), 10)

        self.suggested_friends_tab = SuggestedFriends(self.screen, pygame.image.load("suggestedfriendstrianglenormal.png"), "", (1925, 167), 10)
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        self.drop_cases_list = []
        self.case_type = 0

    def draw_sidebar(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)
        self.social_media_tab.draw_social_media()
        self.suggested_friends_tab.draw_friends()
        self.profile_tab.show_content()
        self.profile_tab.draw_profile()

    def move_sidebar(self, velocity):
        self.velocity = velocity
        self.rect = self.rect.move(self.velocity, 0)
        self.profile_tab.move_profile(self.velocity)
        self.social_media_tab.move_social_media(self.velocity)
        self.suggested_friends_tab.move_friends(self.velocity)

    def move_down_bar(self, case):
        if case == 1:
            self.social_media_tab.move_down(20)
            self.suggested_friends_tab.move_down(20)
        elif case == 2:
            self.suggested_friends_tab.move_down(20)

    def move_up_bar(self, case):
        if case == 1:
            self.social_media_tab.move_up(20)
            self.suggested_friends_tab.move_up(20)
        elif case == 2:
            self.suggested_friends_tab.move_up(20)



    def calculate_case(self):

        self.drop_cases_list.append(self.profile_tab.get_drop_down())
        self.drop_cases_list.append(self.social_media_tab.get_drop_down())
        self.drop_cases_list.append(self.suggested_friends_tab.get_drop_down())

        for i in range(3):
            if self.drop_cases_list[i] == True:
                self.case_type = i+1

        print(self.case_type)

        self.drop_cases_list = []

    def return_pos(self):
        return self.rect[0]

    def get_profile(self):
        return self.profile_tab

    def get_social(self):
        return self.social_media_tab

    def get_friends(self):
        return self.suggested_friends_tab

    def set_case_type(self):
        self.case_type = 0

    def get_case_type(self):
        return self.case_type


class Background:

    def __init__(self, image, screen):
        self.image = image
        self.screen = screen

    def draw_background(self):
        self.screen.blit(self.image, (0, 0))


class App:

    def __init__(self, screen, size, students, ai):
        self.screen = screen
        self.size = size
        self.students = students
        self.ai = ai
        self.user = students[2101]
        self.close_app = False
        self.pos = (0, 0)
        self.sidebar_position = (1920, 52)
        self.velocity = -25

        self.background = Background(pygame.image.load("background.JPEG"), self.screen)
        self.sidebar = Sidebar(self.screen, pygame.image.load("sidebarAllGray.png"), self.sidebar_position, (291, 776), self.velocity, self.user)
        self.scroll = pygame.image.load("scroll.png")
        self.sidebar_location = "closed"
        self.sidebar_move_left = False
        self.sidebar_move_right = False

        self.move_down_1 = False
        self.moved_down = False
        self.move_up_1 = False
        self.move_down_2 = False
        self.moved_down2 = False
        self.move_up_2 = False
        self.moved_down3 = False

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

        if self.move_down_1 == True:
            if self.sidebar.get_social().get_rect()[1] < 369+111:
                 self.sidebar.move_down_bar(1)
            else:
                self.move_down_1 = False
                self.moved_down = True


        if self.move_up_1 == True:
            if self.sidebar.get_social().get_rect()[1] > 111:
                self.sidebar.move_up_bar(1)
            else:
                 self.move_up_1 = False

        if self.move_down_2 == True:
            if self.sidebar.get_friends().get_rect()[1] < 369+ 33:
                 self.sidebar.move_down_bar(2)
            else:
                self.move_down_2 = False
                self.moved_down2 = True

        if self.move_up_2 == True:
            if self.sidebar.get_friends().get_rect()[1] > 167:
                self.sidebar.move_up_bar(2)
            else:
                 self.move_up_2 = False

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

        # This part is tile click image change
        if self.sidebar.get_profile().get_rect().collidepoint(self.pos) and not self.sidebar.get_profile().get_drop_down():
            self.sidebar.get_profile().set_image(pygame.image.load("profile.png"))
            self.sidebar.get_profile().switch_drop_down()
            self.move_down_1 = True
        elif self.sidebar.get_profile().get_rect().collidepoint(self.pos) and self.sidebar.get_profile().get_drop_down():
            self.moved_down = False
            self.sidebar.get_profile().set_image(pygame.image.load("profileWithTriangle.png"))
            self.sidebar.get_profile().switch_drop_down()
            self.sidebar.set_case_type()
            self.move_up_1 = True
        if self.sidebar.get_social().get_rect().collidepoint(self.pos) and not self.sidebar.get_social().get_drop_down():
            self.sidebar.get_social().set_image(pygame.image.load("socialmedia.png"))
            self.sidebar.get_social().switch_drop_down()
            self.move_down_2 = True
        elif self.sidebar.get_social().get_rect().collidepoint(self.pos) and self.sidebar.get_social().get_drop_down():
            self.moved_down2 = False
            self.sidebar.get_social().set_image(pygame.image.load("socialMediaWithTriangle.png"))
            self.sidebar.get_social().switch_drop_down()
            self.sidebar.set_case_type()
            self.move_up_2 = True
        if self.sidebar.get_friends().get_rect().collidepoint(self.pos) and not self.sidebar.get_friends().get_drop_down():
            self.sidebar.get_friends().set_image(pygame.image.load("suggestedfriendsWithTriangle.png"))
            self.sidebar.get_friends().switch_drop_down()
            self.moved_down3 = True
        elif self.sidebar.get_friends().get_rect().collidepoint(self.pos) and self.sidebar.get_friends().get_drop_down():
            self.moved_down3 = False
            self.sidebar.get_friends().set_image(pygame.image.load("suggestedfriendstrianglenormal.png"))
            self.sidebar.get_friends().switch_drop_down()
            self.sidebar.set_case_type()

        self.sidebar.calculate_case()

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

        if self.moved_down == True:
            self.sidebar.profile_tab.draw_content()
            self.sidebar.profile_tab.display_text("Name: " + self.user.get_name(), (1605,260),17)
            self.sidebar.profile_tab.display_text("Major: " + self.user.get_major(), (1605, 290),17)

            interests = ["Outdoor Sports", "Gaming", "Coding", "Drawing/Painting", "Writing", "Reading", "Travelling",
                         "Music",
                         "Indoor Sports", "Arts and Crafts", "Action Movies", "Romance Movies", "Exercising", "Cooking",
                         "photography", "Watching Theatre"]
            users_interests = []
            for i in range(len(self.user.get_interests())):
                if self.user.get_interests()[i]:
                    users_interests.append(interests[i])

            self.sidebar.profile_tab.display_text("Interests: ", (1605,320), 17)
            for i in range(len(users_interests)):
                self.sidebar.profile_tab.display_text(users_interests[i], (1700, 30*i+320), 17)

            pfp = pygame.image.load("pfp.png")
            self.screen.blit(pfp, (1650,50))

        elif self.moved_down2 == True:
            self.sidebar.get_social().draw_content()
        elif self.moved_down3 == True:
            self.sidebar.get_friends().draw_content()

        self.screen.blit(self.scroll, (1903, 0))

        self.sidebar.profile_tab.draw_text()


        pygame.display.flip()


def main():

    students = AAS_IO.importDummyNames()
    ai = AI.AAS_AI()
    ai.load_from_file()

    pygame.init()

    size = (1920, 910)
    screen = pygame.display.set_mode(size)

    app = App(screen, size, students, ai)
    pygame.display.set_caption("Anti-Anti Social")

    app.run()




main()

