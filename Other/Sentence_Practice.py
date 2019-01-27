def oral_practice():
    starting_sentence = input("What is the line you are trying to remember?\n")  # Starting question
    for i in range(48):  # Loop that will make a ton of lines so the user can't see the phase the phrase that they put in so they can't cheat
        print("")
    number_of_tries = 0
    number_of_times_correct = 0
    filler = 0
    while filler == 0:
        guess = input("Now try and rewrite the string!\n")
        if guess == starting_sentence:
            print("")
            print("You got it right!")
            number_of_times_correct += 1
            number_of_tries += 1
            continue_answer = input("Do you wanna continue? If you do type 1 and of not then type 0\n")
            continue_answer_casted = int(continue_answer)
            if continue_answer_casted == 0:
                break
            else:
                for i in range(48):
                    print("")
                continue
        else:
            print("")
            print("You got it wrong!")
            number_of_tries += 1
            continue
    average_correct = number_of_tries / number_of_times_correct
    print("")
    print("------------------------------------------")
    print("Now that you are done here are your stats:")
    print("")
    print("You answered", number_of_tries, "times")
    print("You got it right", number_of_times_correct, "times")
    print("")
    print("You average amount right is:",average_correct)
    print("------------------------------------------")


oral_practice()
