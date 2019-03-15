while True:
    init_data = input("List of the numbers counterclockwise and seperate each one with a comma. If you have a variable set it equal to x\n")

    nums_str = init_data.split(",")
    nums = []
    vars = []

    for string_item in nums_str:
        try:
            int_item = int(string_item)
            nums.append(int_item)
        except ValueError:
            if string_item.lower() == "x":
                vars.append(string_item.lower())
            else:
                print("Please only use x as the variable!")
                for i in range(15):
                    print("")
                continue

    if len(vars) >= 1:
        print("You can only have one variable!")
        for i in range(10):
            print("\n")
        continue
    elif len(nums) >= 4:
        print("There can only be three numbers!")
        for i in range(10):
            print("\n")
        continue

    def ratio_checker(numbers, variable):
        fraction_one = numbers[0] / numbers[1]
        scale_factor = fraction_one / numbers[3]
        print(variable,"=",scale_factor)


    continue_question = input("Would you like to do another calculation?\n")
    if "y" in continue_question.lower():
        for i in range(15):
            print("")
        continue
    else:
        break
