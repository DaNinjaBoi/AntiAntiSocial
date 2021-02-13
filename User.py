class User:

    def __init__(self, ID, name, passcode, major, interests, club, media_account, classes):
        self.id = ID
        self.name = name
        self.passcode = passcode
        self.major = major
        self.interests = interests
        self.club = club
        self.media = media_account
        self.classes = classes

    def __init__(self):
        pass

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_major(self):
        return self.major

    def get_interests(self):
        return self.interests

    def get_club(self):
        return self.club

    def get_media_account(self):
        return self.media

    def get_classes(self):
        return self.classes

    def find_mutual_friends(self):
        pass

    def print_user(self, type = "normal"):
        if type == "normal":
            print(self.name + "")
        else:
            print(self.id + "")
            print(self.name + "")
            print(self.major + "")
            print(self.interests + "")
            print(self.club + "")
            print(self.media + "")
            print(self.classes + "")












