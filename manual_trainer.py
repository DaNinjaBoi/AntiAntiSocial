import User
from AAS_IO import importDummyNames

students = importDummyNames()

interests = ["Outdoor Sports", "Gaming", "Coding", "Drawing/Painting", "Writing", "Reading", "Travelling", "Music",
             "Indoor Sports", "Arts and Crafts", "Action Movies", "Romance Movies", "Exercising", "Cooking",
             "photography", "Watching Theatre"]


def manual_train():
    import random

    print()
    student1 = random.randrange(0, len(students))
    student2 = random.randrange(0, len(students))
    # students[student1].print_user(" ")
    # students[student2].print_user(" ")
    display_student(student1, student2)


def display_student(student1, student2):
    print("Person 1:")
    print("\tMajor: " + students[student1].get_major())
    print("\tInterests: " + str(students[student1].get_interests()))
    print("\tClasses " + str(students[student1].get_classes()))
    print("\tClubs: " + str(students[student1].get_clubs()))
    print("\tMedia Accounts: " + str(students[student1].get_media_account()))
    print()
    print("Person 2:")
    print("\tMajor: " + students[student2].get_major())
    print("\tInterests: " + str(students[student2].get_interests()))
    print("\tClasses " + str(students[student2].get_classes()))
    print("\tClubs: " + str(students[student2].get_clubs()))
    print("\tMedia Accounts: " + str(students[student2].get_media_account()))

    find_interest(student1)


def find_interest(student):
    str_interests = []
    for i in range(len(students[student].get_interests())):
        print(students[student].get_interests()[i])
        if students[student].get_interests()[i]:
            print(interests[i])







manual_train()

# add telling training method y or n on two specific people
