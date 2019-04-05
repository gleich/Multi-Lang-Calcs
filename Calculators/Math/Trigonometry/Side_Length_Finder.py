import math

def spacer():
    for i  in range(40):
        print("\n")


while True:
    important_values = {
                    "reference angle": None,
                    "hypotenuse": None,
                    "opposite": None,
                    "adjacent": None,
                    }
    print("Do note that this program only works with right triangles")
    reference_angle_str = str(input("What is the the reference angle? If the reference angle is Theda than just put a t\n"))
    try:
        reference_angle = float(reference_angle_str)
        important_values["reference angle"] = reference_angle
        spacer()
        print("The refence angle is now regestered as:", important_values["reference angle"])
    except ValueError:
        important_values["reference angle"] = reference_angle_str
        spacer()
        print("The reference angle is now regestered as theda")
    hyp_length_str = str(input("What is length of the side accross from the right angle? If there is nothing answer nothing and if it is x than just put x.\n"))
    try:
        hyp_length = float(hyp_length_str)
        important_values["hypotenuse"] = hyp_length
        spacer()
        print("The length of the hypotenuse side is now set to:", important_values["hypotenuse"])
    except ValueError:
        important_values["hypotenuse"] = hyp_length_str
        spacer()
        if "x" in hyp_length_str:
            print("The length of the hypotenuse side is now set to: x")
        else:
            print("The length of the hypotenuse side is now set to:",hyp_length_str)  # Should mean that it is none.
    adj_length_str = str(input("What is the length of the adjacent side? If there is nothing answer nothing and if it is x than just put x.\n"))
    try:
        adj_length = float(adj_length_str)
        important_values["adjacent"] = adj_length
        spacer()
        print("The adjacent side length is now regestered as:", important_values["adjacent"])
    except ValueError:
        important_values["adjacent"] = adj_length_str
        spacer()
        if "x" in adj_length_str:
            print("The length of the adjacent side is now set to: x\n")
        else:
            print("The length of the adjacent side is now set to:",adj_length_str,"\n")
    opp_len_str = str(input("What is the last side length? If there is nothing answer nothing and if it is x than just put x.\n"))
    try:
        opp_len = float(opp_len_str)
        important_values["opposite"] = opp_len
    except ValueError:
        important_values["opposite"] = opp_len_str
        spacer()
        if "x" in opp_len_str:
            print("The length of the opposite side is now set to: x\n")
        else:
            print("The length of the opposite side is now set to:",opp_len_str,"\n")

    if "t" in str(important_values["reference angle"]).lower():  # checks to see if are using theda
        if "n" in important_values["opposite"].lower():  # cos
            answer = str(important_values["adjacent"] / important_values["hypotenuse"])
            print("cos(theda) = " + answer)
            print("Reasoning:")
            print("The reason that we use cosine is because we don't use/know the opposite side length")
            print("We get: " + answer + " by doing " + str(important_values["adjacent"]) + " (adjacent side legnth) +" + str(important_values["hypotenuse"]) + " (hypotenuse side legnth)")
            continue_question = input("Would you like to do another caluculation?\n")
            if "y" in continue_question.lower():
                spacer()
                continue
            else:
                break
        elif "n" in important_values["adjacent"].lower():  # sin
            answer = str(important_values["opposite"] / important_values["hypotenuse"])
            print("sin(theda) = " + answer)
            print("Reasoning:")
            print("The reason that we use sine is because we don't use/know the adjacent side legth")
            print("We get: " + answer + " by doing " + str(important_values["opposite"]) + " (opposite side legnth) +" + str(important_values["hypotenuse"]) + " (hypotenuse side legnth)")
            continue_question = input("Would you like to do another caluculation?\n")
            if "y" in continue_question.lower():
                spacer()
                continue
            else:
                break
        elif "n" in important_values["hypotenuse"].lower():
            answer = str(important_values["opposite"] / important_values["adjacent"])
            print("tan(theda) = " + answer)
            print("Reasoning:")
            print("The reason that we use tangent is because we don't use/know the hypotenuse side length")
            print("We get: " + answer + " by doing " + str(important_values["opposite"]) + " (opposite side legnth) +" + str(important_values["adjacent"]) + " (adjacent side legnth)")
            continue_question = input("Would you like to do another caluculation?\n")
            if "y" in continue_question.lower():
                spacer()
                continue
            else:
                break
        else:
            print("Error")
            continue_question = input("Would you like to do another caluculation?\n")
            if "y" in continue_question.lower():
                spacer()
                continue
            else:
                break
    else:
        if "n" in important_values["hypotenuse"].lower() and "x" in important_values["adjacent"].lower():
            answer = important_values["opposite"] / math.tan(math.radians(important_values["reference angle"]))
            print("x is approximately " + answer)
            print("Reasoning:")
            print("xtan({reference}) = ".format(reference=important_values[reference_angle]) + important_values["opposite"])
            continue_question = input("Would you like to do another caluculation?\n")
            if "y" in continue_question.lower():
                spacer()
                continue
            else:
                break
        elif "n" in important_values["hypotenuse"].lower() and "x" in important_values["opposite"].lower():
            answer = important_values["adjacent"] * math.tan(math.radians(important_values["reference angle"]))
            print("x is approximately " + answer)
            print("Reasoning:")
            print("x = {adjacent} * tan({reference})".format(adjacent=important_values["adjacent"], reference=important_values[reference_angle]))
            continue_question = input("Would you like to do another caluculation?\n")
            if "y" in continue_question.lower():
                spacer()
                continue
            else:
                break
        elif "n" in important_values["adjacent"].lower() and "x" in 
