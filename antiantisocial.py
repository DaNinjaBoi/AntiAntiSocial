import generateDummyNames
import AAS_IO
import AI



if __name__ == "__main__":
    # generateDummyNames.generate_dummy_names()
    students = AAS_IO.importDummyNames()
    print(AI.preprocess(students[0],students[1]))


