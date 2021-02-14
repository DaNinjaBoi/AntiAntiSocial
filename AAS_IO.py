def importDummyNames():
    from User import User
    student = []
    with open("DummyNames.csv", "r") as f:
        for line in f.readlines():
            s = User(line)
            student.append(s)
    return student