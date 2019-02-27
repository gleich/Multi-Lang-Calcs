# Instructions:
# Just run the file and answer the questions!
# --------------------------------------------------------------------
while True:
    def slope_finder(x1,y1,x2,y2):
        slope = ((y2 - y1) / (x2 - x1))
        return slope

    two_points = input("What are the two points that you think the line of best fit will be connected to? Separate each number with a comma\n")
    two_points_str = two_points.split(",")

    two_points_int = []
    for string in two_points_str:
        new_number = int(string)
        two_points_int.append(new_number)

    m = slope_finder(two_points_int[0],two_points_int[1],two_points_int[2],two_points_int[3])
    y = two_points_int[1]
    x = two_points_int[0]
    new_y = y/x
    b = new_y - m

    if b < 0:
        print("The approximate equation for the line of best fit is y=" + str(m) + "x " + str(b))
        continue_question = input("Would you like to do another calculation?\n")
        if "y" in continue_question.lower():
            continue
        else:
            break
    else:
        print("The approximate equation for the line of best fit is y=" + str(m) + "x +" + str(b))
        continue_question = input("Would you like to do another calculation?\n")
        if "y" in continue_question.lower():
            continue
        else:
            break
