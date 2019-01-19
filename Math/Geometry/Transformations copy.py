def transformations(movement_type, movement_spec, points):
    if 'tran' in movement_type.lower():
        X_movement = movement_spec[0] #This is the movement on the X
        Y_movement = movement_spec[1] #This is the movement on the Y
        First_movement = X_movement + points[0]
        Second_movement = Y_movement + points[1]
        print("") #Easier output reading
        print ("Start-----------------------------------------------------------") #Easier output reading
        print ("The new set of points for the translation of " + "(" + str(points[0]) + "," + str(points[1]) + ") " + "is: " + "(" + str(First_movement) + "," + str(Second_movement) + ")")
        print ("End-------------------------------------------------------------") #Easier output reading
        print("") #Easier output reading
    elif movement_type == "Rotation" and movement_spec == 90: #This is for a rotation of 90 degrees if Y is positive
        First_movement = points[1] - (points[1] * 2) #This is making the Y point negative
        print("") #Easier output reading
        print ("Start-----------------------------------------------------------") #Easier output reading
        print ("The new set of points for the rotation of " + "(" + str(points[0]) + "," + str(points[1]) + ") " + "is: " + "(" + str(points[1]) + "," + str(First_movement) + ")")
        print ("End-------------------------------------------------------------")
        print("") #Easier output reading
    elif movement_type == "Rotation" and movement_spec == 180: #This is for a rotation of 180 degrees
        First_movement = points[0] - (points[0] * 2) #This is making the X point negative
        Second_movement = points[1] - (points[1] * 2) #This is making the Y point negative
        print("") #Easier output reading
        print ("Start-----------------------------------------------------------") #Easier output reading
        print ("The new set of points for the rotation of " + "(" + str(points[0]) + "," + str(points[1]) + ") " + "is: " + "(" + str(First_movement) + "," + str(Second_movement) + ")")
        print ("End-------------------------------------------------------------") #Easier output reading
        print("") #Easier output reading
    elif movement_type == "Rotation" and movement_spec == 270: #This is for a rotation of 270 degrees
        First_movement = points[1] #This is swaping X with Y
        Second_movement = points[0] - (points[0] * 2) #This is making the X point negative
        print("") #Easier output reading
        print ("Start-----------------------------------------------------------") #Easier output reading
        print ("The new set of points for the rotation of "  + "(" + str(points[0]) + "," + str(points[1]) + ") " + "is: " + "(" + str(First_movement) + "," + str(Second_movement) + ")")
        print ("End-------------------------------------------------------------") #Easier output reading
        print("") #Easier output reading
    elif movement_type == "Reflection" and movement_spec == "y_axis":
        First_movement = points[1] - (points[1] * 2) #This is making the Y point negative
        print("") #Easier output reading
        print ("Start-----------------------------------------------------------") #Easier output reading
        print ("The new set of points for the reflection of "  + "(" + str(points[0]) + "," + str(points[1]) + ") " + "is: " + "("  + str(points[1]) + "," + str(First_movement) + ")")
        print ("End-------------------------------------------------------------") #Easier output reading
        print("") #Easier output reading
    elif movement_type == "Reflection" and movement_spec == "x_axis":
        First_movement = points[0] - (points[0] * 2) #This is making the X point negative
        print("") #Easier output reading
        print ("Start-----------------------------------------------------------") #Easier output reading
        print ("The new set of points for the reflection of "  + "(" + str(points[0]) + "," + str(points[1]) + ") " + "is: " + "("  + str(points[1]) + "," + str(First_movement) + ")")
        print ("End-------------------------------------------------------------") #Easier output reading
        print("") #Easier output reading
    elif movement_type == "Reflection" and movement_spec[0] == "X": #If it is intending to be reflected in the X-axis
        First_movement = movement_spec[1] + points[1] #When it being reflected in the X-axis it is really being reflected in the Y-axis
        print("") #Easier output reading
        print ("Start-----------------------------------------------------------") #Easier output reading
        print ("The new set of points for the rotation of "  + "(" + str(points[0]) + "," + str(points[1]) + ") " + "is: " + "("  + str(points[1]) + "," + str(First_movement) + ")")
        print ("End-------------------------------------------------------------") #Easier output reading
        print("") #Easier output reading
    elif movement_type == "Reflection" and movement_spec[0] == "Y": #If it is intending to be reflected in the Y-axis
        First_movement = movement_spec[1] + points[0] #When it being reflected in the Y-axis it is really being reflected in the X-axisprint("")
        print("") #Easier output reading
        print ("Start-----------------------------------------------------------") #Easier output reading
        print ("The new set of points ofr the reflection of "  + "(" + str(points[0]) + "," + str(points[1]) + ") " + "is: " + "("  "(" + str(First_movement) + "," + str(points[1]) + ")")
        print ("End-------------------------------------------------------------") #Easier output reading
        print("") #Easier output reading
    elif movement_type == "Dilation":
        First_movement = points[0] * movement_spec #This is taking the X point and multiplying it with the scale factor
        Second_movement = points[1] * movement_spec #This is taking the Y point and multiplying it with the scale factor
        print("") #Easier output reading
        print ("Start-----------------------------------------------------------") #Easier output reading
        print ("The new set of points for the dilation of "  + "(" + str(points[0]) + "," + str(points[1]) + ") " + "is: " + "("  + str(First_movement) + "," + str(Second_movement) + ")")
        print ("End-------------------------------------------------------------") #Easier output reading
        print("") #Easier output reading
    else:
        print ("Something went wrong. Check if everything is put in the right way!")

#Examples for Translation:
transformations("translation",[1,2],[2,3]) #Translation can be called with "translation"
#transformations("Translation",[1,2],[2,0]) #Translation can be called with "Translation"
#transformations("Trans",[1,2],[2,7]) #Translation can be called with "Trans"
#transformations("tran",[1,2],[5,8]) #Translation can be called with "tran"
#transformations("Tran",[1,2],[1,4]) #Translation can be called with "Tran"
#transformations("trans",[1,2],[0,2]) #Translation can be called with "Trans"

#Examples for Rotation:
transformations("Rotation",90,[2,3]) #Rotation with a 90 degree turn
#transformations("Rotation",180,[2,0]) #Rotation with a 180 degree turn
#transformations("Rotation",270,[2,7]) #Rotation with a 270 degree turn=
#transformations("Reflection", "y_axis",[2,7]) #Reflection in the y-axis
#transformations("Reflection",["X",3],[5,8]) #Reflection in the x-axis
#transformations("Reflection",["Y",2],[1,4]) #Reflection in the y-axis

#Examples for Dilation:
#transformations("Dilation",0.5,[2,3]) #Dilation with an reduction
#transformations("Dilation",-3,[2,7]) #Dilation wih an enlargement
