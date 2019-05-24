# Instructions:
# Just run the file and answer the quesitons!
#--------------------------------------------------------------------
def distance(line_points):
    x_movements = (line_points[1] - line_points[0]) ** 2
    y_movements = (line_points[3] - line_points[2]) ** 2
    added_movements = x_movements + y_movements
    final_square_root = added_movements**(0.5)
    print("")
    print("------------------------")
    print("The distance formula is:")
    print(final_square_root)
    print("------------------------")
    print("")

#Example:
distance([10,2,7,5])
