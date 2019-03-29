while True:

    def list_nums(question, seperator):
        """
        Get a list of numbers that the uder supplies.
        :parameter String which is the question getting asked
        :parameter What the seperator of the numbers should be
        :return lst of ints
        """
        nums = input("{quest}. Each number should be seperated by a {sep}\n".format(quest=question,sep=seperator))
        lst_int = []
        for string in nums.split(seperator):
            integer = float(string)
            lst_int.append(integer)
        return lst_int

    def find_motion():
        """
        Get the speed of a certain object
        :return int
        """
        numbers = list_nums("What is the time and distance? Example answer: 2.34,400", ",")
        speed = round(numbers[1] / numbers[0])
        return speed

    print("Speed:", str(find_motion(), "mph"))
    print("")
    continue_question = input("Would you like to do another calculation?\n")
    if "y" in continue_question.lower():
        for i in range(20):
            print("\n")
        continue
    else:
        break
