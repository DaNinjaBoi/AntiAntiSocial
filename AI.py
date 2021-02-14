import antiantisocial
import User
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


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
        self.logreg = []

    def create_logreg_and_train(self):
        data = pd.read_csv('training.csv', header=None)
        targets = pd.read_csv('training_targets.csv', header=None)
        targets = targets.values.ravel()
        print(targets.shape)
        x_train, x_test, y_train, y_test = train_test_split(data, targets, test_size=0.25, )
        self.logreg = LogisticRegression()
        self.logreg.fit(x_train,y_train)
        y_pred = self.logreg.predict(x_test)
        print('Accuracy: {:.5f}'.format(self.logreg.score(x_test, y_test)))
        from sklearn.metrics import confusion_matrix
        confusion_matrix = confusion_matrix(y_test, y_pred)
        print(confusion_matrix)
        from sklearn.metrics import roc_auc_score
        score = roc_auc_score(y_test, self.logreg.predict(x_test))
        print("ROC score area is {:.5f}".format(score))
        print("Would you like to save? (y/n): ")
        if input() == 'y':
            self.save_to_file()

    def save_to_file(self):
        with open('saved_model', 'wb') as f:
            pickle.dump(self.logreg, f)

    def load_from_file(self):
        with open('saved_model', 'rb') as f:
            self.logreg = pickle.load(f)

    def classify(self, user1, user2):
        return self.logreg.decision_function(np.array(preprocess(user1, user2)).reshape(1,-1))

    def find_best_matches(self,userList, userIndex, k):
        '''
        Gives k best predictions from userList for the user at userIndex
        :param userList: list of user objects
        :param userIndex: index of target user in userList
        :return: list of indices of k top likely-to-be-friends users
        '''

        k_best_matches = []
        for i in range(len(userList)):
            if userList[i] != userList[userIndex]:
                k_best_matches.append([self.classify(userList[userIndex], userList[i]), i])
        k_best_matches.sort(key=lambda arr: arr[0], reverse=True)
        return k_best_matches[:k]



    def train(self):
        pass

