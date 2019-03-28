while True:
    calculation_type = input("What are you trying to do, Velocity or Speed?\n")
    if "spe" in calculation_type.lower():
        seperator = "\n\n\n\n\n\n\n\n\n\n\n"
        print(seperator)
        distance = float(input("What is the distance?\n"))
        print(seperator)
        time = float(input("What is the time?\n"))
        print(seperator)
        speed = distance / time
        print(seperator)
        print("Speed =", speed)
        continue_question = input("Would you like to do another calculation?\n")
        if "y" in continue_question.lower():
            for i in range(15):
                print("")
            continue
        else:
            break
