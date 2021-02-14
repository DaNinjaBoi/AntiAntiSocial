import antiantisocial
import User
import sklearn as sk
import pandas as pd
from sklearn import preprocessing
import statsmodels.api as sm
from sklearn.model_selection import train_test_split


def preprocess(user1, user2):
    """
    Converts Two users into an array of numbers for use by the AI
    :param user1: First user
    :param user2: Second user
    :return: Array of numbers to pass into AI
    """
    numList = []
    if user1.get_major() == user2.get_major():
        numList.append(1)
    else:
        numList.append(0)
    for i in user1.get_interests():
        if i:
            numList.append(1)
        else:
            numList.append(0)
    for i in user2.get_interests():
        if i:
            numList.append(1)
        else:
            numList.append(0)
    commonClubs = 0
    for club in user1.get_clubs():
        if club in user2.get_clubs():
            commonClubs += 1
    numList.append(commonClubs)

    commonSocial = 0
    for i in range(len(user1.get_media_account())):
        if user1.get_media_account()[i] and user2.get_media_account()[i]:
            commonSocial += 1
    numList.append(commonSocial)

    commonClasses = 0
    for classID in user1.get_classes():
        if classID in user2.get_classes():
            commonClasses += 1
    numList.append(commonClasses)

    return numList


def create_training_csv():
    from AAS_IO import importDummyNames
    users = importDummyNames()
    with open("manual_training.csv", 'r') as f:
        with open("training.csv", "w") as g:
            with open("training_targets.csv", "w") as h:
                print("Opened")
                for line in f.readlines():
                    data = line.split(",")
                    towrite = preprocess(users[int(data[0])], users[int(data[1])])
                    for index in range(len(towrite)):
                        g.write(str(towrite[index]))
                        if index < len(towrite)-1:
                            g.write(",")
                    g.write("\n")
                    h.write(data[2])


class AAS_AI():
    def __init__(self):
        pass

    def load_from_file_and_train(self):
        data = pd.read_csv('training.csv', header=None)
        x_train, x_test, y_train, y_test = train_test_split()
        logit_model = sm.Logit()

    def save_to_file(self):
        pass

    def initial_setup(self):
        pass

    def classify(self):
        pass

    def train(self):
        pass

