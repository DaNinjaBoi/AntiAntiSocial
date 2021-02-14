def isTrue(s):
    return s == 'True'

class User:

    def __init__(self, csv):
        splitline = csv.split("%")
        self.id = splitline[1]
        self.name = splitline[0]
        self.passcode = splitline[2]
        self.major = splitline[3]
        self.interests = list(map(isTrue, splitline[4][1:-1].split(", ")))
        if len(splitline[6]) > 2:
            self.clubs = splitline[6][1:-1].split(", ")
        else:
            self.clubs = []
        self.media = splitline[5][2:-2].split("', '")
        self.classes = list(map(int, splitline[7][1:-2].split(', ')))


    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_major(self):
        return self.major

    def get_interests(self):
        return self.interests

    def get_clubs(self):
        return self.clubs

    def get_media_account(self):
        return self.media

    def get_classes(self):
        return self.classes

    def find_mutual_friends(self):
        pass

    def get_string_interests(self):
        interests = ["Outdoor Sports", "Gaming", "Coding", "Drawing/Painting", "Writing", "Reading", "Travelling",
                     "Music",
                     "Indoor Sports", "Arts and Crafts", "Action Movies", "Romance Movies", "Exercising", "Cooking",
                     "photography", "Watching Theatre"]
        out = []
        for i in range(len(self.interests)):
            if(self.interests[i]):
                out.append(interests[i])
        return ','.join(out)

    def print_user(self, type = "normal"):
        if type == "normal":
            print(self.name)
        else:
            print(self.id, end=", ")
            print(self.name, end=", ")
            print(self.major, end=", ")
            interests = ["Outdoor Sports", "Gaming", "Coding", "Drawing/Painting", "Writing", "Reading", "Travelling",
                         "Music",
                         "Indoor Sports", "Arts and Crafts", "Action Movies", "Romance Movies", "Exercising", "Cooking",
                         "photography", "Watching Theatre"]
            for i in range(len(self.interests)):
                if self.interests[i]:
                    print(interests[i], end=" | ")
            print(self.clubs, end=", ")
            print(self.media, end=", ")
            print(self.classes)












