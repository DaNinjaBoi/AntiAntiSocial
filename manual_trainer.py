import User
from AAS_IO import importDummyNames

students = importDummyNames()

interests = ["Outdoor Sports", "Gaming", "Coding", "Drawing/Painting", "Writing", "Reading", "Travelling", "Music",
             "Indoor Sports", "Arts and Crafts", "Action Movies", "Romance Movies", "Exercising", "Cooking",
             "photography", "Watching Theatre"]


def manual_train():
    import random
    with open("manual_training_Karanpal.csv", "a") as f:
        for i in range(5000):
            student1idx = random.randrange(0, len(students))
            student2idx = random.randrange(0, len(students))
            while student1idx == student2idx:
                student2idx = random.randrange(0, len(students))
            # students[student1idx].print_user(" ")
            # students[student2idx].print_user(" ")
            display_students(students[student1idx],students[student2idx])
            answer = ""
            while answer != "y" and answer != "n" and answer != 'e':
                answer = input("Possible friends? y/n  ")
            if answer == "y":
                f.write(str(student1idx)+","+str(student2idx)+",1\n")
            elif answer == "n":
                f.write(str(student1idx)+","+str(student2idx)+",0\n")
            elif answer == 'e':
                break
            print("\n")


def display_student(student):
    print(student.get_name().split(" ")[0].ljust(10), end="")
    print("Major: " + student.get_major().ljust(18), end="")
    print("| Interests: ",end="")
    for i in range(len(student.get_interests())):
        if student.get_interests()[i]:
            print(interests[i],end="  ")
    print()


def display_students(student1, student2):
    display_student(student1)
    display_student(student2)
    common_clubs = 0
    for club in student1.get_clubs():
        if club in student2.get_clubs():
            common_clubs += 1
    print("Common Clubs: " + str(common_clubs))
    common_social = 0
    for i in range(len(student1.get_media_account())):
        if student2.get_media_account()[i] and student1.get_media_account()[i]:
            common_social += 1

    print("Common Social Media: "+ str(common_social))
    common_classes = 0
    for classID in student1.get_classes():
        if classID in student2.get_classes():
            common_classes += 1
    print("Common Classes:  "+ str(common_classes))







manual_train()

# add telling training method y or n on two specific people
