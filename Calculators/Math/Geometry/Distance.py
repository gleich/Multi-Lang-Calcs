# Instructions:
# Just run the file and answer the quesitons!
#--------------------------------------------------------------------


def spacer():
    """
    Will clear the output
    """
    for i in range(40):
        print("\n")


def ask_question(question, cast):
    """
    Will ask the user a question
    :param question: question that will be asked
        :type: str
    :param cast: what the question will be casted as
        :type: str
    :return: the casted input from the user
        :type: str
    """
    if "float" in cast.lower():
        try:
            orig_input = float(input(question))
            return orig_input
            spacer()
        except ValueError:
            print("Error!\n Re run the program and make sure that you are putting in valid inputs.")
            spacer()
    elif "int" in cast.lower():
        try:
            orig_input = int(input(question))
            return orig_input
            spacer()
        except ValueError:
            print("Error!\n Re run the program and make sure that you are putting in valid inputs.")
            spacer()
    elif "bool" in cast.lower():
        try:
            orig_input = bool(input(question))
            return orig_input
            spacer()
        except ValueError:
            print("Error!\n Re run the program and make sure that you are putting in valid inputs.")
            spacer()
    elif "list" in cast.lower():
        try:
            orig_input = list(input(question))
            return orig_input
            spacer()
        except ValueError:
            print("Error!\n Re-run the program and make sure that you are putting in valid inputs.")
            spacer()
    else:
        return input(question)
        spacer()


def distance():
    """
    Will find the distance between two points on a graph
    """
    while True:
        point_one_str = ask_question("What is the first point? Sperate the two points by a comma.\n", "str").split(",")
        point_one = []
        for point in point_one_str:
            number_point = float(point)
            point_one.append(number_point)
        point_two_str = ask_question("What is the second point? Sperate the two points by a comma.\n", "str").split(",")
        point_two = []
        for point in point_two_str:
            number_point = float(point)
            point_two.append(number_point)
        x_movements = (point_two[0] - point_one[0]) ** 2
        y_movements = (point_two[1] - point_one[1]) ** 2
        added_movements = x_movements + y_movements
        final_square_root = added_movements ** (0.5)
        print("")
        print("------------------------")
        print("The distance between the two points is:")
        print(final_square_root)
        print("------------------------")
        print("")
        continue_question = input("Would you like to do another calculation?\n")
        if "y" in continue_question.lower():
            spacer()
            continue
        else:
            break


distance()
