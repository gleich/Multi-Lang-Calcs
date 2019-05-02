# NOTICE:
# This file is currently under construction, please do not use!


def seperator():
    """
    Will clear the output screen for the user:
    """
    for i in range(50):
        print("\n")


def ask_question(question,cast_type):
    """
    Will ask the user a question and cast the answer.
    :param question: the question that will be asked to the user
    :param cast_type: what the question will be casted as
    """
    if "int" in cast_type:
        users_input = int(input(question))
        return users_input
    elif "float" in cast_type:
        users_input = float(input(question))
        return users_input
    elif "bool" in cast_type:
        users_input = bool(input(question))
        return users_input
    elif "list" in cast_type:
        users_input = list(input(question))
        return users_input
    else:
        users_input = input(question)
        return users_input





while True:

    ask_question =
