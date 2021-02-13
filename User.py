from typing import Any


class User:
    def __init__(self, ID, name, passcode, major, interests, club, media_account, classes):
        self.id = ID
        self.name = name
        self.passcode = passcode
        self.major = major
        self.interests = interests

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










