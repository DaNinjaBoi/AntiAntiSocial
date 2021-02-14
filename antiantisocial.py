import generateDummyNames
import AAS_IO
import AI


if __name__ == "__main__":

    students = AAS_IO.importDummyNames()
    # print(AI.preprocess(students[22],students[5]))
    ai = AI.AAS_AI()
    ai.load_from_file()
    print(ai.classify(students[120],students[1848]))
    print(ai.find_best_matches(students, 120, 5))
    students[120].print_user(" ")
    students[126211-123000].print_user(" ")




