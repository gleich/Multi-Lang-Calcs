def find_distance(acceleration_str, time_str):
    acceleration_num = float(acceleration_str)
    time_num = float(time_str)
    distance_answer = (0.5 * acceleration_num * time_num) ** 2
    return distance_answer


def find_acceleration(distance_str, time_str):
    distance_num = float(distance_str)
    time_num = float(time_str)
    acceleration_answer = (2 * distance_num) / (time_num ** 2)
    return acceleration_answer

def spacer():
    for i in range(30):
        print("\n")


while True:
    acceleration = input("What is the acceleration? If there is nothing then enter none.\n")
    time = input("What is the time? If there is nothing then enter none\n")
    if "n" in acceleration.lower():
        distance = input("What is the distance?\n")
        spacer()
        print("The acceleration is:",find_acceleration(distance, time))
        print("Work:")
        print("(2 * {distance_print_ref}) / ({time_print_ref}^2)".format(distance_print_ref=distance,time_print_ref=time))
        continue_question = input("Would you like to do another calculation?\n")
        if "y" in continue_question.lower():
            spacer()
            continue
        else:
            break
    elif "n" in time.lower():
        spacer()
        print("There is no time  supplied, this means that there is not enough information.")
        continue_question = input("Would you like to do another calculation?\n")
        if "y" in continue_question.lower():
            spacer()
            continue
        else:
            break
    else:
        spacer()
        print("The distance is:",find_distance(acceleration, time))
        print("Work:")
        print("(0.5 * {acceleration_print_ref} * {time_print_ref})^2".format(acceleration_print_ref=acceleration,time_print_ref=time))
        continue_question = input("Would you like to do another calculation?\n")
        if "y" in continue_question.lower():
            spacer()
            continue
        else:
            break
