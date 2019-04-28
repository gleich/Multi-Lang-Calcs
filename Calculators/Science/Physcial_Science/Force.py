# Instructions:
# Just run the file and answer the questions!
# -------------------------------------------


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
            print("Error!\n Re run the program and make sure that you are putting in valid inputs.")
            spacer()
    else:
        return input(question)
        spacer()


while True:
    solving_for_question = \
    """
    Which two of the three do you know?:
    1. Force
    2. Mass
    3. Acceleration
    """
    solving_for_answer = ask_question(solving_for_question, "str")

    if "2" in solving_for_answer and "3" in solving_for_answer:
        mass = ask_question("What is the mass?\n","float")
        acceleration = ask_question("What is the acceleration?\n", "float")
        answer = mass * acceleration
        print("Answer:")
        print(answer)
        print("Work:")
        print("{m} * {a}".format(m=mass,a=acceleration))
        continue_question = input("Would you like to do another calculation?\n")
        if "y" in continue_question.lower():
            spacer()
            continue
        else:
            break
    elif "1" in solving_for_answer and "2" in solving_for_answer:
        force = ask_question("What is the force?\n", "float")
        mass = ask_question("What is the mass?\n", "float")
        answer = force / mass
        print("Answer:")
        print(answer)
        print("Work:")
        print("{f} / {m}".format(f=force,m=mass))
        continue_question = input("Would you like to do another calculation?\n")
        if "y" in continue_question.lower():
            spacer()
            continue
        else:
            break
    elif "1" in solving_for_answer and "3" in solving_for_answer:
        force = ask_question("What is the force?\n", "float")
        acceleration = ask_question("What is the acceleration?\n", "float")
        answer = force / acceleration
        print("Answer:")
        print(answer)
        print("Work:")
        print("{f} / {a}".format(f=force,a=acceleration))
        continue_question = input("Would you like to do another calculation?\n")
        if "y" in continue_question.lower():
            spacer()
            continue
        else:
            break
    else:
        print("Error")
        continue_question = input("Would you like to restart the program?\n")
        if "y" in continue_question.lower():
            spacer()
            continue
        else:
            break
