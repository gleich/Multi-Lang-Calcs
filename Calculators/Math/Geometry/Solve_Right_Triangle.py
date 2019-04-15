# Instructions:
# Just run the file and answer the questions.
# -------------------------------------------
import math


def pythagorean_theorem(side_one,side_two):
    """
    Will find the missing side of a right triangle when given two other side lengths
    :param one of the other side lengths
    :param the other known side length
    :return the third side length
    """
    side_three_squared = side_one**2 + side_two**2
    side_three = math.sqrt(c_squared)
    return side_three


def spacer():
    for i in range(30):
        print("\n")


def correct_form(string,integer):
    """
    Will replace user input with it's correct form
    :param string that is going to be checked
        :type str
    :param if the string would like to become an int or a float
        :type boolean
    :return float,int,boolean, or str
    """
    if "none" in string.lower():
        return False
    elif integer:
        return int(string)
    elif integer == False:
        return float(string)
    else:
        return string


def ask_question(question):
    """
    Will ask the user a question
    :param the question that will be asked
    :return user's response
    """
    question_str = str(question)
    user_input = input(question_str)
    spacer()
    return user_input


def is_a_type(object,check_type):
    """
    Will return True is an object is what type is the user is checking for
    :param the object that is going to be checked
    :param what the object is being check to be
    :return type
        :type string
    """
    if "int" in check_type.lower() and type(object) == type(1):
        return True
    elif "str" in check_type.lower() and type(object) == type(""):
        return True
    elif "float" in check_type.lower() and type(object) == type(1.0):
        return True
    elif "boolean" in check_type.lower() and type(object) == type(True):
        return True
    elif "num" in check_type.lower() and type(object) == type(1) or type(object) == type(1.0):
        return True
    else:
        return False


while True:
    is_a_variable = "string"

    hypotenuse_str = ask_question("What is the side length of the hypotenuse side? If you don't know than just say none and if it a variable just put x.\n")
    adjacent_str = ask_question("What is the side length of the adjacent side? If you don't know than just say none and if it a variable just put x.\n")
    opposite_str = ask_question("What is the side length of the opposite side? If you don't know than just say none and if it a variable just put x.\n")

    hypotenuse = correct_form(hypotenuse_str,False)
    adjacent = correct_form(adjacent_str,False)
    opposite = correct_form(opposite_str,False)

    solving_direction = ask_question("What are you trying to find (opposite, hypotenuse, adjacent)?\n")

    if adjacent == False and is_a_type(opposite,"num") and is_a_type(hypotenuse,"num"):
        answer = opposite / hypotenuse
        print("The answer is:",answer)
        print("Explanation:")
        print("Because we don't know the adjacent side length, we can only use sin")
        print(opposite,"/",hypotenuse,"\n")
        continue_question = input("Would you like to do another caluclation?\n")
        if "y" in continue_question:
            spacer()
            continue
        else:
            break
    elif is_a_type(adjacent,"num") and opposite == False and is_a_type(hypotenuse,"num"):
        answer = adjacent / hypotenuse
        print("The answer is:",answer)
        print("Explanation:")
        print("Because we don't know the oppoiste side length, we can only use cos")
        print(adjacent,"/",hypotenuse,"\n")
        continue_question = input("Would you like to do another caluclation?\n")
        if "y" in continue_question:
            spacer()
            continue
        else:
            break
    elif is_a_type(adjacent,"num") and is_a_type(opposite,"num") and hypotenuse == False:
        answer = opposite / adjacent
        print("The answer is:",answer)
        print("Explanation:")
        print("Because we don't know the hypotenuse side length, we can only use tan")
        print(opposite,"/",adjacent,"\n")
        continue_question = input("Would you like to do another caluclation?\n")
        if "y" in continue_question:
            spacer()
            continue
        else:
            break
    elif is_a_type(adjacent,is_a_variable):
        angle = ask_question("What is the angle of the angle that is not 90 degrees?\n")
        if is_a_type(opposite,"num"):
