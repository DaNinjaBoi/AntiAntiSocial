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



