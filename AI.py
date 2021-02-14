import antiantisocial
import User

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



