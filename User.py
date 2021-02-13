class User:

    def __init__(self, csv):
        splitline = csv.split(",")
        self.id = splitline[1]
        self.name = splitline[0]
        self.passcode = splitline[2]
        self.major = splitline[3]
        self.interests = splitline[4]
        self.club = splitline[6]
        self.media = splitline[5]
        self.classes = splitline[7]


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












