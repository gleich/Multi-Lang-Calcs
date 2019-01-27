#Instructions:
#Go the bottom of the file and edit the inputs for what you need done
#--------------------------------------------------------------------

def distance(line_points):
    x_movements = (line_points[1] - line_points[0]) ** 2
    y_movements = (line_points[3] - line_points[2]) ** 2
    added_movements = x_movements + y_movements
    final_square_root = added_movements**(0.5)
    
    print("\n------------------------")
    print("The distance formula is:\n",final_square_root)
    print("------------------------\n")

#Example:
distance([10,2,7,5])
