def importDummyNames():
    from User import User
    student = []
    with open("DummyNames.csv", "r") as f:
        for line in f.readlines():
            s = User(line)
            student.append(s)
    return student

def interpret_csv_line(line):
    output = list(map(int,(line.split(","))))
    if line[0] > line[1]:
        output[0], output[1] = output[1], output[0]
    return output

def sort_csv_lines_key(line):
    return line[0]+(line[1]/5000)


def merge_csv():
    lines = []
    with open("manual_training_alec.csv","r") as f:
        for line in f.readlines():
            lines.append(interpret_csv_line(line))
    with open("manual_training_adam.csv","r") as f:
        for line in f.readlines():
            lines.append(interpret_csv_line(line))
    with open("manual_training_Karanpal.csv","r") as f:
        for line in f.readlines():
            lines.append(interpret_csv_line(line))
    with open("manual_training_oscar.csv","r") as f:
        for line in f.readlines():
            lines.append(interpret_csv_line(line))
    with open("manual_training_vansh.csv","r") as f:
        for line in f.readlines():
            lines.append(interpret_csv_line(line))

    lines.sort()

    traverse = 0
    while traverse < len(lines)-1:
        if lines[traverse][0] == lines[traverse+1][0] and lines[traverse][1] == lines[traverse+1][1]:
            lines.pop(traverse)
            traverse -= 1
        traverse += 1

    with open("manual_training.csv", "w") as f:
        for line in lines:
            f.write(str(line[0])+","+str(line[1])+","+str(line[2])+"\n")

    total = 0
    for line in lines:
        total += line[2]
    print(total)


