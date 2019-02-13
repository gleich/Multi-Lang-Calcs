# This file is still being rebuilt and can't be used right now. It will be done in a few days or so...
#--------------------------------------------------------------------

# Distance formula:
def distance_finder(x1,y1,x2,y2):
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

inital_input = input("What are you given, points or degrees?\n")

if "p" in inital_input.lower():
    first_point_input_question = \
    """
    For this step you will need to graph the shape.
    Once you have graphed them please type the coordinates of each point counter-clockwise
    Please seperate each point by a comma!
    """
    points = input(first_point_input_question)
    points_list_org = points.split(",")
    points_list = []

    for number in points_list_org:
        new_number = int(number)
        points_list.append(new_number)

    #Point 1 Coordinates:
    point1_x = points_list[0]
    point1_y = points_list[1]

    #Point 2 Coordinates:
    point2_x = points_list[2]
    point2_y = points_list[3]

    #Point 3 Coordinates:
    point3_x = points_list[4]
    point3_y = points_list[5]

    #Point 4 Coordinates:
    point4_x = points_list[6]
    point4_y = points_list[7]

    distance_from_1to2S = distance_finder(point1_x,point1_y,point2_x,point2_y)
    distance_from_3to4S = distance_finder(point3_x,point3_y,point4_x,point4_y)
    distance_from_2to3S = distance_finder(point2_x,point2_y,point3_x,point3_y)
    distance_from_4to1S = distance_finder(point4_x,point4_y,point1_x,point1_y)
    distance_from_

    if distance_from_1to2S == distance_from_3to4S or distance_from_4to1S == distance_from_2to3S:
        if distance_from_1to2S == distance_from_3to4S and distance_from_4to1S == distance_from_2to3S:
            print("")
            print("---------------------")
            print("The shape is a square\n")
            print("Explanation:")
            print("The reason that these shape is a square is because there are four congruent sides\n")
            print("Proof:")
            print("First distance:",distance_from_1to2S)
            print("Second distrance:",distance_from_3to4S)
            print("Third distance:",distance_from_4to1S)
            print("Fourth distance:",distance_from_2to3S)
            print("---------------------")
        elif distance_from_1to2S == distance_from_3to4S and distance_from_4to1S == distance_from_2to3S or distance_from_1to2S == distance_from_2to3S and distance_from_3to4S == distance_from_4to1S:
            print("")
            print("---------------------")
            print("The shape is a square\n")
            print("Explanation:")
            print("The reason that these shape is a rectangle is because there are two pairs of congruent sides\n")
            print("Proof:")
            print("First distance:",distance_from_1to2S)
            print("Second distrance:",distance_from_3to4S)
            print("Third distance:",distance_from_4to1S)
            print("Fourth distance:",distance_from_2to3S)
            print("---------------------")
        elif
