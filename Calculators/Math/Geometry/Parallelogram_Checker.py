# This file now works and just needs to be run!
#--------------------------------------------------------------------
while 0 == 0:
    # Distance formula:
    def distance_finder(x1,y1,x2,y2):
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        return distance

    def slope_finder(x1,y1,x2,y2):
        slope = ((y2 - y1) / (x2 - x1))
        return slope

    initial_input = input("What are you given, points or degrees?\n")

    if "p" in initial_input.lower():
        print("")
        points = input("Please list all the coordinates of each point counter-clockwise. Please separate each point by a comma.\n")
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

        distance_from_1to2S = distance_finder(point1_x, point1_y, point2_x, point2_y)
        distance_from_3to4S = distance_finder(point3_x, point3_y, point4_x, point4_y)
        distance_from_2to3S = distance_finder(point2_x, point2_y, point3_x, point3_y)
        distance_from_4to1S = distance_finder(point4_x, point4_y, point1_x, point1_y)
        distance_from_2to4D = distance_finder(point2_x, point2_y, point4_x, point4_y)
        distance_from_3to1D = distance_finder(point3_x, point3_y, point1_x, point1_y)
        slope_of_2to3S = slope_finder(point2_x, point2_y, point3_x, point3_y)
        slope_of_1to4S = slope_finder(point1_x, point1_y, point4_x, point4_y)
        slope_of_2to1S = slope_finder(point2_x, point2_y, point1_x, point1_y)
        slope_of_3to4S = slope_finder(point3_x, point3_y, point4_x, point4_y)

        if distance_from_1to2S == distance_from_2to3S and distance_from_1to2S == distance_from_4to1S and distance_from_2to4D == distance_from_3to1D:
            print("")
            print("-------------------------------------------------------")
            print("The four points form a square\n")
            print("Explanation:")
            print("All four sides are the same length and diagonals are the same length\n")
            print("Proof:")
            print("Distance from point 1 to point 2 (" + str(distance_from_1to2S) + ") is equal to the distance of point 3 to point 4 (" + str(distance_from_3to4S) + (")"))
            print("Distance from point 2 to point 3 (" + str(distance_from_2to3S) + ") is equal to the distance of point 4 to point 1 (" + str(distance_from_4to1S) + (")"))
            print("Distance from point 2 to point 4 (" + str(distance_from_2to4D) + ") is equal to the distance of point 3 to point 1 (" + str(distance_from_3to1D) + (")\n"))
            continue_question = input("Would you like to do another calculation?\n")
            if "y" in continue_question.lower():
                continue
            else:
                break
        elif distance_from_2to4D == distance_from_3to1D and slope_of_1to4S == slope_of_2to3S:
            print("")
            print("-------------------------------------------------------")
            print("The four points form a rectangle\n")
            print("Explanation:")
            print("All diagonals are the same length and both sides have the same length\n")
            print("Proof:")
            print("Distance from point 2 to point 4 (" + str(distance_from_2to4D) + ") is equal to the distance of point 3 to point 1 (" + str(distance_from_3to1D) + (")\n"))
            continue_question = input("Would you like to do another calculation?\n")
            if "y" in continue_question.lower():
                continue
            else:
                break
        elif distance_from_1to2S == distance_from_2to3S and distance_from_1to2S == distance_from_4to1S:
            print("")
            print("-------------------------------------------------------")
            print("The four points form a rhombus\n")
            print("Explanation:")
            print("All four sides are the same length\n")
            print("Proof:")
            print("Distance from point 1 to point 2 (" + str(distance_from_1to2S) + ") is equal to the distance of point 3 to point 4 (" + str(distance_from_3to4S) + (")"))
            print("Distance from point 2 to point 3 (" + str(distance_from_2to3S) + ") is equal to the distance of point 4 to point 1 (" + str(distance_from_4to1S) + (")\n"))
            continue_question = input("Would you like to do another calculation?\n")
            if "y" in continue_question.lower():
                continue
            else:
                break
        elif slope_of_2to1S == slope_of_3to4S:
            print("")
            print("-------------------------------------------------------")
            print("The four points form a Trapezoid\n")
            print("Explanation:")
            print("All base sides are congruent and all diagonals are not congruent. All legs don't have the same slope as well.\n")
            print("Proof:")
            print("Distance from point 1 to point 2 (" + str(distance_from_1to2S) + ") is equal to the distance of point 3 to point 4 (" + str(distance_from_3to4S) + (")"))
            print("Distance from point 2 to point 3 (" + str(distance_from_2to3S) + ") is equal to the distance of point 4 to point 1 (" + str(distance_from_4to1S) + (")"))
            print("Distance from point 2 to point 4 (" + str(distance_from_2to4D) + ") is equal to the distance of point 3 to point 1 (" + str(distance_from_3to1D) + (")\n"))
            print("Other info:")
            print("Length of top: " + str(distance_from_3to4S))
            length_of_middle = 0.5 * (distance_from_3to4S + distance_from_1to2S)
            print("Length of middle: " + str(length_of_middle))
            print("Length of bottom: " + str(distance_from_1to2S))
            continue_question = input("Would you like to do another calculation?\n")
            if "y" in continue_question.lower():
                continue
            else:
                break
        elif distance_from_2to3S == distance_from_4to1S and slope_of_3to4S == slope_of_2to1S and distance_from_2to4D == distance_from_3to1D:
            print("")
            print("-------------------------------------------------------")
            print("The four points form a Isosceles Trapezoid\n")
            print("Explanation:")
            print("Both diagonals are congruent, bases are congruent, and legs are congruent\n")
            print("Proof:")
            print("Distance from point 1 to point 2 (" + str(distance_from_1to2S) + ") is equal to the distance of point 3 to point 4 (" + str(distance_from_3to4S) + (")"))
            print("Distance from point 2 to point 3 (" + str(distance_from_2to3S) + ") is equal to the distance of point 4 to point 1 (" + str(distance_from_4to1S) + (")"))
            print("Distance from point 2 to point 4 (" + str(distance_from_2to4D) + ") is equal to the distance of point 3 to point 1 (" + str(distance_from_3to1D) + (")\n"))
            print("Other info:")
            print("Length of top: " + str(distance_from_3to4S))
            length_of_middle = 0.5 * (distance_from_3to4S + distance_from_1to2S)
            print("Length of middle: " + str(length_of_middle))
            print("Length of bottom: " + str(distance_from_1to2S))
            continue_question = input("Would you like to do another calculation?\n")
            if "y" in continue_question.lower():
                continue
            else:
                print("")
                break
        elif distance_from_1to2S == distance_from_3to4S and distance_from_2to3S == distance_from_4to1S:
            print("")
            print("-------------------------------------------------------")
            print("The four points form a parallelogram\n")
            print("Explanation:")
            print("There are two sets of congruent sides\n")
            print("Proof:")
            print("Distance from point 1 to point 2 (" + str(distance_from_1to2S) + ") is equal to the distance of point 3 to point 4 (" + str(distance_from_3to4S) + (")"))
            print("Distance from point 2 to point 3 (" + str(distance_from_2to3S) + ") is equal to the distance of point 4 to point 1 (" + str(distance_from_4to1S) + (")"))
            print("Distance from point 2 to point 4 (" + str(distance_from_2to4D) + ") is equal to the distance of point 3 to point 1 (" + str(distance_from_3to1D) + (")\n"))
            continue_question = input("Would you like to do another calculation?\n")
            if "y" in continue_question.lower():
                continue
            else:
                break
        else:
            print("")
            print("-------------------------------------------------------")
            print("The four points don't form a parallelogram\n")
            print("Explanation:")
            print("More than two sides are not the same length\n")
            print("Proof:")
            print("Distance from point 1 to point 2 (" + str(distance_from_1to2S) + ") is equal to the distance of point 3 to point 4 (" + str(distance_from_3to4S) + (")"))
            print("Distance from point 2 to point 3 (" + str(distance_from_2to3S) + ") is equal to the distance of point 4 to point 1 (" + str(distance_from_4to1S) + (")"))
            print("Distance from point 2 to point 4 (" + str(distance_from_2to4D) + ") is equal to the distance of point 3 to point 1 (" + str(distance_from_3to1D) + (")\n"))
            continue_question = input("Would you like to do another calculation?\n")
            if "y" in continue_question.lower():
                continue
            else:
                print("")
                break
