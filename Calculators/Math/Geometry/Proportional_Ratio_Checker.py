# Instructions:
# Just run the file and answer the questions!
# --------------------------------------------------------------------
while 0 == 0:
    first_fraction_str = input("What is the first fraction? Please separate the two numbers by a comma!\n")
    print("")
    second_fraction_str = input("What is the second fraction? Please separate the two numbers by a comma\n")

    first_fraction_str = first_fraction_str.split(",")
    second_fraction_str = second_fraction_str.split(",")
    first_fraction = []
    second_fraction = []

    for number in first_fraction_str:
        new_number = int(number)
        first_fraction.append(new_number)

    for number in second_fraction_str:
        new_number = int(number)
        second_fraction.append(new_number)

    fraction1_simplest = (first_fraction[0] / first_fraction[0]) / (first_fraction[1] / first_fraction[0])
    fraction2_simplest = (second_fraction[0] / second_fraction[0]) / (second_fraction[1] / second_fraction[0])

    if fraction1_simplest == fraction2_simplest:
        print("")
        print("The two ratios form a proportion!")
        print("Ratio one's simplest form:", fraction1_simplest)
        print("Ratio two's simplest form:", fraction2_simplest)
        print("")
        continue_question = input("Would you like to do another calculation?\n")
        if "y" in continue_question.lower():
            for i in range(15):
                print("")
            continue
        else:
            break
    elif fraction1_simplest != fraction2_simplest:
        print("")
        print("The two ratios don't form a proportion!")
        print("Ratio one's simplest form:", fraction1_simplest)
        print("Ratio two's simplest form:", fraction2_simplest)
        print("")
        continue_question = input("Would you like to do another calculation?\n")
        if "y" in continue_question.lower():
            for i in range(15):
                print("")
            continue
        else:
            break
    else:
        print("")
        print("Please put in a valid data type")
        for i in range(15):
            print("")
        continue
